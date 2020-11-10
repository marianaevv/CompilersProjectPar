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
        Temporal Local Memory - 49000 and ends at 64999
        Constant Memory - Starts at 65000 and ends at 80999

        Each memory context will be divided into types context (int, bool, float, char, temp)
        avoiding the use of casting values.

        """

        self.baseAddress = {
            1: 1000,
            2: 33000,
            3: 65000
        }

        self.baseTemporalAddress = {
            1: 17000,
            2: 49000
        }

        self.dataTypeRangeStart = {
            'int': 0,
            'float': 4000,
            'char': 8000,
            'bool': 12000,
            'str': 16000
        }

        self.countPositions = {
            1: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            2: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            3: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'str': 0
            }
        }

        self.countTemporalPositions = {
            1: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            2: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            }
        }

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

    def getMemoryAddress(self, varType, size, scope, flgTemp):
        """
        Function to get the memory address for a variable

        Args:
            varType (string): The data type of the variable [int | float | char | string]
            size (integer): Size of the vairibale
            scope (string): Name of the current function or if it is a constant
            flgTemp (bool): To know it is a teporal varible

        Returns:
            [integer]: Assigned memory address
        """

        # Define the scope integer
        if(scope == 'global'):
            scope = 1
        elif(scope == 'constant'):
            scope = 3
        else:
            scope = 2

        # Check if it's a temporal variable or not
        if(not flgTemp):
            # Calculate the address using the non temporal ranges
            memAddress = self.baseAddress[scope] + self.dataTypeRangeStart[varType] + \
                self.countPositions[scope][varType]

            self.countPositions[scope][varType] += size

        else:
            # Calculate the address using the termporal ranges
            memAddress = self.baseTemporalAddress[scope] + self.dataTypeRangeStart[varType] + \
                self.countTemporalPositions[scope][varType]

            self.countTemporalPositions[scope][varType] += size

        return memAddress

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
        self.countPositions[2] = {
            'int': 0,
            'float': 0,
            'char': 0,
            'bool': 0
        }

        self.countTemporalPositions[2] = {
            'int': 0,
            'float': 0,
            'char': 0,
            'bool': 0
        }

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
