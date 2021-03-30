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


class PqKeyGenManager:
    
    # KEM
    def generate_keypair_mceliece8192128(self):
        return gen_mceliece()
    
    def generate_keypair_saber(self):
        return gen_saber()
    
    def generate_keypair_kyber1024(self):
        return gen_kyber1024()
    
    def generate_keypair_ntruhps2048509(self):
        return gen_ntruhps2048509()
    
    # DSA
    def generate_keypair_dilithium4(self):
        return gen_dilithium4()
    
    def generate_keypair_rainbowVc_classic(self):
            return gen_rainbowVc_classic()
        
    def generate_keypair_sphincs_shake256_256s_simple(self):
        return gen_sphincs_shake256_256s_simple()
    
    
