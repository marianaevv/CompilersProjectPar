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
            self.compiledCode = json.load(inputFile)

            # Load the constant and global variables
            self.execMemory.reserveContextMemmory(
                self.compiledCode['FuncTable']['global']['numVars'],
                self.compiledCode['FuncTable']['global']['numTempVars'], 0)
            self.execMemory.addConstantMemory(
                self.compiledCode['ConstantValues'])
            self.execMemory.loadQuads(self.compiledCode['Quadruples'])

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
            17: self.paramQuad, 18: self.eraQuad,
            19: self.returnQuad, 20: self.endFunction,
            21: self.gotoQuad, 22: self.gosubQuad,
            23: self.gotof, 24: self.verifyOperation,
            25: self.endProgram
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
        self.countQuad = 0

        while True:
            quad = self.execMemory.quadsList[self.countQuad]

            # Execute the function depending on the operator
            self.functionsDict[quad[0]](quad[1], quad[2], quad[3], quad[0])

            # To end the program
            if(self.countQuad == 'EXIT'):
                break
            else:
                self.countQuad += 1

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

        # If it is not a array/matrix assignation
        if(type(lftVal) == int):
            # Store the value on the expected memory
            self.execMemory.saveOnMemory(resultAddress, lftVal)

        # If it is a array/matrix
        else:
            # Get the array data of the B value
            rghtVal = self.execMemory.getFromMemory(resultAddress)

            # Ge the base direction
            baseB = ast.literal_eval(lftVal)[0]
            sizeB = ast.literal_eval(lftVal)[1]
            baseA = ast.literal_eval(rghtVal)[0]

            # Save the data of array B onto A
            for iI in range(sizeB):
                getVale = self.execMemory.getFromMemory(baseB + iI)
                self.execMemory.saveOnMemory(baseA + iI, getVale)

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
        """
        # Get the values from the operand address
        resultVal = self.execMemory.getFromMemory(resultAddress)

        if(resultVal == ""):
            print()
        elif(resultVal != "" and resultVal != None):
            print(resultVal, end=" ")

    def readOperation(self, lftAddress, rghtAddress, resultAddress, operatorNum):
        """
        Read input from the console and store it on the received memory address

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            resultAddress (integer): Memory address in which to store the readed data.
            operatorNum (None): None. Just to keep params simetry with all the functions.

        """
        # Ask for input to the user
        inputVal = input()

        self.execMemory.saveOnMemory(resultAddress, inputVal, True)

    def gotoQuad(self, lftAddress, rghtAddress, quadAddr, operatorNum):
        """
        Move the quads proccessing to the target quad

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            quadAddr (integer): Target quadruple number
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        self.countQuad = self.execMemory.getFromMemory(quadAddr) - 1

    def gotof(self, boolAddress, rghtAddress, quadAddr, operatorNum):
        """
        Move the quads proccessing to the target quad if the received boolean is false.

        Args:
            boolAddress (integer): Memory address to get the boolean.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            quadAddr (integer): Target quadruple number
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        boolVal = self.execMemory.getFromMemory(boolAddress)

        if(not boolVal):
            self.countQuad = self.execMemory.getFromMemory(quadAddr) - 1

    def eraQuad(self, lftAddress, rghtAddress, nameAddress, operatorNum):
        """
        Function to resever the needed memory to a function.

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            nameAddress (integer): Memory address where the function identifier is stored.
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        nameFunc = self.execMemory.getFromMemory(nameAddress)
        countDict = self.compiledCode['FuncTable'][nameFunc]['numVars']
        tempDict = self.compiledCode['FuncTable'][nameFunc]['numTempVars']
        self.execMemory.reserveContextMemmory(countDict, tempDict, 1)

    def paramQuad(self, argAddress, rghtAddress, nameAddress, operatorNum):
        """
        Function to resever the needed memory to a function.

        Args:
            argAddress (integer): ValftVal where the sent argvarghtVal is stored.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            nameAddress (integer): Memory address where the function identifier is stored.
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        argVal = self.execMemory.getFromMemory(argAddress)
        self.execMemory.sendParams(argAddress, argVal)

    def gosubQuad(self, lftAddress, rghtAddress, quadAddr, operatorNum):
        """
        Moves the quad processing to a function segment. Storing the current Control-Flow.

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            quadAddr (integer): Target quadruple number
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        self.execMemory.copyArgsToParms()
        self.execMemory.saveInstructionPointers(self.countQuad)
        self.countQuad = self.execMemory.getFromMemory(quadAddr) - 2

    def returnQuad(self, lftAddress, rghtAddress, globalAddress, operatorNum):
        """
        Store the returned value on the global address of the function.

        Args:
            lftAddress (integer): Local temporal address where is stored the returned value.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            globalAddress (integer): Memory address to store the returned value on the global scope.
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        returnVal = self.execMemory.getFromMemory(lftAddress)
        self.execMemory.saveOnMemory(globalAddress, returnVal)
        self.countQuad = self.execMemory.restoreInstructionPointer()

    def endFunction(self, lftAddress, rghtAddress, quadNum, operatorNum):
        """
        Finish the current flow control and goes back to the previous one.

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            quadNum (None): None. Just to keep params simetry with all the functions.
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """

        self.countQuad = self.execMemory.restoreInstructionPointer()

    def endProgram(self, lftAddress, rghtAddress, quadNum, operatorNum):
        """
        Break the while that read the quad list, ending the program.

        Args:
            lftAddress (None): None. Just to keep params simetry with all the functions.
            rghtAddress (None): None. Just to keep params simetry with all the functions.
            None. Just to keep params simetry with all the functions.
            operatorNum (None): None. Just to keep params simetry with all the functions.
        """
        self.countQuad = "EXIT"
        print('\n\n')


virMachine = VirtualMachine('./CompiledCode/test.obj')
virMachine.proccessQuads()
