class Memory:
    def __init__(self):
        """
        Dictionaries to save values according to the context and the value type
        """
        self.globalMemory = {
            'int': {},
            'float': {},
            'bool': {},
            'char': {}
        }

        self.globalTemporalMemory = self.globalMemory.copy()
        self.localMemory = self.globalMemory.copy()
        self.localTemporalMemory = self.globalMemory.copy()
        self.constantsMemory = self.globalMemory.copy()

        self.backupLocalMemory = {
            'local': []
        }
        self.backupLocalTempMemory = {
            'temporal': []
        }

        """
        Global Memory - Starts at 1000 and ends at 15999
        Temporal Global Memory - 17000 and ends at 32999
        Local Memory - Starts at 33000 and ends at 48999
        Temporal Global Memory - 49000 and ends at 64999
        Constant Memory - Starts at 65000 and ends at 80999

        Each memory context will be divided into types context (int, bool, float, char, temp)
        avoiding the use of casting values.

        """

        """
        Counters will help to keep record of how much memory will be needed in execution
        """
        self.globalIntCounter = 0
        self.globalFloatCounter = 0
        self.globalBoolCounter = 0
        self.globalCharCounter = 0

        self.tempGlobalIntCounter = 0
        self.tempGlobalFloatCounter = 0
        self.tempGlobalBoolCounter = 0
        self.tempGlobalCharCounter = 0

        self.localIntCounter = 0
        self.localFloatCounter = 0
        self.localBoolCounter = 0
        self.localCharCounter = 0

        self.tempLocalIntCounter = 0
        self.tempLocalFloatCounter = 0
        self.tempLocalBoolCounter = 0
        self.tempLocalCharCounter = 0

        self.constantIntCounter = 0
        self.constantFloatCounter = 0
        self.constantBoolCounter = 0
        self.constantCharCounter = 0
        self.constantStringCounter = 0

    def getGlobalAddress(self, varType, flgArray=False):
        """
        Saves values into the Global context depending on the type of value
        being save (int, float, char, bool)

        Example: globalMemory = {
                                'int': {
                                        '8001' :'32',
                                        '8002' :'24'
                                        },
                                'float' :{
                                        '5002' :'55',
                                        '5003' :'63'
                                        }
                                 }

        Args:
            varType (String): Type of variable
            flgArray (Bool): variable that checks if the type belongs to a matrix or array
        """
        if(varType == 'int'):
            self.tempGlobalIntCounter += 1
            return (1000 + self.tempGlobalIntCounter - 1)

        elif(varType == 'float'):
            self.tempGlobalFloatCounter += 1
            return (5000 + self.tempGlobalFloatCounter - 1)

        elif(varType == 'char'):
            self.tempGlobalCharCounter += 1
            return (9000 + self.tempGlobalCharCounter - 1)

        elif(varType == 'bool'):
            self.tempGlobalBoolCounter += 1
            return (13000 + self.tempGlobalBoolCounter - 1)

    def getVariableGlobalTempAddress(self, varType, flgArray=False):
        """
        Saves values into the Temporal Global context depending on the type of value
        being save (int, float, char, bool)

        Example: globalTemporalMemory = {
                                'int': {
                                        '8001' :'32',
                                        '8002' :'24'
                                        },
                                'float' :{
                                        '5002' :'55',
                                        '5003' :'63'
                                        }
                                 }

        Args:
            vvarType (String): Type of variable
            flgArray (Bool): variable that checks if the type belongs to a matrix or array
        """
        if(varType == 'int'):
            self.globalIntCounter += 1
            return (17000 + self.globalIntCounter - 1)

        elif(varType == 'float'):
            self.globalFloatCounter += 1
            return (21000 + self.globalFloatCounter - 1)

        elif(varType == 'char'):
            self.globalCharCounter += 1
            return (25000 + self.globalCharCounter - 1)

        elif(varType == 'bool'):
            self.globalBoolCounter += 1
            return (29000 + self.globalBoolCounter - 1)

    def getVariableLocalAddress(self, varType, flgArray=False):
        """
        Saves values into the Local context depending on the type of value
        being save (int, float, char, bool)

        Example: localMemory = {
                                'int': {
                                        '8001' :'32',
                                        '8002' :'24'
                                        },
                                'float' :{
                                        '5002' :'55',
                                        '5003' :'63'
                                        }
                                 }

        Args:
           varType (String): Type of variable
            flgArray (Bool): variable that checks if the type belongs to a matrix or array
        """
        if(varType == 'int'):
            self.localIntCounter += 1
            return (33000 + self.localIntCounter - 1)

        elif(varType == 'float'):
            self.localFloatCounter += 1
            return (37000 + self.localFloatCounter - 1)

        elif(varType == 'char'):
            self.localCharCounter += 1
            return (41000 + self.localCharCounter - 1)

        elif(varType == 'bool'):
            self.localBoolCounter += 1
            return (45000 + self.localBoolCounter - 1)

    def getVariableLocalTempAddress(self, varType, flgArray=False):
        """
        Saves values into the Local Temporal context depending on the type of value
        being save (int, float, char, bool)

        Example: localTemporalMemory = {
                                'int': {
                                        '8001' :'32',
                                        '8002' :'24'
                                        },
                                'float' :{
                                        '5002' :'55',
                                        '5003' :'63'
                                        }
                                 }

        Args:
            varType (String): Type of variable
            flgArray (Bool): variable that checks if the type belongs to a matrix or array
        """
        if(varType == 'int'):
            self.tempLocalIntCounter += 1
            return (49000 + self.tempLocalIntCounter - 1)

        elif(varType == 'float'):
            self.tempLocalFloatCounter += 1
            return (53000 + self.tempLocalFloatCounter - 1)

        elif(varType == 'char'):
            self.tempLocalCharCounter += 1
            return (57000 + self.tempLocalCharCounter - 1)

        elif(varType == 'bool'):
            self.tempLocalBoolCounter += 1
            return (61000 + self.tempLocalBoolCounter - 1)

    def getVariableConstantAddress(self, varType, flgArray=False):
        """
        Saves values into the Constant context depending on the type of value
        being save (int, float, char, bool)

        Example: constantMemory = {
                                'int': {
                                        '8001' :'32',
                                        '8002' :'24'
                                        },
                                'float' :{
                                        '5002' :'55',
                                        '5003' :'63'
                                        }
                                 }

        Args:
            varType (String): Type of variable
            flgArray (Bool): variable that checks if the type belongs to a matrix or array
        """
        if(varType == 'int'):
            self.constantIntCounter += 1
            return (65000 + self.constantIntCounter - 1)

        elif(varType == 'float'):
            self.constantFloatCounter += 1
            return (69000 + self.constantFloatCounter - 1)

        elif(varType == 'char'):
            self.constantCharCounter += 1
            return (73000 + self.constantCharCounter - 1)

        elif(varType == 'bool'):
            self.constantBoolCounter += 1
            return (77000 + self.constantBoolCounter - 1)

        elif(varType == 'str'):
            self.constantStringCounter += 1
            return (81000 + self.constantStringCounter - 1)

    def savesBackupLocalMemory(self):
        """
        Saves de values of both local Memory and local temporal Memory in another structure
        """
        self.backupLocalMemory['local'].append(self.localMemory)
        self.backupLocalTempMemory['temporal'].append(self.localTemporalMemory)

    def resetLocalCounters(self):
        """
        Reinitialize values for local context and temporal local context so other function can start de count.
        """
        self.localIntCounter = 0
        self.localFloatCounter = 0
        self.localBoolCounter = 0
        self.localCharCounter = 0

        self.tempLocalIntCounter = 0
        self.tempLocalFloatCounter = 0
        self.tempLocalBoolCounter = 0
        self.tempLocalCharCounter = 0

    def get_value(self, address, context, context_type):
        """
        Function to get the value of the address sent as a parameter

        Args:
            address (string): key to look in the dictionary inside the context type to get the value save in the address space.
            context: dictionary to look into (Global, Local, Constant)
            context_type: type to look into the dictionary (int, float, bool, char, temp)
        """
        if address in context[context_type]:
            return context[context_type][address]
        else:
            return None

    def check_limits(self, mem_address):
        """
        Function to check in which context the address sent as a parameter is, either global, local,
        constant and inside that context in which context type is, either int, float, bool, char or temp

        Args:
            mem_address: Memory address
        """
        if(1000 <= mem_address < 17000):
            if(1000 <= mem_address < 5000):
                varType = 'int'
            elif(5000 <= mem_address < 9000):
                varType = 'float'
            elif(9000 <= mem_address < 13000):
                varType = 'char'
            elif(13000 <= mem_address < 17000):
                varType = 'bool'

            return self.get_value(mem_address, self.globalMemory, varType)
        elif(17000 <= mem_address < 33000):
            if(17000 <= mem_address < 21000):
                varType = 'int'
            elif(21000 <= mem_address < 25000):
                varType = 'float'
            elif(25000 <= mem_address < 29000):
                varType = 'char'
            elif(29000 <= mem_address < 33000):
                varType = 'bool'

            return self.get_value(mem_address, self.globalTemporalMemory, varType)
        elif(33000 <= mem_address < 49000):
            if(33000 <= mem_address < 37000):
                varType = 'int'
            elif(37000 <= mem_address < 41000):
                varType = 'float'
            elif(41000 <= mem_address < 45000):
                varType = 'char'
            elif(49000 <= mem_address < 53000):
                varType = 'bool'

            return self.get_value(mem_address, self.localMemory, varType)
        elif(49000 <= mem_address < 65000):
            if(49000 <= mem_address < 53000):
                varType = 'int'
            elif(53000 <= mem_address < 57000):
                varType = 'float'
            elif(57000 <= mem_address < 61000):
                varType = 'char'
            elif(61000 <= mem_address < 65000):
                varType = 'bool'

            return self.get_value(mem_address, self.localTemporalMemory, varType)
        elif(65000 <= mem_address < 77000):
            if(65000 <= mem_address < 69000):
                varType = 'int'
            elif(69000 <= mem_address < 73000):
                varType = 'float'
            elif(73000 <= mem_address < 77000):
                varType = 'char'
            elif(77000 <= mem_address < 81000):
                varType = 'bool'
            elif(81000 <= mem_address < 85000):
                varType = 'str'

            return self.get_value(mem_address, self.constantsMemory, varType)
