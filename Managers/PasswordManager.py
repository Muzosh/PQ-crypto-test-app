import os
import json
import base64
import hashlib
from PqEncryptionManager import aesEncrypt, aesDecrypt

class PasswordManager:
    """
    This class handles everything around user authentication, user-defined password storing, changing, adding, deleting keyPairs, etc...
        Constructor takes masterPassword:str
    
    Available public methods:
        changeMasterPassword(old:str, new:str):None
        addKeyPair(publicKey:bytes, secretKey:bytes):None
        deleteKeyPair(ublicKey:bytes, secretKey:bytes):None
        loadKeyPairList():[tuple(bytes, bytes)]
    """
    # file for keyPairs
    __keyPairsFileName = os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database/secrets" 
    # file for masterPassword
    __keyChainFileName = os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database/keychain"
    
    # masterPassword in plaintext
    __masterPassword = b""

    def __init__(self, masterPassword):
        # Create or check keyPairs file
        if not os.path.exists(self.__keyPairsFileName):
            open(self.__keyPairsFileName, 'w').close()
            
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

    def __readKeyPairs(self):
        '''
        Read keyPairs from the file.
        '''
        with open(self.__keyPairsFileName, 'r') as file:
            encryptedList = base64.b85decode(file.readline().encode()).decode()
            keyPairs = json.loads(str(encryptedList).replace("'", "\""))
            
            # list of keyPairs
            decryptedList = []
            for x in keyPairs:
                decryptedList.append(tuple(aesDecrypt(x, self.__masterPassword).split(b"\0\0\0")))
                
            return decryptedList

    def __writeKeyPairs(self, keyPairsList):
        '''
        Write encrypted keyPairs keys to the file.
        '''
        encryptedList = []
        for x in keyPairsList:
            encryptedList.append(aesEncrypt(x[0] + b"\0\0\0" + x[1], self.__masterPassword))
            
        with open(self.__keyPairsFileName, 'w') as file:
            file.write(base64.b85encode(str(encryptedList).encode()).decode())

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
            # save currenty used keyPairs to variable
            keyPairs = self.__readKeyPairs()
            
            # write new masterPassword to file
            self.__writeKeyChain(new)
            
            # write new 2x hashedmasterPassword to memory
            hash = hashlib.sha512()
            hash.update(new.encode())
            hash.update(new.encode())
            self.__masterPassword = hash.digest()
            
            # re-encrypt keyPairs using new passphrase = new masterPassword
            self.__writeKeyPairs(keyPairs)

    def addKeyPair(self, publicKey, secretKey):
        '''
        A new keyPair is added to the file.
        '''
        self.__writeKeyPairs(self.__readKeyPairs()+[(publicKey, secretKey)])

    def deleteKeyPair(self, publicKey, secretKey):
        '''
        Remove keyPair from the file.
        '''
        
        keyPair = (publicKey, secretKey)
        
        keyPairs = self.__readKeyPairs()
        if keyPair in keyPairs:
            keyPairs.remove(keyPair)
            self.__writeKeyPairs(keyPairs)
    
    # Public method for creating list of user-stored passwords
    def loadKeyPairList(self):
        return self.__readKeyPairs()

# TEST AREA
# Initialize with "masterPassword" as masterPassword
x = PasswordManager("masterPassword")
# Add user defined passwords (strings for now)
x._PasswordManager__writeKeyPairs([[b"publicKey1", b"secretKey1"],[b"publicKey2", b"secretKey2"],[b"publicKey3", b"secretKey3"],[b"publicKey4", b"secretKey4"]])
# print first list
print("after init: ", x.loadKeyPairList())
# change master password
x.changeMasterPassword("masterPassword", "newPassword")
# add "added" password
x.addKeyPair(b"addedPublicKey", b"addedSecretKey")
# delete third password
x.deleteKeyPair(b"publicKey3", b"secretKey3")
# final print
print("final print: ", x.loadKeyPairList())
# change master password
x.changeMasterPassword("newPassword", "masterPassword")

# Program should generate two "keychain" and "secrets" obfuscated files
