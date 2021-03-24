from secrets import compare_digest
# from pqcrypto.kem.firesaber import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem1344shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem640shake import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976aes import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.frodokem976shake import generate_keypair, encrypt, decrypt
from pqcrypto.kem.kyber1024 import encrypt_kyber1024, decrypt_kyber1024
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
from pqcrypto.kem.mceliece8192128 import encrypt_mceliece8192128, decrypt_mceliece8192128
# from pqcrypto.kem.mceliece8192128f import generate_keypair, encrypt, decrypt
from pqcrypto.kem.ntruhps2048509 import encrypt_ntruhps2048509, decrypt_ntruhps2048509
# from pqcrypto.kem.ntruhps2048677 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhps4096821 import generate_keypair, encrypt, decrypt
# from pqcrypto.kem.ntruhrss701 import generate_keypair, encrypt, decrypt
from pqcrypto.kem.saber import encrypt_saber, decrypt_saber
class PqEncryptionManager:
    
    @staticmethod
    def aesEncrypt(self, dataBytes, symmetricKey):        
        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the 2x hashed masterPassword = PBKDF2 (Password Based Key Derivation Function)
        private_key = hashlib.scrypt(
            symmetricKey, salt=salt, n=2**14, r=8, p=1, dklen=32)

        # GCM mode used for authenticated encryption --> authenticated tag
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(dataBytes)
        return {
            'cipher_text': base64.b64encode(cipher_text).decode('utf-8'),
            'salt': base64.b64encode(salt).decode('utf-8'),
            'nonce': base64.b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': base64.b64encode(tag).decode('utf-8')
        }
    
    @staticmethod
    def aesDecrypt(self, encryptedData, symmetricKey):
        # decode the dictionary entries from base64
        salt = base64.b64decode(encryptedData['salt'])
        cipher_text = base64.b64decode(encryptedData['cipher_text'])
        nonce = base64.b64decode(encryptedData['nonce'])
        tag = base64.b64decode(enc_encryptedDatadict['tag'])
        
        # generate the private key from the 2x hashed masterPassword and salt
        private_key = hashlib.scrypt(
            symmetricKey, salt=salt, n=2**14, r=8, p=1, dklen=32)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
        
        return decrypted
    
    #mceliece
    def encapsulation_mceliece8192128(public_key):
        ciphertext, secret_key = encrypt_mceliece8192128(public_key)
        #print("Plain text bytes\n" + str(secret_key) + "\n")
        return ciphertext, secret_key

    def decapsulation_mceliece8192128(ciphertext, private_key):
        secret_key_recovered = decrypt_mceliece8192128(private_key, ciphertext)
        return secret_key_recovered
    
    #saber
    def encapsulation_saber(public_key):
        ciphertext, secret_key = encrypt_saber(public_key)
        #print("Plain text bytes\n" + str(secret_key) + "\n")
        return ciphertext, secret_key

    def decapsulation_saber(ciphertext, private_key):
        secret_key_recovered = decrypt_saber(private_key, ciphertext)
        return secret_key_recovered
    
    #kyber
    def encapsulation_kyber1024(public_key):
        ciphertext, secret_key = encrypt_kyber1024(public_key)
        #print("Plain text bytes\n" + str(secret_key) + "\n")
        return ciphertext, secret_key
    
    def decapsulation_kyber1024(ciphertext, private_key):
        secret_key_recovered = decrypt_kyber1024(private_key, ciphertext)
        return secret_key_recovered

    #ntruhps
    def encapsulation_ntruhps2048509(public_key):
        ciphertext, secret_key = encrypt_ntruhps2048509(public_key)
        #print("Plain text bytes\n" + str(secret_key) + "\n")
        return ciphertext, secret_key
    
    def decapsulation_ntruhps2048509(ciphertext, private_key):
        secret_key_recovered = decrypt_ntruhps2048509(private_key, ciphertext)
        return secret_key_recovered
    
    

    