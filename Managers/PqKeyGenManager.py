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

from collections.abc import Callable
from PasswordManager import PasswordManager
from StatisticsManager import StatisticsManager
from datetime import datetime
import time, random

class PqKeyGenManager: 
    """
    This class generates key pairs using PQ algorithms and saves them into the database. It is recommended to reload keyStores list after generating keyPair.
        Constructor takes passwordManager:PasswordManager and statisticsManager:StatisticsManager
    
    Available public methods:
        generate_keypair_mceliece8192128(name=""):None
        generate_keypair_saber(name=""):None
        generate_keypair_kyber1024(name=""):None
        generate_keypair_ntruhps2048509(name=""):None
        generate_keypair_dilithium4(name=""):None
        generate_keypair_rainbowVc_classic(name=""):None
        generate_keypair_sphincs_shake256_256s_simple(name=""):None
    """
       
    def __init__(self, passwordManager:PasswordManager, statisticsManager:StatisticsManager):
        self.__passwordManager = passwordManager
        self.__statisticsManager = statisticsManager

    def __RunKeyGen(self, function:Callable[[], [bytes]], alg:str, name:str):
        now = datetime.now()
        nameText = "|"+ random.randint(0,999) + "|" + str(now) + "|" + name
        
        start = time.time()
        keyPair = function()
        keyGenTime = time.time() - start
        
        self.__statisticsManager.addKeyGenEntry(now, alg, keyGenTime)
        self.__passwordManager.addKeyStore(nameText, alg, "Public", keyPair[0])
        self.__passwordManager.addKeyStore(nameText, alg, "Private", keyPair[1])

    # KEM
    def generate_keypair_mceliece8192128(self, name=""):
        self.__RunKeyGen(gen_mceliece, "McLiece", name)

    def generate_keypair_saber(self, name=""):
        self.__RunKeyGen(gen_saber, "Saber", name)

    def generate_keypair_kyber1024(self, name=""):
        self.__RunKeyGen(gen_kyber1024, "Kyber", name)

    def generate_keypair_ntruhps2048509(self, name=""):
        self.__RunKeyGen(gen_ntruhps2048509, "Nthrups", name)

    # DSA
    def generate_keypair_dilithium4(self, name=""):
        self.__RunKeyGen(gen_dilithium4, "Dilithium", name)

    def generate_keypair_rainbowVc_classic(self, name=""):
        self.__RunKeyGen(gen_rainbowVc_classic, "RainbowVc", name)

    def generate_keypair_sphincs_shake256_256s_simple(self, name=""):
        self.__RunKeyGen(gen_sphincs_shake256_256s_simple, "Sphincs", name)

# TEST AREA
pm = PasswordManager("masterPassword")
p = PqKeyGenManager(pm, StatisticsManager())

print("____________________________________________")
p.generate_keypair_mceliece8192128("myName1")
p.generate_keypair_kyber1024("testName1")
p.generate_keypair_rainbowVc_classic("testName2")
p.generate_keypair_sphincs_shake256_256s_simple()

print(pm.loadKeyStoreList())