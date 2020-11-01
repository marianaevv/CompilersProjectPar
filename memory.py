class memory:
    def __init__(self):
        self.globalMemory = {
            'int' = {},
            'float' = {},
            'bool' = {},
            'char' = {}
        }
        self.localMemory = {
            'int' = {},
            'float' = {},
            'bool' = {},
            'char' = {}
        }
        self.constantsMemory = {
            'int' = {},
            'float' = {},
            'bool' = {},
            'char' = {}
        }
        self.globalMem = 1000 #Comienza en 1000 y termina en 20999
        self.localMem = 21000 #Comienza en 21000 y termina en 40999
        self.constantMem = 41000 # Comienza en 41000 y termina en 60000
        self.intMem = 1
        self.floatMem = 4000
        self.charMem = 8000
        self.boolMem = 12000
        self.tempMem = 16000
        self.topLimit = 19999

    def saveVariableGlobal(self,variables):
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
         for var in variables:
            if type(var) is bool:
                self.globalMemory[self.globalMem+self.boolMem] = var
                self.boolMem += 1
            elif type(var) is int:
                self.globalMemory[self.globalMem+self.intMem] = var
                self.intMem += 1
            elif type(var) is float:
                self.globalMemory[self.globalMem+self.floatMem] = var
                self.floatMem += 1
            else:
                self.globalMemory[self.globalMem+self.charMem] = var
                self.charMem += 1
    

    def saveVariableLocal(self,variables):
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
                self.localMemory[self.localMem+self.boolMem] = var
                self.boolMem += 1
            elif type(var) is int:
                self.localMemory[self.localMem+self.intMem] = var
                self.intMem += 1
            elif type(var) is float:
                self.localMemory[self.localMem+self.floatMem] = var
                self.floatMem += 1
            else:
                self.localMemory[self.localMem+self.charMem] = var
                self.charMem += 1

    def saveVariableConstant(self,variables):
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
                self.constantsMemory[self.constantMem+self.boolMem] = var
                self.boolMem += 1
            elif type(var) is int:
                self.constantsMemory[self.constantMem+self.intMem] = var
                self.intMem += 1
            elif type(var) is float:
                self.constantsMemory[self.constantMem+self.floatMem] = var
                self.floatMem += 1
            else:
                self.constantsMemory[self.constantMem+self.charMem] = var
                self.charMem += 1
    

    def get_value(self, address,context, context_type ):
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
            if( mem_address >= self.globalMem and mem_address < self.localMem):
                if(mem_address >= (self.globalMem + self.intMem) and mem_address < (self.globalMem + self.floatMem)):
                    return self.get_value(mem_address, self.globalMemory, 'int')
                if(mem_address >= (self.globalMem + self.floatMem) and mem_address <(self.globalMem + self.charMem)):
                    return self.get_value(mem_address, self.globalMemory, 'float')
                if(mem_address >= (self.globalMem + self.charMem) and mem_address < (self.globalMem + self.boolMem)):
                    return self.get_value(mem_address, self.globalMemory, 'char')
                if(mem_address >= (self.globalMem + self.boolMem) and mem_address < (self.globalMem + self.tempMem)):
                    return self.get_value(mem_address, self.globalMemory, 'bool')    
                if(mem_address >= (self.globalMem + self.tempMem) and mem_address < (self.globalMem + self.topLimit)):
                    return self.get_value(mem_address, self.globalMemory, 'temp')
            if( mem_address >= self.localMem and mem_address < self.constantMem):
                if(mem_address >= (self.localMem + self.intMem) and mem_address < (self.localMem + self.floatMem)):
                    return self.get_value(mem_address, self.localMemory, 'int')
                if(mem_address >= (self.localMem + self.floatMem) and mem_address < (self.localMem + self.charMem)):
                    return self.get_value(mem_address, self.localMemory, 'float')
                if(mem_address >= (self.localMem + self.charMem) and mem_address < (self.localMem + self.boolMem)):
                    return self.get_value(mem_address, self.localMemory, 'char')
                if(mem_address >= (self.localMem + self.boolMem) and mem_address < (self.localMem + self.tempMem)):
                    return self.get_value(mem_address, self.localMemory, 'bool')    
                if(mem_address >= (self.localMem + self.tempMem) and mem_address < (self.localMem + self.topLimit)):
                    return self.get_value(mem_address, self.localMemory, 'temp')
            if( mem_address >= self.constantMem and mem_address < (self.constantMem + self.topLimit)):
                if(mem_address >= (self.constantMem + self.intMem) and mem_address < (self.constantMem + self.floatMem)):
                    return self.get_value(mem_address, self.constantMem, 'int')
                if(mem_address >= (self.constantMem + self.floatMem) and mem_address < (self.constantMem + self.charMem)):
                    return self.get_value(mem_address, self.constantMem, 'float')
                if(mem_address >= (self.constantMem + self.charMem) and mem_address < (self.constantMem + self.boolMem)):
                    return self.get_value(mem_address, self.constantMem, 'char')
                if(mem_address >= (self.constantMem + self.boolMem) and mem_address < (self.constantMem + self.tempMem)):
                    return self.get_value(mem_address, self.constantMem, 'bool')    
                if(mem_address >= (self.constantMem + self.tempMem) and mem_address < (self.constantMem + self.topLimit)):
                    return self.get_value(mem_address, self.constantMem, 'temp')
        
       