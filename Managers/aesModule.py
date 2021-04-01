import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def aesEncrypt(dataBytes, symmetricKey):        
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

# this method is defined out of the class because it is being used in multiple classes
def aesDecrypt(encryptedData, symmetricKey):
    # decode the dictionary entries from base64
    salt = base64.b64decode(encryptedData['salt'])
    cipher_text = base64.b64decode(encryptedData['cipher_text'])
    nonce = base64.b64decode(encryptedData['nonce'])
    tag = base64.b64decode(encryptedData['tag'])
    
    # generate the private key from the 2x hashed masterPassword and salt
    private_key = hashlib.scrypt(
        symmetricKey, salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)
    
    return decrypted