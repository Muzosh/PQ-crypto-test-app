from secrets import compare_digest
# from pqcrypto.kem.firesaber import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976shake import generate_keypair, encrypt, decrypt
from pqcrypto.kem.kyber1024 import encrypt as encapsulate_kyber1024, decrypt as decapsulate_kyber1024
# from pqcrypto.kem.kyber1024_90s import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.kyber512_90s import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.kyber768 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.kyber768_90s import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.lightsaber import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece348864 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece348864f import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece460896 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece460896f import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece6688128 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece6688128f import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece6960119 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece6960119f import generate_keypair, encrypt, decrypt
from pqcrypto.kem.mceliece8192128 import encrypt as encapsulate_mceliece8192128, decrypt as decapsulate_mceliece8192128
# from pqcrypto.kem.mceliece8192128f import generate_keypair, encrypt, decrypt
from pqcrypto.kem.ntruhps2048509 import encrypt as encapsulate_ntruhps2048509, decrypt as decapsulate_ntruhps2048509
# from pqcrypto.kem.ntruhps2048677 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhps4096821 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhrss701 import generate_keypair, encrypt, decrypt
from pqcrypto.kem.saber import encrypt as encapsulate_saber, decrypt as decapsulate_saber

import time
from datetime import datetime
from aesModule import aesEncrypt, aesDecrypt

class PqEncryptionManager:    
    def __init__(self, statisticsManager):
        self.__statisticsManager = statisticsManager
        
        self.encFuncDict = {
            "McLiece": encapsulate_mceliece8192128,
            "Saber": encapsulate_saber,
            "Kyber": encapsulate_kyber1024,
            "Nthrups": encapsulate_ntruhps2048509
        }
        
        self.decFuncDict = {
            "McLiece": decapsulate_mceliece8192128,
            "Saber": decapsulate_saber,
            "Kyber": decapsulate_kyber1024,
            "Nthrups": decapsulate_ntruhps2048509
        }
    
    def encryptFile(self, file:bytes, publicKeyStore:tuple) -> (bytes, bytes):
        if publicKeyStore[2] != "Public":
            raise ValueError("Public key is needed for encryption.")
        
        encapsulationFunction = self.encFuncDict[publicKeyStore[1]]
        
        start = time.time()
        ciphertext, secret_key = encapsulationFunction(publicKeyStore[3])
        kemTime = time.time() - start
        
        start = time.time()
        encryptedFile = aesEncrypt(file, secret_key)
        aesTime = time.time() - start

        self.__statisticsManager.addKemAesEntry(datetime.now(), publicKeyStore[1], "Encrypt", 256, kemTime, aesTime)
        return ciphertext, encryptedFile
    
    def decryptFile(self, encryptedFile:bytes, ciphertext:bytes, privateKeyStore:tuple):
        if privateKeyStore[2] != "Private":
            raise ValueError("Private key is needed for decryption.")
        
        decapsulationFunction = self.decFuncDict[privateKeyStore[1]]
        
        start = time.time()
        secret_key = decapsulationFunction(privateKeyStore[3], ciphertext)
        kemTime = time.time() - start
        
        start = time.time()
        decryptedFile = aesDecrypt(encryptedFile, secret_key)
        aesTime = time.time() - start

        self.__statisticsManager.addKemAesEntry(datetime.now(), privateKeyStore[1], "Decrypt", 256, kemTime, aesTime)
        return decryptedFile
        
# # TEST AREA
# from statisticsModule import StatisticsManager
# from passwordsModule import PasswordManager
# from pqKeyGenModule import PqKeyGenManager
# import os
# pe = PqEncryptionManager(StatisticsManager())

# pm = PasswordManager("masterPassword")
# p = PqKeyGenManager(pm, StatisticsManager())
# with open(os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database/secrets", 'w') as file:
#     file.write("")
# p.generate_keypair_saber("myName1")


# storeList = pm.loadKeyStoreList()

# publicLen = len(storeList[0][3])
# privateLen = len(storeList[1][3])

# encryptionOutput = pe.encryptFile(b"testFile", pm.loadKeyStoreList()[0])

# decryptionOutput = pe.decryptFile(encryptionOutput[1], encryptionOutput[0], pm.loadKeyStoreList()[1])
# print(decryptionOutput)