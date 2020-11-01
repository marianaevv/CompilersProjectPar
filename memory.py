class memory:
    def __init__(self):
    
    self.globalMemory = {}
    self.localMemory = {}
    self.constantsMemory = {}
    self.globalMem = 1000
    self.localMem = 21000
    self.constantMem = 40000
    self.intMem = 1
    self.floatMem = 6000
    self.charMem = 11000
    self.boolMem = 16000

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
