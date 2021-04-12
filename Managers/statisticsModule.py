from datetime import datetime

class StatisticsManager:
    """This class handles everything around statistics, data mining, collecting data, etc...
    Available public methods:
        addKeyGenEntry(datetime:datetime, alg:str, timeInSeconds:float) -> None
        addKemAesEntry(datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float) -> None
        addDsaEntry(datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float) -> None
    """
    
    def __init__(self):
        self.__keyGenEntries = []
        self.__kemAesEntries = []
        self.__dsaEntries = []
        #for testing
        #self.__keyGenEntries = [(datetime.today(), 'McEliece', float(40)),(datetime.today(), 'aaa', float(10)),(datetime.today(), 'McEliece', float(20))]
        #self.__kemAesEntries = [(datetime.today(), 'McEliece', 'op', 256, 50, float(40), float(40)), (datetime.today(), 'aaa', 'op', 256, 50, float(40), float(40)), (datetime.today(), 'McEliece', 'op', 256, 50, float(20), float(20))]
        #self.__dsaEntries = [(datetime.today(), 'RainbowVc', 'op',50, float(40)), (datetime.today(), 'RainbowVc', 'op', 50, float(40)), (datetime.today(), 'Sphincs', 'op', 50, float(20))]
    
    def addKeyGenEntry(self, datetime:datetime, alg:str, timeInSeconds:float):
        self.keyGenEntries.append((datetime, alg, timeInSeconds))
        
    def addKemAesEntry(self, datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float):
        self.kemAesEntries.append((datetime, alg, operationType, aesBlockSize, fileSize, kemTimeInSeconds, aesTimeInSeconds))
        
    def addDsaEntry(self, datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float):
        self.__dsaEntries.append((datetime, alg, operationType, fileSize, timeInSeconds)) #timeInSeconds/fileSize
    
    def average_handler(self, list, position_of_indextime):
        sum = 0
        for tup in list:
            sum = sum + tup[position_of_indextime]
        if len(list) == 0:
            return None
        else:
            return sum/len(list)
        
    def min_handler(self, list, position_of_indextime):
        min = float('inf')
        for tup in list:
            if tup[position_of_indextime] < min:
                min = tup[position_of_indextime]        
        return min
    
    def max_handler(self, list, position_of_indextime):
        max = float('-inf')
        for tup in list:
            if tup[position_of_indextime] > max:
                max = tup[position_of_indextime]        
        return max
    
    def median_handler(self, list:list, position_of_indextime):
        list.sort(key=lambda tup:tup[position_of_indextime])
        if (list == None or list == []):
            return None
        x = len(list)
        if (x % 2 == 0):
            median1 = list[x//2]
            median2 = list[x//2 - 1]
            median = (median1[position_of_indextime] + median2[position_of_indextime])/2
            return median
        else:
            median = list[x//2]
            return median[position_of_indextime]
        
    def filterKeyList_handler(self):
        mceliece = [tup for tup in self.__keyGenEntries if (tup[1] == 'McEliece')]
        #mceliece = [tup[2] for tup in self.__keyGenEntries if (tup[1] == 'McEliece')]
        saber = [tup for tup in self.__keyGenEntries if (tup[1] == 'Saber')]
        kyber = [tup for tup in self.__keyGenEntries if (tup[1] == 'Kyber')]
        nthrups = [tup for tup in self.__keyGenEntries if (tup[1] == 'Nthrups')]
        dilithium = [tup for tup in self.__keyGenEntries if (tup[1] == 'Dilithium')]
        rainbow = [tup for tup in self.__keyGenEntries if (tup[1] == 'RainbowVc')]
        sphincs = [tup for tup in self.__keyGenEntries if (tup[1] == 'Sphincs')]
        
        return mceliece, saber, kyber, nthrups, dilithium, rainbow, sphincs
    
    def filterKemList_handler(self):
        mceliece = [tup for tup in self.__kemAesEntries if (tup[1] == 'McEliece')]
        #mceliece = [tup[2] for tup in self.__keyGenEntries if (tup[1] == 'McEliece')]
        saber = [tup for tup in self.__kemAesEntries if (tup[1] == 'Saber')]
        kyber = [tup for tup in self.__kemAesEntries if (tup[1] == 'Kyber')]
        nthrups = [tup for tup in self.__kemAesEntries if (tup[1] == 'Nthrups')]
        
        return mceliece, saber, kyber, nthrups
    
    def filterDsaList_handler(self):
        dilithium = [tup for tup in self.__dsaEntries if (tup[1] == 'Dilithium')]
        rainbow = [tup for tup in self.__dsaEntries if (tup[1] == 'RainbowVc')]
        sphincs = [tup for tup in self.__dsaEntries if (tup[1] == 'Sphincs')]
        
        return dilithium, rainbow, sphincs
    
    #KEY  
    def getKeyAverages(self):
        key_filtered_list = self.filterKeyList_handler()        
        return [self.average_handler(key_filtered_list[0],2), self.average_handler(key_filtered_list[1],2), self.average_handler(key_filtered_list[2],2), self.average_handler(key_filtered_list[3],2), self.average_handler(key_filtered_list[4],2), self.average_handler(key_filtered_list[5],2), self.average_handler(key_filtered_list[6],2)]

    def getKeyMins(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.min_handler(key_filtered_list[0],2), self.min_handler(key_filtered_list[1],2), self.min_handler(key_filtered_list[2],2), self.min_handler(key_filtered_list[3],2), self.min_handler(key_filtered_list[4],2), self.min_handler(key_filtered_list[5],2), self.min_handler(key_filtered_list[6],2)]
    
    def getKeyMaxs(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.max_handler(key_filtered_list[0],2), self.max_handler(key_filtered_list[1],2), self.max_handler(key_filtered_list[2],2), self.max_handler(key_filtered_list[3],2), self.max_handler(key_filtered_list[4],2), self.max_handler(key_filtered_list[5],2), self.max_handler(key_filtered_list[6],2)]
    
    def getKeyMedians(self):
        key_filtered_list = self.filterKeyList_handler()
        return [self.median_handler(key_filtered_list[0],2), self.median_handler(key_filtered_list[1],2), self.median_handler(key_filtered_list[2],2), self.median_handler(key_filtered_list[3],2), self.median_handler(key_filtered_list[4],2), self.median_handler(key_filtered_list[5],2), self.median_handler(key_filtered_list[6],2)]
    
    #KEM   
    def getKemAverages(self):
        kem_filtered_list = self.filterKemList_handler()        
        return [self.average_handler(kem_filtered_list[0],5), self.average_handler(kem_filtered_list[1],5), self.average_handler(kem_filtered_list[2],5), self.average_handler(kem_filtered_list[3],5)]

    def getKemMins(self):
        kem_filtered_list = self.filterKemList_handler()
        return [self.min_handler(kem_filtered_list[0],5), self.min_handler(kem_filtered_list[1],5), self.min_handler(kem_filtered_list[2],5), self.min_handler(kem_filtered_list[3],5)]
    
    def getKemMaxs(self):
        kem_filtered_list = self.filterKemList_handler()
        return [self.max_handler(kem_filtered_list[0],5), self.max_handler(kem_filtered_list[1],5), self.max_handler(kem_filtered_list[2],5), self.max_handler(kem_filtered_list[3],5)]
    
    def getKemMedians(self):
        kem_filtered_list = self.filterKemList_handler()
        return [self.median_handler(kem_filtered_list[0],5), self.median_handler(kem_filtered_list[1],5), self.median_handler(kem_filtered_list[2],5), self.median_handler(kem_filtered_list[3],5)]
    
    #DSA  
    def getDsaAverages(self):
        dsa_filtered_list = self.filterDsaList_handler()        
        return [self.average_handler(dsa_filtered_list[0],4), self.average_handler(dsa_filtered_list[1],4), self.average_handler(dsa_filtered_list[2],4)]

    def getDsaMins(self):
        dsa_filtered_list = self.filterDsaList_handler()
        return [self.min_handler(dsa_filtered_list[0],4), self.min_handler(dsa_filtered_list[1],4), self.min_handler(dsa_filtered_list[2],4)]
    
    def getDsaMaxs(self):
        dsa_filtered_list = self.filterDsaList_handler()
        return [self.max_handler(dsa_filtered_list[0],4), self.max_handler(dsa_filtered_list[1],4), self.max_handler(dsa_filtered_list[2],4)]
    
    def getDsaMedians(self):
        dsa_filtered_list = self.filterDsaList_handler()
        return [self.median_handler(dsa_filtered_list[0],4), self.median_handler(dsa_filtered_list[1],4), self.median_handler(dsa_filtered_list[2],4)]
         
    
# TEST AREA        
#s = StatisticsManager()
#s.average_handler([("a", "a", float(10)), ("a", "a", float(15))])

#s.filterKeyList_handler()

#print(s.getKeyAverages())
#print(s.getKeyMins())
#print(s.getKeyMaxs())
#print(s.getKeyMedians())

#print(s.getKemAverages())
#print(s.getKemMins())
#print(s.getKemMaxs())
#print(s.getKemMedians())


#print(s.getDsaAverages())
#print(s.getDsaMins())
#print(s.getDsaMaxs())
#print(s.getDsaMedians())
        
        