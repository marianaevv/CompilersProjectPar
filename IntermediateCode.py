from SemanticCube import SemanticCube
from Quadruples import QuadrupleEncoder
from Quadruples import Quadruple
from Memory import Memory

import json

semanticCube = SemanticCube()
memoryObj = Memory()


class IntermediateCode:
    def __init__(self):
        # Needed stacks to the quadruples process
        self.stkOperand = list()
        self.stkType = list()
        self.stkOperator = list()
        self.stkJumps = list()
        self.stkQuadruples = list()
        self.stkIndexes = list()

        self.countTemporals = 1
        self.countReturns = 1

        self.currentFunction = 'global'

    def addFunctionToTable(self, funcTable, funcName, returnType):
        """
        To add a function to the Function Table while assigning 
        a Memory Address if it is not a void

        Args:
            funcTable (FunctionTableObj): A function table class
            funcName (string): Name of the function 
            returnType (string) : The function return type
        """
        funcTable.addNewFunction(funcName, returnType, memoryObj)

    def addVariablesToTables(self, funcTable, funcName, listVars, flgParams=False):
        """
        To add variables to the Function Table while assigning 
        a Memory Address

        Args:
            funcTable (FunctionTableObj): A function table class
            funcName (string): Name of the function 
            listVars (list): List with the tupples variables (TypeVar, Name)
            flgParams (bool | optional): Is a flag to know if the variables are 
                                         or not parameters.
        """
        funcTable.addVariables(funcName, listVars,
                               flgParams, memoryObj=memoryObj)

    def addIdentifiers(self, funcTable, varIden):
        """
        To add a variable identifier to the stacks after making sure
        the variable exists.

        Args:
            funcTable (FunctionTable Obj|): A function table object
            varIden (string): Variable's name
        """
        # Get the operand data type
        operandData = funcTable.searchVariable(
            self.currentFunction, varIden)

        # Add variable address and datatype to the stacks
        self.stkOperand.append(operandData['memoryAddress'])
        self.stkType.append(operandData['dataType'])

    def updateArrayAddress(self, arrayData, varName):
        """
        Make the needed quads to get the real indexed memory address from an array

        Args:
            arrayData (Dictionary): A dict with the data from a variable
            varName (string): String with the variable name

        Raises:
            Exception: If the variable is actually a matrix
        """

        # Check if the var is actually a matrix
        if(arrayData['numDimensions'] == 2):
            raise Exception('Variable {} is a matrix'.format(varName))

        # Get expresion as index
        index = self.stkOperand.pop()
        self.stkType.pop()

        # Make the verify quad
        self.stkQuadruples.append(
            Quadruple('VERIFY', index, arrayData['dimensions'], None))

        # Create memory address to store the sum of base address and index
        sumAddr = memoryObj.getMemoryAddress(
            'int', 1, self.currentFunction, True)

        # Make the sum to get the actual memory address
        self.stkQuadruples.append(
            Quadruple('SUMINDEX', index, arrayData['memoryAddress'], sumAddr))

        # Append the pointer to the stack
        self.stkOperand.append('->' + str(sumAddr))
        self.stkType.append(arrayData['dataType'])

    def updateMatrixAddress(self, arrayData):
        """
        Function to make the VERIFY quads and the sum to get the pointer to 
        the real indexed address from a matri

        Args:
            arrayData (Dictionary): A dict with the variable data
        """

        # Get expresion as index
        indexCol = self.stkOperand.pop()
        self.stkType.pop()
        indexRow = self.stkOperand.pop()
        self.stkType.pop()

        # Make the verify quad
        self.stkQuadruples.append(
            Quadruple('VERIFY', indexRow, arrayData['dimensions'][0], None))
        self.stkQuadruples.append(
            Quadruple('VERIFY', indexCol, arrayData['dimensions'][1], None))

        # Create memory address to store the sum of base address and index
        sumAddr = memoryObj.getMemoryAddress(
            'int', 1, self.currentFunction, True)
        multAddr = memoryObj.getMemoryAddress(
            'int', 1, self.currentFunction, True)

        # Make the sum to get the actual memory address
        self.stkQuadruples.append(
            Quadruple('MULTINDEX', indexRow, arrayData['dimensions'][1], sumAddr))
        self.stkQuadruples.append(
            Quadruple('SUMINDEX', indexCol, arrayData['memoryAddress'], multAddr))

        # Append the pointer to the stack
        self.stkOperand.append('->' + str(multAddr))
        self.stkType.append(arrayData['dataType'])

    def addConstantValue(self, cteValue):
        """
        To push the constant data type and its memory address to the
        stacks

        Args:
            cteValue (int | float | str): The constant value
        """
        # Append the constant data type
        if(type(cteValue).__name__ == 'str'):
            if(len(cteValue) == 1):
                self.stkType.append('char')
            else:
                self.stkType.append('str')
        else:
            self.stkType.append(type(cteValue).__name__)

        # Get the memory address
        memAddress = memoryObj.getMemoryAddressToConstant(self.stkType[-1],
                                                          cteValue)

        # Push the memory address
        self.stkOperand.append(memAddress)

    def generateGOTOMain(self):
        """
        Generate the quad to go to the main
        """
        self.stkQuadruples.append(Quadruple('GOTO', None, None, None))

    def fillGOTOMain(self):
        """
        Fill the GOTO Main quad
        """
        # Get the initial quad
        self.stkQuadruples[0].result = len(self.stkQuadruples)

    def endQuad(self):
        """
        Generate the END Quad
        """
        self.stkQuadruples.append(Quadruple('END', None, None, None))

    def generateOperatorQuadruple(self, funcName, groupOperators=None, flgArithmetic=True):
        """
        Function to generate the operation quadruples

        Args:
            funcName (string): The name of the function (To generate the temporal memory space)
            groupOperators (list, optional): List with the arithmetic operators to look for
            flgArithmetic (bool, optional): If the quadruple is going to be a arithmetic operation or not

        Raises:
            Exception: If the operation is invalid
        """

        # Flag to know if is time to push a quadruple
        insertQuad = False

        # If it is a arithmetic operator, make the validations...
        if(flgArithmetic):
            # Check that there are operands and if the
            # if the las operator is on the searched operators group
            if(self.stkOperator):
                if(self.stkOperator[-1] in groupOperators):
                    insertQuad = True

        # Or just push the quad if it is a logical
        # or relational operator
        else:
            insertQuad = True

        if(insertQuad):
            # Pop the last operands
            rgtOperand = self.stkOperand.pop()
            rgtOpndType = self.stkType.pop()
            lftOperand = self.stkOperand.pop()
            lftOpndType = self.stkType.pop()

            # Pop the operator
            operator = self.stkOperator.pop()

            # Validate the operation
            resultType = semanticCube.verifyOperations(operator,
                                                       lftOpndType, rgtOpndType)

            # Raise exception if it is a invalid operation
            if(resultType == "error"):
                raise Exception("Invalid operation {} between {} and {}".format(
                    operator, lftOpndType, rgtOpndType))

            # Calculate the memory address
            resultAddress = memoryObj.getMemoryAddress(resultType, 1,
                                                       self.currentFunction, True)

            # Push the result and it's type
            self.stkOperand.append(resultAddress)
            self.stkType.append(resultType)

            # Push the quadruple
            self.stkQuadruples.append(Quadruple(operator, lftOperand,
                                                rgtOperand, resultAddress))

    def generateAssignmentQuad(self):
        """
        Function to generate the quadruplo of assignments

        Raises:
            Exception: If the operands types are different
        """
        # Pop the last operands
        rgtOperand = self.stkOperand.pop()
        rgtOpndType = self.stkType.pop()
        lftOperand = self.stkOperand.pop()
        lftOpndType = self.stkType.pop()

        # Pop the operator
        operator = self.stkOperator.pop()

        # Raise exception if it is a invalid operation
        if(lftOpndType != rgtOpndType):
            raise Exception("Cannot asign a {} to a {}".format(rgtOpndType,
                                                               lftOpndType))

        if(operator == '='):
            # Push the quadruple
            self.stkQuadruples.append(Quadruple(operator,
                                                rgtOperand, None, lftOperand))

        elif(operator == '+='):
            # Push the quadruple
            self.stkQuadruples.append(Quadruple('+',
                                                lftOperand, rgtOperand, lftOperand))

        elif(operator == '-='):
            # Push the quadruple
            self.stkQuadruples.append(Quadruple('-',
                                                lftOperand, rgtOperand, lftOperand))

    def generateAssignmentSingleQuad(self):
        """
        Generate the quadruple when using the operators ++ and --

        Raises:
            Exception: If the variables are not Integers or Floats
        """

        # Pop the last operands
        lftOperand = self.stkOperand.pop()
        lftOpndType = self.stkType.pop()

        # Pop the operator
        operator = self.stkOperator.pop()

        # Raise exception if it is a invalid operation
        if(lftOpndType not in ['int', 'float']):
            if(operator == '++'):
                actionName = 'increment'
            else:
                actionName = 'decrement'
            raise Exception("Cannot {} a {}".format(actionName, lftOpndType))

        if(operator == '++'):
            # Push the quadruple
            self.stkQuadruples.append(Quadruple('+',
                                                lftOperand, 1, lftOperand))

        elif(operator == '--'):
            # Push the quadruple
            self.stkQuadruples.append(Quadruple('-',
                                                lftOperand, 1, lftOperand))

    def generateConditionQuad(self):
        """
        Generate the GOTOF quadruple when start a IF/Then statement

        Raises:
            Exception: If the expression inside the parenthesis is not a bool
        """
        # Pop the last operands
        resultValue = self.stkOperand.pop()
        resultType = self.stkType.pop()

        # Check the result data type
        if(resultType != 'bool'):
            raise Exception(
                "Invalid operation, the condition need to result on a bool.")

        # Push the quadruple
        self.stkQuadruples.append(Quadruple('GOTOF', resultValue, None, None))

        # Add the jump quad to come back later
        self.stkJumps.append(len(self.stkQuadruples) - 1)

    def elseConditionQuad(self):
        """
        Function to generate the GOTO quad when uing a else statement
        Also, filling the past GOTOF quad
        """
        # Push the Goto quad
        self.stkQuadruples.append(Quadruple('GOTO', None, None, None))

        # Pop the jump quad
        falseLine = self.stkJumps.pop()

        # Append the new jump
        self.stkJumps.append(len(self.stkQuadruples) - 1)

        # Fill the GotoF
        self.stkQuadruples[falseLine].result = len(self.stkQuadruples)

    def endConditionQuad(self):
        """
        Function to fill the GOTOF or GOTO quads from a IF-THEN ELSE
        """
        # Pop the jump quad
        endLine = self.stkJumps.pop()

        # Fill the Goto
        self.stkQuadruples[endLine].result = len(self.stkQuadruples)

    def endWhileQuad(self):
        """
        Generate the GOTO Quad when starting a While
        """
        # Get the jump
        endLine = self.stkJumps.pop()

        # Get the return jump
        returnLine = self.stkJumps.pop()

        # Push the return quad
        self.stkQuadruples.append(Quadruple('GOTO', None, None, returnLine))

        # Fill the end line
        self.stkQuadruples[endLine].result = len(self.stkQuadruples)

    def returnFunctionQuad(self, funcName, returnType):
        """
        Generate the RETURN Quad of the return statement.
        Making the needed validation.

        Args:
            funcName (string): Name of the function the return is inside
            returnType (string): Data type of the returned value

        Raises:
            Exception: If the function is void and has a return
            Exception: If the returned data type is different than the expected
        """
        actualType = self.stkType.pop()

        # If the function is void and have a return
        if(returnType == 'void'):
            raise Exception(
                'Function "{}" is void and does not need a return'.format(funcName))

        # If the returned value is different from the function return type
        if(returnType != actualType):
            raise Exception(
                'Error trying to return a {} when function "{}" returns a {}'.format(
                    actualType, funcName, returnType))

        # Push the returned value
        self.stkQuadruples.append(
            Quadruple('RETURN', None, None, self.stkOperand.pop()))

    def endFunctionQuad(self):
        """
        Generate the ENDFUNC quad
        """
        self.stkQuadruples.append(Quadruple('ENDFUNC', None, None, None))

        # Reset local memory address
        memoryObj.resetLocalCounters()

    def eraQuad(self, numVars):
        """
        Generate the ERA quad when calling a function

        Args:
            numVars (integert): Number of variables that the function has
        """
        self.stkQuadruples.append(Quadruple('ERA', None, None, numVars))

    def argumentQuad(self, varType, argNum):
        """
        Generate the quad per argument sended to a function. Also checks that
        the user do not send more thant the expécted amount.

        Args:
            varType (string): Data type of the expected argument
            argNum (integer): Number of the expected argument

        Raises:
            Exception: If there are more arguments than the called function needs
        """
        # Pop the arg value
        argValue = self.stkOperand.pop()
        argType = self.stkType.pop()

        # Validate the data type
        if(varType != argType):
            raise Exception(
                "The argument is {} but needs to be {}".format(argType, varType))

        # Push the quadruple
        self.stkQuadruples.append(Quadruple('PARAM', argValue, None, argNum))

    def gosubQuad(self, returnType, numQuad, funcName, returnAddress):
        """
        Generate the GOSUB quad when calling a function

        Args:
            returnType (string): Data type the called functon returns
            numQuad (integer): The number of the quadrupĺe where the called function starts
            funcName (string): Name of the current function to know if the memory address
                               needs to be global or local.
            returnAddress (integer): Memory address of the return value from the called function
        """
        if(returnType == 'void'):
            returnDir = None
        else:
            returnDir = memoryObj.getMemoryAddress(returnType, 1,
                                                   self.currentFunction, True)

            self.stkType.append(returnType)
            self.stkOperand.append(returnDir)

        # Generate GOSUB Quad to execute a function and update the return data
        self.stkQuadruples.append(Quadruple('GOSUB', None, None, numQuad))

        # Generate assignation quad to store the returned value in a termporal value
        if(returnAddress != None):
            self.stkQuadruples.append(
                Quadruple('=', returnAddress, None, returnDir))

    def writeQuad(self):
        """
        Generate the quadruple of the WRITE function
        """
        # Get the value to print
        toWriteVal = self.stkOperand.pop()
        self.stkType.pop()

        # Push the quad
        self.stkQuadruples.append(Quadruple('WRITE', None, None, toWriteVal))

    def readQuad(self):
        """
        Generate the quadruple of the READ function
        """
        # Get were to store the data
        toReadDir = self.stkOperand.pop()
        self.stkType.pop()

        # Push the quad
        self.stkQuadruples.append(Quadruple('READ', None, None, toReadDir))

    def generateVControlQuad(self, funcName):
        """
        Generate the Quadruple where the VControl get the value

        Args:
            funcName (string): Name of the current function to know if the memory address
                               needs to be global or local.
        """

        # Pop the memory address of the ID
        expOperand = self.stkOperand[-1]

        # Generate the memory address of the VControl
        VControl = memoryObj.getMemoryAddress(
            'int', 1, self.currentFunction, True)

        # Generate the quad
        self.stkQuadruples.append(Quadruple('=', expOperand, None, VControl))

        # Push the VC memory address
        self.stkOperand.append(VControl)
        self.stkType.append('int')

    def generateVCVFComparisonQuad(self, funcName):
        """
        Generate the quads where the VControl and VFinal are compared

        Args:
            funcName (string): Name of the current function to know if the memory address
                               needs to be global or local.

        Raises:
            Exception: If the goal expression is not an integer
        """

        # Checks that the goal expresion is a integer
        expType = self.stkType.pop()
        if(expType != 'int'):
            raise Exception("The final expression on a FOR must be an integer")

        # Pop the fianl expresion
        expOperand = self.stkOperand.pop()

        # Generate the memory address of the VFinal
        VFinal = memoryObj.getMemoryAddress(
            'int', 1, self.currentFunction, True)

        # Generate memory for the temporal boolean
        tempBoolean = memoryObj.getMemoryAddress(
            'int', 1, self.currentFunction, True)

        # Generate quads
        self.stkQuadruples.append(Quadruple('=', expOperand, None, VFinal))
        self.stkQuadruples.append(Quadruple('<', self.stkOperand[-1], VFinal,
                                            tempBoolean))

        # Push the jump quad
        self.stkJumps.append(len(self.stkQuadruples) - 1)

        # Generate the GOTOF quad
        self.stkQuadruples.append(Quadruple('GOTOF', tempBoolean, None, None))

        # Push the jump quad
        self.stkJumps.append(len(self.stkQuadruples) - 1)

    def fillForQuad(self):
        """
        Generate the last quads of the FOR and the GOTO if the condition 
        still does not meet. Also fill the previous GOTOF quad.
        """

        # Pop the memory address
        VControl = self.stkOperand.pop()
        IDMemory = self.stkOperand.pop()
        self.stkType.pop()
        self.stkType.pop()

        # Generate the update quad
        self.stkQuadruples.append(Quadruple('+', VControl, 1, VControl))
        self.stkQuadruples.append(Quadruple('=', VControl, None, IDMemory))

        # Get jumps
        endFOR = self.stkJumps.pop()
        returnFOR = self.stkJumps.pop()

        # Generate the GOTO quad
        self.stkQuadruples.append(Quadruple('GOTO', None, None, returnFOR))

        # Fill the jump quad
        self.stkQuadruples[endFOR].result = len(self.stkQuadruples)

    def compileCode(self, funcTable, programName):
        """
        Function to write the object code file after compile the input code.
        The Quadruples, constant values and function table are dumped into a JSON to facilate the reading for the
        virtual machine.

        Args:
            funcTable (FunctionTable Obj): The function table object
            programName (string): Name of the input program
        """

        # Switch keys to values and viciversa, to have the memory addresses as keys on
        # the dictionary
        constantValues = {value: key for key,
                          value in memoryObj.constantValues.items()}

        # Encode the quadruple list
        encodedQuads = list(
            map(lambda Quad: QuadrupleEncoder().encode(Quad), self.stkQuadruples))

        compiledCode = {
            "FuncTable": funcTable.functionTable,
            "ConstantValues": constantValues,
            "Quadruples": encodedQuads
        }

        # Dump the compiled data into a JSON
        with open("{}.json".format(programName), 'w') as compiledFile:
            json.dump(compiledCode, compiledFile, separators=(',', ':'))
