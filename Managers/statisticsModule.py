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
    
    def addKeyGenEntry(self, datetime:datetime, alg:str, timeInSeconds:float):
        self.__keyGenEntries.append((datetime, alg, timeInSeconds))
        
    def addKemAesEntry(self, datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float):
        self.__kemAesEntries.append((datetime, alg, operationType, aesBlockSize, fileSize, kemTimeInSeconds, aesTimeInSeconds))
        
    def addDsaEntry(self, datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float):
        self.__dsaEntries.append((datetime, alg, operationType, fileSize, timeInSeconds))
        
        