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
            if type(i) is bool:
                self.globalMemory[self.globalMem+self.boolMem] = i
                self.boolMem += 1
            if type(i) is int:
                self.globalMemory[self.globalMem+self.intMem] = i
                self.intMem += 1
            elif type(i) is float:
                self.globalMemory[self.globalMem+self.floatMem] = i
                self.floatMem += 1
            else:
                self.globalMemory[self.globalMem+self.charMem] = i
                self.charMem += 1
    }

    def saveVariableLocal(self,variables ){
         for var in variables:
            if type(i) is bool:
                self.localMemory[self.localMem+self.boolMem] = i
                self.boolMem += 1
            if type(i) is int:
                self.localMemory[self.localMem+self.intMem] = i
                self.intMem += 1
            elif type(i) is float:
                self.localMemory[self.localMem+self.floatMem] = i
                self.floatMem += 1
            else:
                self.localMemory[self.localMem+self.charMem] = i
                self.charMem += 1
    }
      def saveVariableConstant(self,variables ){
         for var in variables:
            if type(i) is bool:
                self.constantsMemory[self.constantMem+self.boolMem] = i
                self.boolMem += 1
            if type(i) is int:
                self.constantsMemory[self.constantMem+self.intMem] = i
                self.intMem += 1
            elif type(i) is float:
                self.constantsMemory[self.constantMem+self.floatMem] = i
                self.floatMem += 1
            else:
                self.constantsMemory[self.constantMem+self.charMem] = i
                self.charMem += 1
    }
