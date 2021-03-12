import os
import json
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

class PasswordManager:

    # file of secrets/keys
    __secretsFileName = "secrets" 
    # file for masterPassword
    __keyChainFileName = "keychain"

    def __init__(self, masterPassword):
        '''
        Constructor
        Secrets file is created, if it is not.
        Calling method for creating hash of masterPassword.
        '''
        # Create or check secrets file
        if not os.path.exists(self.__secretsFileName):
            open(self.__secretsFileName, 'w').close()
            
        self.__writeKeyChain(masterPassword)
        
    def __readKeyChainBytes(self):
        ''' 
        Read masterPassword from the the file. 
        '''
        with open(self.__keyChainFileName, 'rb') as file:
            return file.read()

    def __writeKeyChain(self, masterPassword):
        '''
        Write hash of masterPassword to the file.
        ''' 
        hash = hashlib.sha512()
        hash.update(masterPassword.encode())
        with open(self.__keyChainFileName, 'wb') as file:
            file.write(hash.digest())

    def __readSecrets(self):
        '''
        Read secrets/uploaded keys from the file.
        '''
        with open(self.__secretsFileName, 'r') as file:
            encrypteList = base64.b85decode(file.readline().encode()).decode()
            secrets = json.loads(str(encrypteList).replace("'", "\""))
            
            # list of secrets
            decryptedList = []
            for x in secrets:
                decryptedList.append(self.__aesDecrypt(x).decode())
                
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

        # use the Scrypt KDF to get a private key from the masterPassword = PBKDF2 (Password Based Key Derivation Function)
        private_key = hashlib.scrypt(
            self.__readKeyChainBytes(), salt=salt, n=2**14, r=8, p=1, dklen=32) # aka je dlzka klucu pre sifrovanie AES??

        # create cipher config
        # GCM mode used for authenticated encryption --> authenticated tag
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
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
        

        # generate the private key from the masterPassword and salt
        private_key = hashlib.scrypt(
            self.__readKeyChainBytes(), salt=salt, n=2**14, r=8, p=1, dklen=32)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        return decrypted

    def authenticate(self, password):
        '''
        Auhthentication - hash checking.
        '''
        hash = hashlib.sha512()
        hash.update(password.encode())
        return hash.digest() == self.__readKeyChainBytes()

    def changeMasterPassword(self, old, new):
        '''
        Change masterPassword of the application.
        '''
        if not self.authenticate(old):
            raise ValueError("Old password does not match!")
        else:
            # save currenty used secrets to variable
            secrets = self.__readSecrets()
            # write new masterPassword to file
            self.__writeKeyChain(new)
            # re-encrypt secrets/keys using new passphrase = new masterPassword
            self.__writeSecrets(secrets)

    def addPassword(self, password): # premenovat na addSecret
        '''
        A new secret/key is added to the file.
        '''
        self.__writeSecrets(self.__readSecrets()+[password])

    def deletePassword(self, password): # premenovat na deleteSecret
        '''
        Remove secret/key from the file.
        '''
        secrets = self.__readSecrets()
        if password in secrets:
            secrets.remove(password)
            self.__writeSecrets(secrets)
    
    def loadPasswordList(self): # je potrebna ?? ci ma znazornovat akoze public metodu
        return self.__readSecrets()

# TEST AREA
# Initialize with "masterPassword" as masterPassword
x = PasswordManager("masterPassword")
# Add user defined passwords (strings for now)
x._PasswordManager__writeSecrets(["heslo1", "heslo2", "heslo3", "heslo4", "heslo5"])
# print first list
print("after init: ", x.loadPasswordList())
# change master password
x.changeMasterPassword("masterPassword", "newPassword")
# add "added" password
x.addPassword("added")
# delete thrird password
x.deletePassword("heslo3")
# final print
print("final print: ", x.loadPasswordList())

# Program should generate two "keychain" and "secrets" obfuscated files
