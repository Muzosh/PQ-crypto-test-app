from datetime import datetime
import statistics


class StatisticsManager:
    """
    This class handles everything around statistics, data mining, collecting data, etc...

    Constructor:
        passwordManager (PasswordManager): existing instance of PasswordManager managing keyStores database
        + creating lists for storing data
    """

    def __init__(self, passwordManager):
        """
        Constructor:
            passwordManager (PasswordManager): existing instance of PasswordManager managing keyStores database
            + creating lists for storing data
        """
        self.keyGenEntries = []
        self.kemAesEntries = []
        self.dsaEntries = []
        self.passwordManager = passwordManager

    def addKeyGenEntry(
        self, datetime: datetime, alg: str, timeInMiliseconds: float
    ):
        """
        This method adds data about key generation to the list.

        Args:
            datetime (datetime): Date when the key was generated
            alg (str): Name of used algorithm for key generation
            timeInMiliseconds (float): Duration of generation in miliseconds
        """
        self.keyGenEntries.append((datetime, alg, timeInMiliseconds))

    def addKemAesEntry(
        self,
        datetime: datetime,
        alg: str,
        operationType: str,
        aesBlockSize: int,
        fileSize: int,
        kemTimeInMiliseconds: float,
        aesTimeInMiliseconds: float,
    ):
        """
        This method adds data about encryption/decryption process to the list.

        Args:
            datetime (datetime): Date when the key was generated
            alg (str): Name of used KEM algorithm
            operationType (str): Encryption/Decryption
            aesBlockSize (int): 256b
            fileSize (int): Size of ecrypted/decrypted file
            kemTimeInMiliseconds (float): Duration of encapsulation/decapsulation in miliseconds
            aesTimeInMiliseconds (float): Duration of AES encryption/decrypion in miliseconds
        """
        self.kemAesEntries.append(
            (
                datetime,
                alg,
                operationType,
                aesBlockSize,
                fileSize,
                kemTimeInMiliseconds,
                aesTimeInMiliseconds,
            )
        )

    def addDsaEntry(
        self,
        datetime: datetime,
        alg: str,
        operationType: str,
        fileSize: int,
        timeInMiliseconds: float,
    ):
        """
        This method adds data about signing/verifying to the list.

        Args:
            datetime (datetime): Date when the key was generated
            alg (str): Name of used DSA algorithm
            operationType (str): Sign/Verify
            fileSize (int): Size of ecrypted/decrypted file
            timeInMiliseconds (float): Duration of signing/verifying in miliseconds
        """
        self.dsaEntries.append(
            (datetime, alg, operationType, fileSize, timeInMiliseconds)
        )

    def saveStatisticsToFile(self):
        """
        This method saves statistics data to the file.
        """
        self.passwordManager.writeStatistics(
            self.keyGenEntries, self.kemAesEntries, self.dsaEntries
        )

    def loadStatisticsFromFile(self):
        """
        This method loads statistics data after log in.
        """
        (
            self.keyGenEntries,
            self.kemAesEntries,
            self.dsaEntries,
        ) = self.passwordManager.readStatistics()

    def average_handler(self, list):
        """
        This method computes average duration from given list.

        Args:
            list: List from which average is computed
        """
        if len(list) == 0:
            return "N/A"
        else:
            return sum(list) / len(list)

    def min_handler(self, list):
        """
        This method computes minimum duration from given list.

        Args:
            list: List from which minimum is computed
        """
        if len(list) == 0:
            return "N/A"
        else:
            return min(list)

    def max_handler(self, list):
        """
        This method computes maximum duration from given list.

        Args:
            list: List from which maximum is computed
        """
        if len(list) == 0:
            return "N/A"
        else:
            return max(list)

    def median_handler(self, list):
        """
        This method computes median duration from given list.

        Args:
            list: List from which median is computed
        """
        if len(list) == 0:
            return "N/A"
        else:
            return statistics.median(list)

    def filterKeyList_handler(self):
        """
        This method filters list of tuples keyGenEntries according to alg attribute with index 1 to create separated
        lists for each PQ algorithm just with duration expressions.
        """
        mceliece = [
            tup[2] for tup in self.keyGenEntries if (tup[1] == "McEliece")
        ]
        saber = [tup[2] for tup in self.keyGenEntries if (tup[1] == "Saber")]
        kyber = [tup[2] for tup in self.keyGenEntries if (tup[1] == "Kyber")]
        nthrups = [
            tup[2] for tup in self.keyGenEntries if (tup[1] == "Nthrups")
        ]
        dilithium = [
            tup[2] for tup in self.keyGenEntries if (tup[1] == "Dilithium")
        ]
        rainbow = [
            tup[2] for tup in self.keyGenEntries if (tup[1] == "RainbowVc")
        ]
        sphincs = [
            tup[2] for tup in self.keyGenEntries if (tup[1] == "Sphincs")
        ]
        return mceliece, kyber, saber, nthrups, dilithium, rainbow, sphincs

    def filterEncryptList_handler(self):
        """
        This method filters list of tuples kemAesEntries according to alg attribute with index 1 and only for encryption process
        to create separated lists for each PQ algorithm just with duration expressions.
        """
        mceliece = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "McEliece" and tup[2] == "Encrypt")
        ]
        saber = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "Saber" and tup[2] == "Encrypt")
        ]
        kyber = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "Kyber" and tup[2] == "Encrypt")
        ]
        nthrups = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "Nthrups" and tup[2] == "Encrypt")
        ]
        return mceliece, kyber, saber, nthrups

    def filterDecryptList_handler(self):
        """
        This method filters list of tuples kemAesEntries according to alg attribute with index 1 and only for decryption process
        to create separated lists for each PQ algorithm just with duration expressions.
        """
        mceliece = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "McEliece" and tup[2] == "Decrypt")
        ]
        saber = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "Saber" and tup[2] == "Decrypt")
        ]
        kyber = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "Kyber" and tup[2] == "Decrypt")
        ]
        nthrups = [
            tup[5] + tup[6] / tup[4]
            for tup in self.kemAesEntries
            if (tup[1] == "Nthrups" and tup[2] == "Decrypt")
        ]
        return mceliece, kyber, saber, nthrups

    def filterSignList_handler(self):
        """
        This method filters list of tuples dsaEntries according to alg attribute with index 1 and only for signing
        to create separated lists for each PQ algorithm just with duration expressions.
        """
        dilithium = [
            tup[4] / tup[3]
            for tup in self.dsaEntries
            if (tup[1] == "Dilithium" and tup[2] == "Sign")
        ]
        rainbow = [
            tup[4] / tup[3]
            for tup in self.dsaEntries
            if (tup[1] == "RainbowVc" and tup[2] == "Sign")
        ]
        sphincs = [
            tup[4] / tup[3]
            for tup in self.dsaEntries
            if (tup[1] == "Sphincs" and tup[2] == "Sign")
        ]
        return dilithium, rainbow, sphincs

    def filterVerifyList_handler(self):
        """
        This method filters list of tuples dsaEntries according to alg attribute with index 1 and only for verifying
        to create separated lists for each PQ algorithm just with duration expressions.
        """
        dilithium = [
            tup[4] / tup[3]
            for tup in self.dsaEntries
            if (tup[1] == "Dilithium" and tup[2] == "Verify")
        ]
        rainbow = [
            tup[4] / tup[3]
            for tup in self.dsaEntries
            if (tup[1] == "RainbowVc" and tup[2] == "Verify")
        ]
        sphincs = [
            tup[4] / tup[3]
            for tup in self.dsaEntries
            if (tup[1] == "Sphincs" and tup[2] == "Verify")
        ]
        return dilithium, rainbow, sphincs

    # Getters for Key/KEM/DSA average/min/max/median
    def getKeyAverages(self):
        key_filtered_list = self.filterKeyList_handler()
        return [
            self.average_handler(key_filtered_list[i])
            for i in range(len(key_filtered_list))
        ]

    def getKeyMins(self):
        key_filtered_list = self.filterKeyList_handler()
        return [
            self.min_handler(key_filtered_list[i])
            for i in range(len(key_filtered_list))
        ]

    def getKeyMaxes(self):
        key_filtered_list = self.filterKeyList_handler()
        return [
            self.max_handler(key_filtered_list[i])
            for i in range(len(key_filtered_list))
        ]

    def getKeyMedians(self):
        key_filtered_list = self.filterKeyList_handler()
        return [
            self.median_handler(key_filtered_list[i])
            for i in range(len(key_filtered_list))
        ]

    def getEncryptAverages(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [
            self.average_handler(encypt_filtered_list[i])
            for i in range(len(encypt_filtered_list))
        ]

    def getEncryptMins(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [
            self.min_handler(encypt_filtered_list[i])
            for i in range(len(encypt_filtered_list))
        ]

    def getEncryptMaxes(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [
            self.max_handler(encypt_filtered_list[i])
            for i in range(len(encypt_filtered_list))
        ]

    def getEncryptMedians(self):
        encypt_filtered_list = self.filterEncryptList_handler()
        return [
            self.median_handler(encypt_filtered_list[i])
            for i in range(len(encypt_filtered_list))
        ]

    def getDecryptAverages(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [
            self.average_handler(decrypt_filtered_list[i])
            for i in range(len(decrypt_filtered_list))
        ]

    def getDecryptMins(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [
            self.min_handler(decrypt_filtered_list[i])
            for i in range(len(decrypt_filtered_list))
        ]

    def getDecryptMaxes(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [
            self.max_handler(decrypt_filtered_list[i])
            for i in range(len(decrypt_filtered_list))
        ]

    def getDecryptMedians(self):
        decrypt_filtered_list = self.filterDecryptList_handler()
        return [
            self.median_handler(decrypt_filtered_list[i])
            for i in range(len(decrypt_filtered_list))
        ]

    def getSignAverages(self):
        sign_filtered_list = self.filterSignList_handler()
        return [
            self.average_handler(sign_filtered_list[i])
            for i in range(len(sign_filtered_list))
        ]

    def getSignMins(self):
        sign_filtered_list = self.filterSignList_handler()
        return [
            self.min_handler(sign_filtered_list[i])
            for i in range(len(sign_filtered_list))
        ]

    def getSignMaxes(self):
        sign_filtered_list = self.filterSignList_handler()
        return [
            self.max_handler(sign_filtered_list[i])
            for i in range(len(sign_filtered_list))
        ]

    def getSignMedians(self):
        sign_filtered_list = self.filterSignList_handler()
        return [
            self.median_handler(sign_filtered_list[i])
            for i in range(len(sign_filtered_list))
        ]

    def getVerifyAverages(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [
            self.average_handler(verify_filtered_list[i])
            for i in range(len(verify_filtered_list))
        ]

    def getVerifyMins(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [
            self.min_handler(verify_filtered_list[i])
            for i in range(len(verify_filtered_list))
        ]

    def getVerifyMaxes(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [
            self.max_handler(verify_filtered_list[i])
            for i in range(len(verify_filtered_list))
        ]

    def getVerifyMedians(self):
        verify_filtered_list = self.filterVerifyList_handler()
        return [
            self.median_handler(verify_filtered_list[i])
            for i in range(len(verify_filtered_list))
        ]


# # TEST AREA
# s = StatisticsManager()
# #s.average_handler([("a", "a", float(10)), ("a", "a", float(15))])
# #print(s.getKeyAverages())

# s.filterKeyList_handler()
# #print(s.getKeyMins())

# print(s.getKeyMedians())
