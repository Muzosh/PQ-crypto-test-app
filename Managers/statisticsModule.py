from datetime import datetime
import statistics

class StatisticsManager:
    """This class handles everything around statistics, data mining, collecting data, etc...
    Available public methods:
        addKeyGenEntry(datetime:datetime, alg:str, timeInSeconds:float) -> None
        addKemAesEntry(datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float) -> None
        addDsaEntry(datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float) -> None
    """
    
    def __init__(self, passwordManager):
        self.keyGenEntries = []
        self.kemAesEntries = []
        self.dsaEntries = []
        self.passwordManager = passwordManager
    
    def addKeyGenEntry(self, datetime:datetime, alg:str, timeInSeconds:float):
        self.keyGenEntries.append((datetime, alg, timeInSeconds))
        
    def addKemAesEntry(self, datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float):
        self.kemAesEntries.append((datetime, alg, operationType, aesBlockSize, fileSize, kemTimeInSeconds, aesTimeInSeconds))
        
    def addDsaEntry(self, datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float):
        self.__dsaEntries.append((datetime, alg, operationType, fileSize, timeInSeconds))
    
    def saveStatisticsToFile(self):
        self.passwordManager.writeStatistics(self.keyGenEntries, self.kemAesEntries, self.dsaEntries)

    def loadStatisticsFromFile(self):
        self.keyGenEntries, self.kemAesEntries, self.dsaEntries = self.passwordManager.readStatistics()

    def average_handler(self, list):
        if len(list) == 0:
            return "N/A"
        else:
            return sum(list)/len(list)
        
    def min_handler(self, list):
        if len(list) == 0:
            return "N/A"
        else:
            return min(list)
    
    def max_handler(self, list):
        if len(list) == 0:
            return "N/A"
        else:
            return max(list)
    
    def median_handler(self, list):
        if len(list) == 0:
            return "N/A"
        else:
            return statistics.median(list)
        
    def filterKeyList_handler(self):
        mceliece = [tup[2] for tup in self.keyGenEntries if (tup[1] == 'McEliece')]
        saber = [tup[2] for tup in self.keyGenEntries if (tup[1] == 'Saber')]
        kyber = [tup[2] for tup in self.keyGenEntries if (tup[1] == 'Kyber')]
        nthrups = [tup[2] for tup in self.keyGenEntries if (tup[1] == 'Nthrups')]
        dilithium = [tup[2] for tup in self.keyGenEntries if (tup[1] == 'Dilithium')]
        rainbow = [tup[2] for tup in self.keyGenEntries if (tup[1] == 'RainbowVc')]
        sphincs = [tup[2] for tup in self.keyGenEntries if (tup[1] == 'Sphincs')]
        return mceliece, kyber, saber, nthrups, dilithium, rainbow, sphincs

    def filterEncryptList_handler(self):
        mceliece = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'McEliece' and tup[2] == 'Encrypt')]
        saber = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'Saber' and tup[2] == 'Encrypt')]
        kyber = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'Kyber' and tup[2] == 'Encrypt')]
        nthrups = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'Nthrups' and tup[2] == 'Encrypt')]
        return mceliece, kyber, saber, nthrups

    def filterDecryptList_handler(self):
        mceliece = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'McEliece' and tup[2] == 'Decrypt')]
        saber = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'Saber' and tup[2] == 'Decrypt')]
        kyber = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'Kyber' and tup[2] == 'Decrypt')]
        nthrups = [tup[5]+tup[6]/tup[4] for tup in self.kemAesEntries if (tup[1] == 'Nthrups' and tup[2] == 'Decrypt')]
        return mceliece, kyber, saber, nthrups

    def filterSignList_handler(self):
        dilithium = [tup[4]/tup[3] for tup in self.dsaEntries if (tup[1] == 'Dilithium' and tup[2] == 'Sign')]
        rainbow = [tup[2]/tup[3] for tup in self.dsaEntries if (tup[1] == 'RainbowVc' and tup[2] == 'Sign')]
        sphincs = [tup[2]/tup[3] for tup in self.dsaEntries if (tup[1] == 'Sphincs' and tup[2] == 'Sign')]
        return dilithium, rainbow, sphincs

    def filterVerifyList_handler(self):
        dilithium = [tup[4]/tup[3] for tup in self.dsaEntries if (tup[1] == 'Dilithium' and tup[2] == 'Verify')]
        rainbow = [tup[2]/tup[3] for tup in self.dsaEntries if (tup[1] == 'RainbowVc' and tup[2] == 'Verify')]
        sphincs = [tup[2]/tup[3] for tup in self.dsaEntries if (tup[1] == 'Sphincs' and tup[2] == 'Verify')]
        return dilithium, rainbow, sphincs    

    def getKeyAverages(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.average_handler(key_filtered_list[i]) for i in range(len(key_filtered_list))]

    def getKeyMins(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.min_handler(key_filtered_list[i]) for i in range(len(key_filtered_list))]

    def getKeyMaxes(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.max_handler(key_filtered_list[i]) for i in range(len(key_filtered_list))]

    def getKeyMedians(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.median_handler(key_filtered_list[i]) for i in range(len(key_filtered_list))]
       
    def getEncryptAverages(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [self.average_handler(encypt_filtered_list[i]) for i in range(len(encypt_filtered_list))]

    def getEncryptMins(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [self.min_handler(encypt_filtered_list[i]) for i in range(len(encypt_filtered_list))]

    def getEncryptMaxes(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [self.max_handler(encypt_filtered_list[i]) for i in range(len(encypt_filtered_list))]

    def getEncryptMedians(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [self.median_handler(encypt_filtered_list[i]) for i in range(len(encypt_filtered_list))]
       
    def getDecryptAverages(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [self.average_handler(decrypt_filtered_list[i]) for i in range(len(decrypt_filtered_list))]

    def getDecryptMins(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [self.min_handler(decrypt_filtered_list[i]) for i in range(len(decrypt_filtered_list))]

    def getDecryptMaxes(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [self.max_handler(decrypt_filtered_list[i]) for i in range(len(decrypt_filtered_list))]

    def getDecryptMedians(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [self.median_handler(decrypt_filtered_list[i]) for i in range(len(decrypt_filtered_list))]
       
    def getSignAverages(self):
        sign_filtered_list = self.filterSignList_handler()
        return [self.average_handler(sign_filtered_list[i]) for i in range(len(sign_filtered_list))]

    def getSignMins(self):
        sign_filtered_list = self.filterSignList_handler()
        return [self.min_handler(sign_filtered_list[i]) for i in range(len(sign_filtered_list))]

    def getSignMaxes(self):
        sign_filtered_list = self.filterSignList_handler()
        return [self.max_handler(sign_filtered_list[i]) for i in range(len(sign_filtered_list))]

    def getSignMedians(self):
        sign_filtered_list = self.filterSignList_handler()
        return [self.median_handler(sign_filtered_list[i]) for i in range(len(sign_filtered_list))]
       
    def getVerifyAverages(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [self.average_handler(verify_filtered_list[i]) for i in range(len(verify_filtered_list))]

    def getVerifyMins(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [self.min_handler(verify_filtered_list[i]) for i in range(len(verify_filtered_list))]

    def getVerifyMaxes(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [self.max_handler(verify_filtered_list[i]) for i in range(len(verify_filtered_list))]

    def getVerifyMedians(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [self.median_handler(verify_filtered_list[i]) for i in range(len(verify_filtered_list))]
    
# # TEST AREA        
# s = StatisticsManager()
# #s.average_handler([("a", "a", float(10)), ("a", "a", float(15))])
# #print(s.getKeyAverages())

# s.filterKeyList_handler()
# #print(s.getKeyMins())

# print(s.getKeyMedians())
        
        