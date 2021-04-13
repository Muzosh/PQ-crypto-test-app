# DSA

# from pqcrypto.sign.dilithium2 import generate_keypair, sign, verify
# from pqcrypto.sign.dilithium3 import generate_keypair, sign, verify
from pqcrypto.sign.dilithium4 import sign as sign_dilithium4, verify as verify_dilithium4
# from pqcrypto.sign.falcon_1024 import generate_keypair, sign, verify
# from pqcrypto.sign.falcon_512 import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_classic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_cyclic_compressed import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_classic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_cyclic_compressed import generate_keypair, sign, verify
from pqcrypto.sign.rainbowVc_classic import sign as sign_rainbowVc_classic, verify as verify_rainbowVc_classic
# from pqcrypto.sign.rainbowVc_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowVc_cyclic_compressed import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_128f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_128f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_128s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_128s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_192f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_192f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_192s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_192s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_256f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_256f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_256s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_haraka_256s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_128f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_128f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_128s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_128s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_192f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_192f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_192s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_192s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_256f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_256f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_256s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_sha256_256s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_128f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_128f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_128s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_128s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_192f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_192f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_192s_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_192s_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_256f_robust import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_256f_simple import generate_keypair, sign, verify
# from pqcrypto.sign.sphincs_shake256_256s_robust import generate_keypair, sign, verify
from pqcrypto.sign.sphincs_shake256_256s_simple import sign as sign_sphincs_shake256_256s_simple, verify as verify_sphincs_shake256_256s_simple

import time
import base64
from datetime import datetime

class PqSigningManager:
    """This class handles everything around file signing and verification using pq-algorithms.
    Constructor:
        statisticsManager (StatisticsManager): existing instance of StatisticsManager for data collection
    Available public methods:
        signFile(fileToSign:bytes, privateKeyStore:tuple) -> signatureObf:bytes
        verifySignature(signatureObf:bytes, signedFile:bytes, publicKeyStore:tuple) -> bool
    """
    
    def __init__(self, statisticsManager):
        self.__statisticsManager = statisticsManager
        
        # dictionary is a substitue for switch case, which is absent in Python
        self.signFuncDict = {
            "Dilithium": sign_dilithium4,
            "RainbowVc": sign_rainbowVc_classic,
            "Sphincs": sign_sphincs_shake256_256s_simple
        }
        
        self.verifyFuncDict = {
            "Dilithium": verify_dilithium4,
            "RainbowVc": verify_rainbowVc_classic,
            "Sphincs": verify_sphincs_shake256_256s_simple
        }
    
    def signFile(self, fileToSign:bytes, privateKeyStore:tuple) -> bytes:
        if privateKeyStore[2] != "Private":
            raise ValueError("Private key is needed for signing.")
        
        # obtain signing function based on algorithm
        try:
            signingFunction = self.signFuncDict[privateKeyStore[1]]
        except KeyError:
            raise ValueError("Wrong algorithm - probably chosen key for KEM algorithm")
        
        # sign file bytes using private key and time it
        start = time.time()
        signature = signingFunction(privateKeyStore[3], fileToSign)
        dsaTime = time.time() - start
        
        # log operations
        self.__statisticsManager.addDsaEntry(datetime.now(), privateKeyStore[1], "Sign", len(fileToSign), dsaTime/1000)
        
        # obfuscate signature
        signatureObf = base64.b64encode(signature)
        
        return signatureObf
    
    def verifySignature(self, signatureObf:bytes, signedFile:bytes, publicKeyStore:tuple) -> bool:
        if publicKeyStore[2] != "Public":
            raise ValueError("Public key is needed for signature verification.")
        
        # obtain verifying function based on algorithm
        try:
            verifyingFunction = self.verifyFuncDict[publicKeyStore[1]]
        except KeyError:
            raise ValueError("Wrong algorithm - probably chosen key for DSA algorithm")

        # Defuscate signature
        signature = base64.b64decode(signatureObf)
        
        # verify signature and time it
        start = time.time()
        verifyResult = verifyingFunction(publicKeyStore[3], signedFile, signature)
        dsaTime = time.time() - start

        # log operation and return verify result
        self.__statisticsManager.addDsaEntry(datetime.now(), publicKeyStore[1], "Verify", len(signedFile), dsaTime/1000)
        return verifyResult

# # TEST AREA
# # Imports and initialization
# import os
# from statisticsModule import StatisticsManager
# from passwordsModule import PasswordManager
# from pqKeyGenModule import PqKeyGenManager
# pm = PasswordManager("masterPassword")
# s = StatisticsManager()
# p = PqKeyGenManager(pm, s)
# ps = PqSigningManager(s)

# # Clear secrets
# with open(os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database/secrets", 'w') as file:
#     file.write("")

# # generate testing keypair
# p.generate_keypair_dilithium4()

# # create "file" (just bytes)
# fileToSign = b"Tohle je test"

# # create signature using private key from generated keypair
# signature = ps.signFile(fileToSign, pm.loadKeyStoreList()[1])

# # verify using public key from generated keypair and print result
# verifyResult = ps.verifySignature(signature, fileToSign, pm.loadKeyStoreList()[0])
# print("VerifyResult of the same file: ", verifyResult)

# # verify using public key from generated keypair and print result
# verifyResult = ps.verifySignature(signature, b"Tohle je test2", pm.loadKeyStoreList()[0])
# print("VerifyResult of slightly different file: ", verifyResult)