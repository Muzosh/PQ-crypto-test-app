import os
import json
import base64
import hashlib

from aesModule import aesEncrypt, aesDecrypt

class PasswordManager:
    """
    This class handles everything around user authentication, user-defined password storing, changing, adding, deleting keyStores, etc...
        Constructor takes masterPassword:str
    
    Available public methods:
        changeMasterPassword(old:str, new:str):None
        addKeyStore(name:string, alg:string, type:string, value:bytes):None
        deleteKeyStore(name:string, alg:string, type:string, value:bytes):None
        loadKeyStoreList():[tuple(name:string, alg:string, type:string, value:bytes)]
    """
    
    # database folder
    __databaseFolder = os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database"
    
    # file for keyStores
    __keyStoresFileName = __databaseFolder + "/secrets" 
    # file for masterPassword
    __keyChainFileName = __databaseFolder + "/keychain"
    
    # masterPassword in plaintext
    __masterPassword = b""

    def __init__(self, masterPassword:str):
        # Create or check database folder
        if not os.path.exists(self.__databaseFolder):
            os.mkdir(self.__databaseFolder)
        
        # Create or check keyStores file
        if not os.path.exists(self.__keyStoresFileName):
            open(self.__keyStoresFileName, 'w').close()
            
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
        
        # Write result from hash function into keychain file
        with open(self.__keyChainFileName, 'wb') as file:
            file.write(hash.digest())

    def __readKeyStores(self):
        '''
        Read keyStores from the file.
        '''
        with open(self.__keyStoresFileName, 'r') as file:
            # read file contents as string and convert that string into list type using json.loads()
            encryptedList = base64.b64decode(file.readline().encode()).decode()
            keyStores = json.loads(str(encryptedList).replace("'", "\"") or "[]")

            # create list of keyStores - decrypt with aes and create (string, string, string bytes) tuple and add it to the list
            decryptedList = []
            for x in keyStores:
                decryptedStore = aesDecrypt(x, self.__masterPassword).split(b"\x00"*4, 3)
                
                decryptedList.append(
                    (decryptedStore[0].decode(), decryptedStore[1].decode(), decryptedStore[2].decode(), decryptedStore[3]))
                
            return decryptedList

    def __writeKeyStores(self, keyStoresList):
        '''
        Write encrypted keyStores keys to the file.
        '''
        encryptedList = []
        
        # for each tuple create bytes object by encoding strings and concatenating them together with separator
        # encrypt the result and add it to the list
        for x in keyStoresList:
            encryptedList.append(
                aesEncrypt(
                    x[0].encode() + b"\x00"*4 + x[1].encode() + b"\x00"*4 + x[2].encode() + b"\x00"*4 + x[3],
                    self.__masterPassword))
            
        with open(self.__keyStoresFileName, 'w') as file:
            file.write(base64.b64encode(str(encryptedList).encode()).decode())

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

    def changeMasterPassword(self, old:str, new:str):
        '''
        Change masterPassword of the application.
        '''
        if not self.__authenticate(old):
            raise ValueError("Old password does not match!")
        else:
            # save currenty used keyStores to variable
            keyStores = self.__readKeyStores()
            
            # write new masterPassword to file
            self.__writeKeyChain(new)
            
            # write new 2x hashedmasterPassword to memory
            hash = hashlib.sha512()
            hash.update(new.encode())
            hash.update(new.encode())
            self.__masterPassword = hash.digest()
            
            # re-encrypt keyStores using new passphrase = new masterPassword
            self.__writeKeyStores(keyStores)

    def addKeyStore(self, name:str, alg:str, type:str, value:bytes):
        '''
        A new keyStore is added to the file.
        '''
        with open(self.__keyStoresFileName, 'r') as file:
            # read file contents as string
            encryptedListString = base64.b64decode(file.readline().encode()).decode()
        
        encryptedKeyStoreString = str(aesEncrypt(
            name.encode() + b"\x00"*4 + alg.encode() + b"\x00"*4 + type.encode() + b"\x00"*4 + value,
            self.__masterPassword))
           
        if not encryptedListString:
            encryptedListString = "[" + encryptedKeyStoreString + "]"
        else:
            encryptedListString = encryptedListString[:-1] + ", " + encryptedKeyStoreString + "]"
        
        with open(self.__keyStoresFileName, 'w') as file:
            file.write(base64.b64encode(encryptedListString.encode()).decode())

    def deleteKeyStore(self, name:str, alg:str, type:str, value:bytes):
        '''
        Remove keyStore from the file.
        '''
        
        keyStore = (name, alg, type, value)
        
        keyStores = self.__readKeyStores()
        self.__writeKeyStores([x for x in keyStores if x not in {keyStore}])
    
    # Public method for creating list of user-stored passwords
    def loadKeyStoreList(self):
        return self.__readKeyStores()


# # TEST AREA
# # Initialize with "masterPassword" as masterPassword
# x = PasswordManager("masterPassword")
# # Add user defined passwords (strings for now)
# x._PasswordManager__writeKeyStores([["name1", "alg1", "type1", b"value1"],["name2", "alg2", "type2", b"value2"],["name3", "alg3", "type3", b"value3"],["name4", "alg4", "type4", b"value4"]])
# # print first list
# print("after init: ", x.loadKeyStoreList())
# # change master password
# #x.changeMasterPassword("masterPassword", "newPassword")
# # add "added" password
# x.addKeyStore("nameX", "algX", "typeX", b"valueX")
# # delete third password
# x.deleteKeyStore("name3", "alg3", "type3", b"value3")
# # final print
# print("final print: ", x.loadKeyStoreList())
# # change master password
# #x.changeMasterPassword("newPassword", "masterPassword")
# # Program should generate two "keychain" and "secrets" obfuscated files