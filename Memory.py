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
        self.globalBase = 1000
        self.globalTempBase = 17000
        self.localBase = 33000
        self.localTempBase = 49000
        self.constantBase = 65000

        self.intMem = 0
        self.floatMem = 4000
        self.charMem = 8000
        self.boolMem = 12000
        self.topLimit = 15999

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
            variables (string): list with the values to store.
        """
        if(varType == 'int'):
            self.globalIntCounter += 1
            return (1000 + self.globalIntCounter - 1)

        elif(varType == 'float'):
            self.globalFloatCounter += 1
            return (5000 + self.globalFloatCounter - 1)

        elif(varType == 'char'):
            self.globalCharCounter += 1
            return (9000 + self.globalCharCounter - 1)

        elif(varType == 'bool'):
            self.globalBoolCounter += 1
            return (13000 + self.globalBoolCounter - 1)

    def saveVariableGlobalTemp(self, variables):
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
            variables (string): list with the values to store.
        """
        for var in variables:
            if type(var) is bool:
                self.globalTemporalMemory[self.globalTempBase +
                                          self.boolMem] = var
                self.boolMem += 1
                self.tempGlobalBoolCounter += 1
            elif type(var) is int:
                self.globalTemporalMemory[self.globalTempBase +
                                          self.intMem] = var
                self.intMem += 1
                self.tempGlobalIntCounter += 1
            elif type(var) is float:
                self.globalTemporalMemory[self.globalTempBase +
                                          self.floatMem] = var
                self.floatMem += 1
                self.tempGlobalFloatCounter += 1
            else:
                self.globalTemporalMemory[self.globalTempBase +
                                          self.charMem] = var
                self.charMem += 1
                self.tempGlobalCharCounter += 1

    def saveVariableLocal(self, variables):
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
            variables (string): list with the values to store.
        """
        for var in variables:
            if type(var) is bool:
                self.localMemory[self.localBase+self.boolMem] = var
                self.boolMem += 1
                self.localBoolCounter += 1
            elif type(var) is int:
                self.localMemory[self.localBase+self.intMem] = var
                self.intMem += 1
                self.localIntCounter += 1
            elif type(var) is float:
                self.localMemory[self.localBase+self.floatMem] = var
                self.floatMem += 1
                self.localFloatCounter += 1
            else:
                self.localMemory[self.localBase+self.charMem] = var
                self.charMem += 1
                self.localCharCounter += 1

    def saveVariableLocalTemp(self, variables):
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
            variables (string): list with the values to store.
        """
        for var in variables:
            if type(var) is bool:
                self.localTemporalMemory[self.localTempBase+self.boolMem] = var
                self.boolMem += 1
                self.tempLocalBoolCounter += 1
            elif type(var) is int:
                self.localTemporalMemory[self.localTempBase+self.intMem] = var
                self.intMem += 1
                self.tempLocalIntCounter += 1
            elif type(var) is float:
                self.localTemporalMemory[self.localTempBase +
                                         self.floatMem] = var
                self.floatMem += 1
                self.tempLocalFloatCounter += 1
            else:
                self.localTemporalMemory[self.localTempBase+self.charMem] = var
                self.charMem += 1
                self.tempLocalCharCounter += 1

    def saveVariableConstant(self, variables):
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
            variables (string): list with the values to store.
        """
        for var in variables:
            if type(var) is bool:
                self.constantsMemory[self.constantBase+self.boolMem] = var
                self.boolMem += 1
                self.constantBoolCounter += 1
            elif type(var) is int:
                self.constantsMemory[self.constantBase+self.intMem] = var
                self.intMem += 1
                self.constantIntCounter += 1
            elif type(var) is float:
                self.constantsMemory[self.constantBase+self.floatMem] = var
                self.floatMem += 1
                self.constantFloatCounter += 1
            else:
                self.constantsMemory[self.constantBase+self.charMem] = var
                self.charMem += 1
                self.constantCharCounter += 1

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
        if(mem_address >= self.globalBase and mem_address < self.globalTempBase):
            if(mem_address >= (self.globalBase + self.intMem) and mem_address < (self.globalBase + self.floatMem)):
                return self.get_value(mem_address, self.globalMemory, 'int')
            if(mem_address >= (self.globalBase + self.floatMem) and mem_address < (self.globalBase + self.charMem)):
                return self.get_value(mem_address, self.globalMemory, 'float')
            if(mem_address >= (self.globalBase + self.charMem) and mem_address < (self.globalBase + self.boolMem)):
                return self.get_value(mem_address, self.globalMemory, 'char')
            if(mem_address >= (self.globalBase + self.boolMem) and mem_address < (self.globalBase + self.topLimit)):
                return self.get_value(mem_address, self.globalMemory, 'bool')
        if(mem_address >= self.globalTempBase and mem_address < self.localBase):
            if(mem_address >= (self.globalTempBase + self.intMem) and mem_address < (self.globalTempBase + self.floatMem)):
                return self.get_value(mem_address, self.globalTemporalMemory, 'int')
            if(mem_address >= (self.globalTempBase + self.floatMem) and mem_address < (self.globalTempBase + self.charMem)):
                return self.get_value(mem_address, self.globalTemporalMemory, 'float')
            if(mem_address >= (self.globalTempBase + self.charMem) and mem_address < (self.globalTempBase + self.boolMem)):
                return self.get_value(mem_address, self.globalTemporalMemory, 'char')
            if(mem_address >= (self.globalTempBase + self.boolMem) and mem_address < (self.globalTempBase + self.topLimit)):
                return self.get_value(mem_address, self.globalTemporalMemory, 'bool')
        if(mem_address >= self.localBase and mem_address < self.localTempBase):
            if(mem_address >= (self.localBase + self.intMem) and mem_address < (self.localBase + self.floatMem)):
                return self.get_value(mem_address, self.localMemory, 'int')
            if(mem_address >= (self.localBase + self.floatMem) and mem_address < (self.localBase + self.charMem)):
                return self.get_value(mem_address, self.localMemory, 'float')
            if(mem_address >= (self.localBase + self.charMem) and mem_address < (self.localBase + self.boolMem)):
                return self.get_value(mem_address, self.localMemory, 'char')
            if(mem_address >= (self.localBase + self.boolMem) and mem_address < (self.localBase + self.topLimit)):
                return self.get_value(mem_address, self.localMemory, 'bool')
        if(mem_address >= self.localTempBase and mem_address < self.constantBase):
            if(mem_address >= (self.localTempBase + self.intMem) and mem_address < (self.localTempBase + self.floatMem)):
                return self.get_value(mem_address, self.localTemporalMemory, 'int')
            if(mem_address >= (self.localTempBase + self.floatMem) and mem_address < (self.localTempBase + self.charMem)):
                return self.get_value(mem_address, self.localTemporalMemory, 'float')
            if(mem_address >= (self.localTempBase + self.charMem) and mem_address < (self.localTempBase + self.boolMem)):
                return self.get_value(mem_address, self.localTemporalMemory, 'char')
            if(mem_address >= (self.localTempBase + self.boolMem) and mem_address < (self.localTempBase + self.topLimit)):
                return self.get_value(mem_address, self.localTemporalMemory, 'bool')
        if(mem_address >= self.constantBase and mem_address < (self.constantBase + self.topLimit)):
            if(mem_address >= (self.constantBase + self.intMem) and mem_address < (self.constantBase + self.floatMem)):
                return self.get_value(mem_address, self.constantsMemory, 'int')
            if(mem_address >= (self.constantBase + self.floatMem) and mem_address < (self.constantBase + self.charMem)):
                return self.get_value(mem_address, self.constantsMemory, 'float')
            if(mem_address >= (self.constantBase + self.charMem) and mem_address < (self.constantBase + self.boolMem)):
                return self.get_value(mem_address, self.constantsMemory, 'char')
            if(mem_address >= (self.constantBase + self.boolMem) and mem_address < (self.constantBase + self.topLimit)):
                return self.get_value(mem_address, self.constantsMemory, 'bool')
