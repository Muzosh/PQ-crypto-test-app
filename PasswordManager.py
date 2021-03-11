import os
import base64


class PasswordManager:

    __secretsFileName = "secrets"

    def __init__(self, newPassword):
        # Create or check secrets file
        if not os.path.exists(self.__secretsFileName):
            open(self.__secretsFileName, 'w').close()

        self.__writeSecrets([newPassword])

    def __readSecrets(self):
        with open(self.__secretsFileName, 'r') as file:
            return base64.b85decode(file.readline().encode()).decode().split(";")

    def __writeSecrets(self, secretsList):
        with open(self.__secretsFileName, 'w') as file:
            file.write(base64.b85encode(";".join(secretsList).encode()).decode())

    def __aesEncrypt(self, password, key):
        return

    def authenticate(self, password):
        return password == self.__readSecrets()[0]

    def changeMasterPassword(self, old, new):
        secrets = self.__readSecrets()
        if secrets[0] != old:
            raise ValueError("Old password does not match!")
        else:
            self.__writeSecrets([new]+secrets[1:])

    def addPassword(self, password):
        self.__writeSecrets(self.__readSecrets()+[password])

    def deletePassword(self, password):
        secrets = self.__readSecrets()
        if password in secrets:
            secrets.remove(password)
            self.__writeSecrets(secrets)
    
    def loadPasswordList(self):
        return self.__readSecrets()[1:]
    


x = PasswordManager("test")
x._PasswordManager__writeSecrets(x._PasswordManager__readSecrets()+["heslo1", "heslo2", "heslo3", "heslo4", "heslo5"])
print(x._PasswordManager__readSecrets())
x.changeMasterPassword("test", "new")
x.addPassword("added")
x.deletePassword("heslo3")
print(x._PasswordManager__readSecrets())
