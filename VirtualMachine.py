import json
import ast
import operator
from ExecutionMemory import ExecutionMemory


class VirtualMachine():
    """
    Class to simula a computer executing a compiled program
    """

    def __init__(self, inputName):

        # Instance of the virtual memory
        self.virtMemory = ExecutionMemory()

        # Open file with the compiled code
        with open(inputName, 'r') as inputFile:
            # Load the JSON
            compiledCode = json.load(inputFile)

            # Load the constant and global variables
            self.virtMemory.addConstantMemory(compiledCode['ConstantValues'])
            self.virtMemory.addGlobalMemory(compiledCode['FuncTable']['global']['varTable'])
            self.virtMemory.loadQuads(compiledCode['Quadruples'])

        # Load operators dictionary
        self.functionsDict = {
            1: self.assignationOperation,
            2: self.arith_relat_logicOperation,

            3: self.arith_relat_logicOperation,
            4: self.arith_relat_logicOperation,

            5: self.arith_relat_logicOperation,
            6: self.arith_relat_logicOperation,

            7: self.arith_relat_logicOperation,
            8: self.arith_relat_logicOperation,

            9: self.arith_relat_logicOperation,
            10: self.arith_relat_logicOperation,

            11: self.arith_relat_logicOperation,
            12: self.arith_relat_logicOperation,

            13: self.arith_relat_logicOperation,
            14: self.arith_relat_logicOperation,

            15: self.temporal,
            16: self.temporal,

            17: self.temporal,
            18: self.temporal,

            19: self.temporal,
            20: self.temporal,

            21: self.temporal,
            22: self.temporal,

            23: self.temporal,
            24: self.temporal,

            25: self.temporal,
            26: self.temporal,

            27: self.temporal
        }

        # From operator ID to python operators
        self.__operatorsDict = {
            2: operator.add, 3: operator.sub,
            4: operator.mul, 5: operator.mod,
            6: operator.truediv, 7: operator.ge,
            8: operator.le, 9: operator.gt,
            10: operator.lt, 11: operator.eq,
            12: operator.ne, 13: operator.or_,
            14: operator.and_
        }

    def proccessQuads(self):
        """
        Go through all the quadruples and execute what is necessary
        """
        for quad in self.virtMemory.quadsList:
            # Execute the function depending on the operator
            self.functionsDict[quad[0]](quad[1], quad[2], quad[3], quad[0])

    def assignationOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        """
        Function to assign the left operand to the result one. Getting the data from the
        first memory address and storing it on the second one.

        Args:
            lftAddress (integer): Memory address were is located the left value
            rghtAddress (None): None. Just to jeep params simetry with all the functions.
            resultAddress (integer): Memory address were is going to be store the value
            operatorNum (None): None. Just to jeep params simetry with all the functions.
        """
        # Get data from the specified address
        lftVal = self.virtMemory.getFromMemory(lftAddress)
        print(type(lftVal))

        # Store the value on the expected memory
        self.virtMemory.saveOnMemory(resultAddress,  lftVal)

        print(self.virtMemory.ExecMemory[0])

    def arith_relat_logicOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        # Get the values from the operand address
        lftVal = self.virtMemory.getFromMemory(lftAddress)
        rghtVal = self.virtMemory.getFromMemory(rghtAddress)
        print(type(lftVal))

        # Execute the operator function
        resultVal = self.__operatorsDict[operatorNum](int(lftVal), int(rghtVal))

        # Store the value on the expected memory
        self.virtMemory.saveOnMemory(resultAddress,  resultVal)

    def temporal(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        print("Temporal")


virMachine = VirtualMachine('patito3.obj')
virMachine.proccessQuads()
