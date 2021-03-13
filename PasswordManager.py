import os
import json
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

class PasswordManager:
    """
    This class handles everything around user authentication, user-defined password storing, changing, adding, deleting secrets, etc...
        Constructor takes masterPassword:str
    
    Available public methods:
        changeMasterPassword(old:str, new:str):None
        addSecret(user-defined-password:bytes):None
        deleteSecret(user-defined-password:bytes):None
        loadSecretList():[bytes]
    """
        
    # file of secrets/keys
    __secretsFileName = "secrets" 
    # file for masterPassword
    __keyChainFileName = "keychain"
    
    # masterPassword in plaintext
    __masterPassword = b""

    def __init__(self, masterPassword):
        # Create or check secrets file
        if not os.path.exists(self.__secretsFileName):
            open(self.__secretsFileName, 'w').close()
            
        # Create or check keyChain file
        if not os.path.exists(self.__keyChainFileName):
            open(self.__keyChainFileName, 'w').close()
            self.__writeKeyChain(masterPassword)
            
        # Authenticate - this will write 2x hashed password into memory
        if not self.__authenticate(masterPassword):
            raise ValueError("Passwords don't match!")

    def __writeKeyChain(self, masterPassword):
        '''
        Write hash of masterPassword to the file.
        ''' 
        # Using triple hashing to hide passoword into file
        hash = hashlib.sha512()
        hash.update(masterPassword.encode())
        hash.update(masterPassword.encode())
        hash.update(masterPassword.encode())
        with open(self.__keyChainFileName, 'wb') as file:
            file.write(hash.digest())

    def __readSecrets(self):
        '''
        Read secrets/uploaded keys from the file.
        '''
        with open(self.__secretsFileName, 'r') as file:
            encryptedList = base64.b85decode(file.readline().encode()).decode()
            secrets = json.loads(str(encryptedList).replace("'", "\""))
            
            # list of secrets
            decryptedList = []
            for x in secrets:
                decryptedList.append(self.__aesDecrypt(x))
                
            return decryptedList

    def __writeSecrets(self, secretsList):
        '''
        Write encrypted secrets/uploaded keys to the file.
        '''
        encryptedList = []
        for x in secretsList:
            encryptedList.append(self.__aesEncrypt(x))
            
        with open(self.__secretsFileName, 'w') as file:
            file.write(base64.b85encode(str(encryptedList).encode()).decode())

    def __aesEncrypt(self, plain_text):
        '''
        Encrypt secret/key bytes using AES.
        '''
        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the 2x hashed masterPassword = PBKDF2 (Password Based Key Derivation Function)
        private_key = hashlib.scrypt(
            self.__masterPassword, salt=salt, n=2**14, r=8, p=1, dklen=32) # aka je dlzka klucu pre sifrovanie AES??

        # create cipher config
        # GCM mode used for authenticated encryption --> authenticated tag
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(plain_text)
        return {
            'cipher_text': base64.b64encode(cipher_text).decode('utf-8'),
            'salt': base64.b64encode(salt).decode('utf-8'),
            'nonce': base64.b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': base64.b64encode(tag).decode('utf-8')
        }
    
    def __aesDecrypt(self, enc_dict):
        '''
        Decrypt secret/key bytes.
        '''
        # decode the dictionary entries from base64
        salt = base64.b64decode(enc_dict['salt'])
        cipher_text = base64.b64decode(enc_dict['cipher_text'])
        nonce = base64.b64decode(enc_dict['nonce'])
        tag = base64.b64decode(enc_dict['tag'])
        
        # generate the private key from the 2x hashed masterPassword and salt
        private_key = hashlib.scrypt(
            self.__masterPassword, salt=salt, n=2**14, r=8, p=1, dklen=32)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        return decrypted

    def __authenticate(self, password):
        '''
        Auhthentication - hash checking.
        '''
        # 3x hash password to compare it with 3x hashed masterPassword from file
        hash = hashlib.sha512()
        hash.update(password.encode())
        hash.update(password.encode())
        hash.update(password.encode())
        digest = hash.digest()
        
        with open(self.__keyChainFileName, 'rb') as file:
            keyChainBytes = file.read()
        
        if digest == keyChainBytes:
            # Authentication successful, write 2x hashed password into memory
            hash = hashlib.sha512()
            hash.update(password.encode())
            hash.update(password.encode())
            self.__masterPassword = hash.digest()
            return True
        else:
            return False

    def changeMasterPassword(self, old, new):
        '''
        Change masterPassword of the application.
        '''
        if not self.__authenticate(old):
            raise ValueError("Old password does not match!")
        else:
            # save currenty used secrets to variable
            secrets = self.__readSecrets()
            
            # write new masterPassword to file
            self.__writeKeyChain(new)
            
            # write new 2x hashedmasterPassword to memory
            hash = hashlib.sha512()
            hash.update(new.encode())
            hash.update(new.encode())
            self.__masterPassword = hash.digest()
            
            # re-encrypt secrets/keys using new passphrase = new masterPassword
            self.__writeSecrets(secrets)

    def addSecret(self, password):
        '''
        A new secret/key is added to the file.
        '''
        self.__writeSecrets(self.__readSecrets()+[password])

    def deleteSecret(self, password):
        '''
        Remove secret/key from the file.
        '''
        secrets = self.__readSecrets()
        if password in secrets:
            secrets.remove(password)
            self.__writeSecrets(secrets)
    
    # Public method for creating list of user-stored passwords
    def loadSecretList(self):
        return self.__readSecrets()

# TEST AREA
# Initialize with "masterPassword" as masterPassword
x = PasswordManager("masterPassword")
# Add user defined passwords (strings for now)
x._PasswordManager__writeSecrets([b"heslo1", b"heslo2", b"heslo3toBeDeleted", b"heslo4", b"heslo5"])
# print first list
print("after init: ", x.loadSecretList())
# change master password
x.changeMasterPassword("masterPassword", "newPassword")
# add "added" password
x.addSecret(b"added")
# delete thrird password
x.deleteSecret(b"heslo3toBeDeleted")
# final print
print("final print: ", x.loadSecretList())
# change master password
x.changeMasterPassword("newPassword", "masterPassword")

# Program should generate two "keychain" and "secrets" obfuscated files
