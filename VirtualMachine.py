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
        self.execMemory = ExecutionMemory()

        # Open file with the compiled code
        with open(inputName, 'r') as inputFile:
            # Load the JSON
            compiledCode = json.load(inputFile)

            # Load the constant and global variables
            self.execMemory.addConstantMemory(compiledCode['ConstantValues'])
            self.execMemory.addGlobalMemory(
                compiledCode['FuncTable']['global']['varTable'])
            self.execMemory.loadQuads(compiledCode['Quadruples'])

        # Load operators dictionary
        self.functionsDict = {
            1: self.assignationOperation, 2: self.arith_relat_logicOperation,
            3: self.arith_relat_logicOperation, 4: self.arith_relat_logicOperation,
            5: self.arith_relat_logicOperation, 6: self.arith_relat_logicOperation,
            7: self.arith_relat_logicOperation, 8: self.arith_relat_logicOperation,
            9: self.arith_relat_logicOperation, 10: self.arith_relat_logicOperation,
            11: self.arith_relat_logicOperation, 12: self.arith_relat_logicOperation,
            13: self.arith_relat_logicOperation, 14: self.arith_relat_logicOperation,

            15: self.writeOperation, 16: self.readOperation,

            17: self.temporal,
            18: self.temporal,

            19: self.temporal,
            20: self.temporal,

            21: self.temporal,
            22: self.temporal,

            23: self.temporal,
            24: self.verifyOperation,

            25: self.temporal
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
        for quad in self.execMemory.quadsList:
            # Execute the function depending on the operator
            self.functionsDict[quad[0]](quad[1], quad[2], quad[3], quad[0])

    def assignationOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        """
        Function to assign the left operand to the result one. Getting the data from the
        first memory address and storing it on the second one.

        Args:
            lftAddress (integer): Memory address were is located the left value
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            resultAddress (integer): Memory address were is going to be store the value
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        # Get data from the specified address
        lftVal = self.execMemory.getFromMemory(lftAddress)

        # Store the value on the expected memory
        self.execMemory.saveOnMemory(resultAddress,  lftVal)

    def arith_relat_logicOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        """
        Function to get the value from a point A and B, to apply an operator and store it on a C 
        memory address.

        Args:
            lftAddress (integer): Memory address of the A operand
            rghtAddress (integer): Memory address of the B operand
            resultAddress (integer): Memory addres to store the operation result
            operatorNum (operator obj): Operator object with the function to apply to the operands
        """
        # Get the values from the operand address
        lftVal = self.execMemory.getFromMemory(lftAddress)
        rghtVal = self.execMemory.getFromMemory(rghtAddress)

        # Execute the operator function
        resultVal = self.__operatorsDict[operatorNum](lftVal, rghtVal)

        # Store the value on the expected memory
        self.execMemory.saveOnMemory(resultAddress,  resultVal)


    def verifyOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        """
        Make the validation that an index is indide the arrays dimension.

        Args:
            lftAddress (integer): Memory address that store the wanted index
            rghtAddress (integer): Memory address that store the array dimension
            resultAddress (None): None. Just to keep params simetry with all the functions.
            operatorNum (None): None. Just to keep params simetry with all the functions.

        Raises:
            Exception: [description]
        """
        # Get the values from the operand address
        lftVal = self.execMemory.getFromMemory(lftAddress)
        rghtVal = self.execMemory.getFromMemory(rghtAddress)

        if(lftVal > rghtVal):
            raise Exception("Index out of range")


    def writeOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        """
        Print on screen the value stored on the received memory address

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            resultAddress (integer): Memory address in which to find the data to be printed
            operatorNum (None): None. Just to keep params simetry with all the functions.

        Raises:
            Exception: [description]
        """
        # Get the values from the operand address
        resultVal = self.execMemory.getFromMemory(resultAddress)

        if(resultVal != None):
            print(resultVal)

    def readOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        """
        Read input from the console and store it on the received memory address

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            resultAddress (integer): Memory address in which to store the readed data.
            operatorNum (None): None. Just to keep params simetry with all the functions.

        Raises:
            Exception: [description]
        """
        # Ask for input to the user
        inputVal = input()

        self.execMemory.saveOnMemory(resultAddress, inputVal, True)

        print(self.execMemory.ExecMemory[0])
        

    def temporal(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        print("Temporal")


virMachine = VirtualMachine('patito3.obj')
virMachine.proccessQuads()
