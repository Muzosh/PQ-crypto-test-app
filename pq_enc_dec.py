from secrets import compare_digest
# from pqcrypto.kem.firesaber import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.kyber1024 import generate_keypair, encrypt, decrypt
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
from pqcrypto.kem.mceliece8192128 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.mceliece8192128f import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhps2048509 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhps2048677 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhps4096821 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhrss701 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.saber import generate_keypair, encrypt, decrypt



def encryption(plaintext, public_key):
    plaintext_bytes = plaintext.encode('utf-8')
    #print(plaintext_bytes)
    #plaintext_s = plaintext_bytes.decode()
    #print(plaintext_s)
    ciphertext, plaintext_bytes = encrypt(public_key)
    #print(plaintext_bytes)
    #plaintext_string = plaintext_bytes.decode(errors='replace')
    print("Plain text bytes\n" + str(plaintext_bytes) + "\n")
    
    return ciphertext

def decryption(ciphertext, secret_key):
    plaintext_recovered = decrypt(secret_key, ciphertext)
    return plaintext_recovered

public_key, secret_key = generate_keypair()
plain_orig="Ahoj, ako sa mas"
print("Plain\n" + str(plain_orig) + "\n")

cipher = encryption(plain_orig, public_key)
print("Cipher\n" + str(cipher) + "\n")

plain = decryption(cipher, secret_key)
print("Plain recover bytes\n" + str(plain) + "\n")