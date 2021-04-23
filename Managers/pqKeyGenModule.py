# KEM

from secrets import compare_digest
# from pqcrypto.kem.firesaber import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976shake import generate_keypair, encrypt, decrypt
from pqcrypto.kem.kyber1024 import generate_keypair as gen_kyber1024
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
from pqcrypto.kem.mceliece8192128 import generate_keypair as gen_mceliece
# from pqcrypto.kem.mceliece8192128f import generate_keypair, encrypt, decrypt
from pqcrypto.kem.ntruhps2048509 import generate_keypair as gen_ntruhps2048509
# from pqcrypto.kem.ntruhps2048677 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhps4096821 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhrss701 import generate_keypair, encrypt, decrypt
from pqcrypto.kem.saber import generate_keypair as gen_saber

# DSA

# from pqcrypto.sign.dilithium2 import generate_keypair, sign, verify
# from pqcrypto.sign.dilithium3 import generate_keypair, sign, verify
from pqcrypto.sign.dilithium4 import generate_keypair as gen_dilithium4
# from pqcrypto.sign.falcon_1024 import generate_keypair, sign, verify
# from pqcrypto.sign.falcon_512 import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_classic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_cyclic_compressed import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_classic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_cyclic_compressed import generate_keypair, sign, verify
from pqcrypto.sign.rainbowVc_classic import generate_keypair as gen_rainbowVc_classic
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
from pqcrypto.sign.sphincs_shake256_256s_simple import generate_keypair as gen_sphincs_shake256_256s_simple

import time
import random
import datetime
import collections.abc as cols

class PqKeyGenManager: 
    """
    This class generates key pairs using PQ algorithms and saves them into the database. It is recommended to reload keyStores list after generating keyPair.
    Constructor: 
        passwordManager (PasswordManager): existing instance of PasswordManager managing keyStores database
        statisticsManager (StatisticsManager): existing instance of StatisticsManager for data collection
    
    Available public methods:
        generate_keypair_mceliece8192128(name="") -> None
        generate_keypair_saber(name="") -> None
        generate_keypair_kyber1024(name="") -> None
        generate_keypair_ntruhps2048509(name="") -> None
        generate_keypair_dilithium4(name="") -> None
        generate_keypair_rainbowVc_classic(name="") -> None
        generate_keypair_sphincs_shake256_256s_simple(name="") -> None
    """
       
    def __init__(self, passwordManager, statisticsManager):
        """
        Constructor of the class:
            passwordManager (PasswordManager): existing instance of PasswordManager managing keyStores database
            statisticsManager (StatisticsManager): existing instance of StatisticsManager for data collection
        """
        self.__passwordManager = passwordManager
        self.__statisticsManager = statisticsManager

    
    def __RunKeyGen(self, generateFunction:cols.Callable[[], [bytes]], alg:str, name:str):
        """
        Private method that is used for measuring time of keypair generation and adding to database.
        
        Args:
            generateFunction (cols.Callable[[], [bytes]]): Specifies that methods takes a function (which returns bytes) as a argument so it can run it later
            alg (str): Name of the PQ algorithm
            name (str): Name that user set for keypair
        """
        # get current datetime
        now = datetime.datetime.now()
        
        # set name - random integer is here for easy private/public key pairing, then date, then user specified name
        nameText = "|"+ str(random.randint(0,999)) + "|" + str(now) + "|" + name
        
        # generate keypair and time it
        start = time.time()
        keyPair = generateFunction()
        keyGenTime = time.time() - start
        
        # log operation and add two keys into database
        self.__statisticsManager.addKeyGenEntry(now, alg, keyGenTime/1000)
        self.__passwordManager.addKeyStore(nameText, alg, "Public", keyPair[0])
        self.__passwordManager.addKeyStore(nameText, alg, "Private", keyPair[1])

    # KEM keypair generation
    def generate_keypair_mceliece8192128(self, name=""):
        """
        Generation of McEliece keypair with
            public key  - 1 357 824 B,
            private key - 14 080 B.
        """
        self.__RunKeyGen(gen_mceliece, "McEliece", name)

    def generate_keypair_saber(self, name=""):
        """
        Generation of SABER keypair with
            public key  - 992 B,
            private key - 2 304 B.
        """
        self.__RunKeyGen(gen_saber, "Saber", name)

    def generate_keypair_kyber1024(self, name=""):
        """
        Generation of Crystals-Kyber keypair with
            public key  - 1 568 B,
            private key - 3 168 B.
        """
        self.__RunKeyGen(gen_kyber1024, "Kyber", name)

    def generate_keypair_ntruhps2048509(self, name=""):
        """
        Generation of NTRU-HPS keypair with
            public key  - 699 B,
            private key - 935 B.
        """
        self.__RunKeyGen(gen_ntruhps2048509, "Nthrups", name)

    # DSA keypair generation
    def generate_keypair_dilithium4(self, name=""):
        """
        Generation of Crustals-Dilithium keypair with
            public key  - 1 760 B,
            private key - 3 856 B.
        """
        self.__RunKeyGen(gen_dilithium4, "Dilithium", name)

    def generate_keypair_rainbowVc_classic(self, name=""):
        """
        Generation of Rainbow Vc Classic keypair with
            public key  - 1 705 536 B,
            private key - 1 227 104 B.
        """
        self.__RunKeyGen(gen_rainbowVc_classic, "RainbowVc", name)

    def generate_keypair_sphincs_shake256_256s_simple(self, name=""):
        """
        Generation of SPHINCS keypair with
            public key  - 64 B,
            private key - 128 B.
        """
        self.__RunKeyGen(gen_sphincs_shake256_256s_simple, "Sphincs", name)

# # TEST AREA
# # init classes
# import os
# from statisticsModule import StatisticsManager
# from passwordsModule import PasswordManager
# pm = PasswordManager("masterPassword")
# p = PqKeyGenManager(pm, StatisticsManager())

# # Clear secrets
# with open(os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database/secrets", 'w') as file:
#     file.write("")

# # generate 4 keypairs
# p.generate_keypair_mceliece8192128("myName1")
# p.generate_keypair_kyber1024("testName1")
# p.generate_keypair_rainbowVc_classic("testName2")
# p.generate_keypair_sphincs_shake256_256s_simple()

# # print keyStoreList
# list = pm.loadKeyStoreList()
# print(list)
# print("Number of keys in DB: ", len(list)) # should print 8 (2 keys per generation)