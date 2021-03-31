from datetime import datetime

class StatisticsManager:
    def __init__(self):
        self.__keyGenEntries = []
        self.__kemAesEntries = []
        self.__dsaEntries = []
    
    def addKeyGenEntry(self, datetime:datetime, alg:str, timeInSeconds:float):
        self.__keyGenEntries.append((datetime, alg, timeInSeconds))
        
    def addKemAesEntry(self, datetime:datetime, alg:str, type:str, aesBlockSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float):
        self.__kemAesEntries.append((datetime, alg, type, aesBlockSize, kemTimeInSeconds, aesTimeInSeconds))
        
    def addDsaEntry(self, datetime:datetime, alg:str, type:str, timeInSeconds:float):
        self.__dsaEntries.append((datetime, alg, type, timeInSeconds))