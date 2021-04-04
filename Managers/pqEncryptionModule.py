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
import base64
import json
from datetime import datetime

from aesModule import aesEncrypt, aesDecrypt

class PqEncryptionManager:    
    """This class handles everything around key en/decapsulation and file en/decryption using pq-algorithms and AES.
    Constructor:
        statisticsManager (StatisticsManager): existing instance of StatisticsManager for data collection
    Available public methods:
        encryptFile(fileToEncrypt:bytes, publicKeyStore:tuple) -> (ciphertext:bytes, encryptedFileObf:bytes)
        decryptFile(encryptedFileObf:bytes, ciphertext:bytes, privateKeyStore:tuple) -> decryptedFile:bytes
    """
    
    def __init__(self, statisticsManager):
        self.__statisticsManager = statisticsManager
        
        # dictionary is a substitue for switch case, which is absent in Python
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
    
    def encryptFile(self, fileToEncrypt:bytes, publicKeyStore:tuple) -> (bytes, bytes):
        if publicKeyStore[2] != "Public":
            raise ValueError("Public key is needed for encryption.")
        
        # obtain encapsulation function based on algorithm
        try:
            encapsulationFunction = self.encFuncDict[publicKeyStore[1]]
        except KeyError:
            raise ValueError("Wrong algorithm - probably chosen key for DSA algorithm")
        
        # create ciphertext used for later secretkey recovery and secretkey used for aes encryption and time it
        start = time.time()
        ciphertext, secret_key = encapsulationFunction(publicKeyStore[3])
        kemTime = time.time() - start
        
        # encrypt file with symmetric secretkey and time it
        start = time.time()
        encryptedFile = aesEncrypt(fileToEncrypt, secret_key)
        aesTime = time.time() - start

        # log operations
        self.__statisticsManager.addKemAesEntry(datetime.now(), publicKeyStore[1], "Encrypt", 256, len(fileToEncrypt), kemTime, aesTime)
        
        # obfuscate encrypted file
        encryptedFileObf = base64.b64encode(str(encryptedFile).encode())
        
        return ciphertext, encryptedFileObf
    
    def decryptFile(self, encryptedFileObf:bytes, ciphertext:bytes, privateKeyStore:tuple) -> bytes:
        if privateKeyStore[2] != "Private":
            raise ValueError("Private key is needed for decryption.")
        
        # obtain decapsulation function based on algorithm
        try:
            decapsulationFunction = self.decFuncDict[privateKeyStore[1]]
        except KeyError:
            raise ValueError("Wrong algorithm - probably chosen key for DSA algorithm")
        
        # derivate secretkey used for aes from ciphertext and public key of ciphertext's author and time it
        start = time.time()
        secret_key = decapsulationFunction(privateKeyStore[3], ciphertext)
        kemTime = time.time() - start
        
        # Defuscate encrypted file
        encryptedFile = json.loads(str(base64.b64decode(encryptedFileObf).decode()).replace("'", "\"") or "[]")
        
        # decrypt encryptedFile with secret key and time it
        start = time.time()
        decryptedFile = aesDecrypt(encryptedFile, secret_key)
        aesTime = time.time() - start

        # log operations and return decrypted file
        self.__statisticsManager.addKemAesEntry(datetime.now(), privateKeyStore[1], "Decrypt", 256, len(decryptedFile), kemTime, aesTime)
        return decryptedFile
        
# # TEST AREA
# # imports and init
# from statisticsModule import StatisticsManager
# from passwordsModule import PasswordManager
# from pqKeyGenModule import PqKeyGenManager
# import os
# import io
# import requests
# from PIL import Image
# import matplotlib.pyplot as plt

# pe = PqEncryptionManager(StatisticsManager())
# pm = PasswordManager("masterPassword")
# p = PqKeyGenManager(pm, StatisticsManager())

# # Clear secrets
# with open(os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database/secrets", 'w') as file:
#     file.write("")
    
# # Generate keypair which will be used to encrypt and decrypt image
# p.generate_keypair_saber("myName1")

# # Download example image and show it
# url = 'https://image.shutterstock.com/image-vector/example-red-square-grunge-stamp-260nw-327662909.jpg'
# data = requests.get(url).content
# img = Image.open(io.BytesIO(data))
# plt.imshow(img)
# plt.title("Before encryption")
# plt.figure()
# plt.show(block=False)

# # Convert image to bytes
# img_byte_arr = io.BytesIO()
# img.save(img_byte_arr, format='JPEG')

# # Encrypt image bytes
# encryptionOutput = pe.encryptFile(img_byte_arr.getvalue(), pm.loadKeyStoreList()[0])

# # Print encrypted file
# print(encryptionOutput[1])

# # Decrypt image bytes using cipher text and private key
# decryptionOutput = pe.decryptFile(encryptionOutput[1], encryptionOutput[0], pm.loadKeyStoreList()[1])

# # Convert bytes back to image and show it
# plt.imshow(Image.open(io.BytesIO(decryptionOutput)))
# plt.title("Encrypted+decrypted")
# plt.show()