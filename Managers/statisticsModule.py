from datetime import datetime

class StatisticsManager:
    """This class handles everything around statistics, data mining, collecting data, etc...
    Available public methods:
        addKeyGenEntry(datetime:datetime, alg:str, timeInSeconds:float) -> None
        addKemAesEntry(datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float) -> None
        addDsaEntry(datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float) -> None
    """
    
    def __init__(self):
        self.keyGenEntries = []
        self.kemAesEntries = []
        self.dsaEntries = []
    
    def addKeyGenEntry(self, datetime:datetime, alg:str, timeInSeconds:float):
        self.keyGenEntries.append((datetime, alg, timeInSeconds))
        
    def addKemAesEntry(self, datetime:datetime, alg:str, operationType:str, aesBlockSize:int, fileSize:int, kemTimeInSeconds:float, aesTimeInSeconds:float):
        self.kemAesEntries.append((datetime, alg, operationType, aesBlockSize, fileSize, kemTimeInSeconds, aesTimeInSeconds))
        
    def addDsaEntry(self, datetime:datetime, alg:str, operationType:str, fileSize:int, timeInSeconds:float):
        self.dsaEntries.append((datetime, alg, operationType, fileSize, timeInSeconds))
        
        