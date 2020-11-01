class memory:
    def __init__(self):
    #Save space and value globalMemory = {'int': {'8001' :'32',
    #                                             '8002' :'2'   },
    #                                    'float': {'5002' :'55',
    #                                              '5003' :'6'   } }
    #Recibir la memoria
    #Checar el límite
    self.globalMemory = {}
    self.localMemory = {}
    self.constantsMemory = {}
    self.globalMem = 1000
    self.localMem = 18000
    self.constantMem = 35000
    self.intMem = 1
    self.floatMem = 4000
    self.charMem = 9000
    self.boolMem = 13000
    self.tempMem = 17000
    self.topLimit = 21000

    def saveVariableGlobal(self,variables ){
         for var in variables:
            if type(var) is bool:
                self.globalMemory[self.globalMem+self.boolMem] = var
                self.boolMem += 1
            if type(var) is int:
                self.globalMemory[self.globalMem+self.intMem] = var
                self.intMem += 1
            elif type(var) is float:
                self.globalMemory[self.globalMem+self.floatMem] = var
                self.floatMem += 1
            else:
                self.globalMemory[self.globalMem+self.charMem] = var
                self.charMem += 1
    }

    def saveVariableLocal(self,variables ){
         for var in variables:
            if type(var) is bool:
                self.localMemory[self.localMem+self.boolMem] = var
                self.boolMem += 1
            if type(var) is int:
                self.localMemory[self.localMem+self.intMem] = var
                self.intMem += 1
            elif type(var) is float:
                self.localMemory[self.localMem+self.floatMem] = var
                self.floatMem += 1
            else:
                self.localMemory[self.localMem+self.charMem] = var
                self.charMem += 1
    }
      def saveVariableConstant(self,variables ){
         for var in variables:
            if type(var) is bool:
                self.constantsMemory[self.constantMem+self.boolMem] = var
                self.boolMem += 1
            if type(var) is int:
                self.constantsMemory[self.constantMem+self.intMem] = var
                self.intMem += 1
            elif type(var) is float:
                self.constantsMemory[self.constantMem+self.floatMem] = var
                self.floatMem += 1
            else:
                self.constantsMemory[self.constantMem+self.charMem] = var
                self.charMem += 1
    }

 def get_value(self, address,context, context_type ):
     if address in self.memory[context][context_type]:
            return self.memory[context][context_type][address]
        else:
            return None

 def check_limits(self, mem_address):
        if( mem_address >= self.globalMem and mem_address < self.localMem):
            if(mem_address >= (self.globalMem + self.intMem) and mem_address < self.floatMem)):
                return self.get_value(mem_address, 'global', 'int')
            if(mem_address >= (self.globalMem + self.floatMem) and mem_address < self.charMem)):
                return self.get_value(mem_address, 'global', 'float')
            if(mem_address >= (self.globalMem + self.charMem) and mem_address < self.boolMem)):
                return self.get_value(mem_address, 'global', 'char')
            if(mem_address >= (self.globalMem + self.boolMem) and mem_address < self.tempMem)):
                return self.get_value(mem_address, 'global', 'bool')    
            if(mem_address >= (self.globalMem + self.tempMem) and mem_address < self.topLimit)):
                return self.get_value(mem_address, 'global', 'temp')
        if( mem_address >= self.localMem and mem_address < self.constantMem):
            if(mem_address >= (self.localMem + self.intMem) and mem_address < self.floatMem)):
                return self.get_value(mem_address, 'global', 'int')
            if(mem_address >= (self.localMem + self.floatMem) and mem_address < self.charMem)):
                return self.get_value(mem_address, 'global', 'float')
            if(mem_address >= (self.localMem + self.charMem) and mem_address < self.boolMem)):
                return self.get_value(mem_address, 'global', 'char')
            if(mem_address >= (self.localMem + self.boolMem) and mem_address < self.tempMem)):
                return self.get_value(mem_address, 'global', 'bool')    
            if(mem_address >= (self.localMem + self.tempMem) and mem_address < self.topLimit)):
                return self.get_value(mem_address, 'global', 'temp')
        
       