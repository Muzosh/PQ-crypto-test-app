from datetime import datetime

class StatisticsManager:
    """This class handles everything around statistics, data mining, collecting data, etc...
    Available public methods:
        addKeyGenEntry(datetime:datetime, alg:str, timeInSeconds:float) -> None
        addKemAesEntry(datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float) -> None
        addDsaEntry(datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float) -> None
    """
    
    def __init__(self):
        self.__keyGenEntries = [(datetime.today(), 'McEliece', float(40)),(datetime.today(), 'aaa', float(10)),(datetime.today(), 'McEliece', float(20))]
        self.__kemAesEntries = []
        self.__dsaEntries = []
    
    def addKeyGenEntry(self, datetime:datetime, alg:str, timeInSeconds:float):
        self.keyGenEntries.append((datetime, alg, timeInSeconds))
        
    def addKemAesEntry(self, datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float):
        self.kemAesEntries.append((datetime, alg, operationType, aesBlockSize, fileSize, kemTimeInSeconds, aesTimeInSeconds))
        
    def addDsaEntry(self, datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float):
        self.__dsaEntries.append((datetime, alg, operationType, fileSize, timeInSeconds)) #timeInSeconds/fileSize
    
    def average_handler(self, list):
        sum = 0
        for tup in list:
            sum = sum + tup[2]
        if len(list) == 0:
            return None
        else:
            return sum/len(list)
        
    def min_handler(self, list):
        min = float('inf')
        for tup in list:
            if tup[2] < min:
                min = tup[2]        
        return min
    
    def max_handler(self, list):
        max = float('-inf')
        for tup in list:
            if tup[2] > max:
                max = tup[2]        
        return max
    
    def median_handler(self, list:list):
        list.sort(key=lambda tup:tup[2])
        if (list == None or list == []):
            return None
        x = len(list)
        if (x % 2 == 0):
            median1 = list[x//2]
            median2 = list[x//2 - 1]
            median = (median1[2] + median2[2])/2
            return median
        else:
            median = list[x//2]
            return median[2]
        
    def filterKeyList_handler(self):
        mceliece_avg = [tup for tup in self.__keyGenEntries if (tup[1] == 'McEliece')]
        #mceliece_avg = [tup[2] for tup in self.__keyGenEntries if (tup[1] == 'McEliece')]
        saber_avg = [tup for tup in self.__keyGenEntries if (tup[1] == 'Saber')]
        kyber_avg = [tup for tup in self.__keyGenEntries if (tup[1] == 'Kyber')]
        nthrups_avg = [tup for tup in self.__keyGenEntries if (tup[1] == 'Nthrups')]
        dilithium_avg = [tup for tup in self.__keyGenEntries if (tup[1] == 'Dilithium')]
        rainbow_avg = [tup for tup in self.__keyGenEntries if (tup[1] == 'RainbowVc')]
        sphincs_avg = [tup for tup in self.__keyGenEntries if (tup[1] == 'Sphincs')]
        
        return mceliece_avg, saber_avg, kyber_avg, nthrups_avg, dilithium_avg, rainbow_avg, sphincs_avg
       
    def getKeyAverages(self):
        key_filtered_list = self.filterKeyList_handler()        
        return [self.average_handler(key_filtered_list[0]), self.average_handler(key_filtered_list[1]), self.average_handler(key_filtered_list[2]), self.average_handler(key_filtered_list[3]), self.average_handler(key_filtered_list[4]), self.average_handler(key_filtered_list[5]), self.average_handler(key_filtered_list[6])]

    def getKeyMins(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.min_handler(key_filtered_list[0]), self.min_handler(key_filtered_list[1]), self.min_handler(key_filtered_list[2]), self.min_handler(key_filtered_list[3]), self.min_handler(key_filtered_list[4]), self.min_handler(key_filtered_list[5]), self.min_handler(key_filtered_list[6])]
    
    def getKeyMaxs(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.max_handler(key_filtered_list[0]), self.max_handler(key_filtered_list[1]), self.max_handler(key_filtered_list[2]), self.max_handler(key_filtered_list[3]), self.max_handler(key_filtered_list[4]), self.max_handler(key_filtered_list[5]), self.max_handler(key_filtered_list[6])]
    
    def getKeyMedians(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.median_handler(key_filtered_list[0]), self.median_handler(key_filtered_list[1]), self.median_handler(key_filtered_list[2]), self.median_handler(key_filtered_list[3]), self.median_handler(key_filtered_list[4]), self.median_handler(key_filtered_list[5]), self.median_handler(key_filtered_list[6])]
       
    
    
# TEST AREA        
s = StatisticsManager()
#s.average_handler([("a", "a", float(10)), ("a", "a", float(15))])
#print(s.getKeyAverages())

s.filterKeyList_handler()
#print(s.getKeyMins())

print(s.getKeyMedians())
        
        