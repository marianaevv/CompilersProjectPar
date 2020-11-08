from SemanticCube import SemanticCube
from Quadruples import Quadruple

semanticCube = SemanticCube()


class IntermediateCode:
    def __init__(self):
        # Needed stacks to the quadruples process
        self.stkOperand = list()
        self.stkType = list()
        self.stkOperator = list()
        self.stkJumps = list()
        self.stkQuadruples = list()

        self.countTemporals = 1
        self.countReturns = 1

        self.currentFunction = 'global'


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
        

    def generateOperatorQuadruple(self, groupOperators=None, flgArithmetic=True):
        """
        Function to generate the operation quadruples

        Args:
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
            resultType = semanticCube.verifyOperations(
                operator, lftOpndType, rgtOpndType)

            # Raise exception if it is a invalid operation
            if(resultType == "error"):
                raise Exception("Invalid operation {} between {} and {}".format(
                    operator, lftOpndType, rgtOpndType))

            # If the operation is valid, generate the memory direction to the result
            resultDirection = 'T' + str(self.countTemporals)
            self.countTemporals += 1

            # Push the result and it's type
            self.stkOperand.append(resultDirection)
            self.stkType.append(resultType)

            # Push the quadruple
            self.stkQuadruples.append(
                Quadruple(operator, lftOperand, rgtOperand, resultDirection))

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
            raise Exception("Cannot asign a {} to a {}".format(
                rgtOpndType, lftOpndType))

        if(operator == '='):
            # Push the quadruple
            self.stkQuadruples.append(
                Quadruple(operator, rgtOperand, None, lftOperand))

        elif(operator == '+='):
            # Push the quadruple
            self.stkQuadruples.append(
                Quadruple('+', lftOperand, rgtOperand, lftOperand))

        elif(operator == '-='):
            # Push the quadruple
            self.stkQuadruples.append(
                Quadruple('-', lftOperand, rgtOperand, lftOperand))

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
            self.stkQuadruples.append(
                Quadruple('+', lftOperand, 1, lftOperand))

        elif(operator == '--'):
            # Push the quadruple
            self.stkQuadruples.append(
                Quadruple('-', lftOperand, 1, lftOperand))

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

    def gosubQuad(self, returnType, numQuad):
        """
        Generate the GOSUB quad when calling a function

        Args:
            returnType (string): Data type the called functon returns
            numQuad (integer): The number of the quadrupĺe where the called function starts
        """
        if(returnType == 'void'):
            returnVal = None
        else:
            returnVal = 'R' + str(self.countReturns)

            self.stkType.append(returnType)
            self.stkOperand.append(returnVal)

        self.stkQuadruples.append(Quadruple('GOSUB', returnVal, None, numQuad))

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

    def generateVControlQuad(self):
        """
        Generate the Quadruple where the VControl get the value
        """

        # Pop the memory direction of the ID
        expOperand = self.stkOperand[-1]

        # Generate the memory direction of the VControl
        VControl = "VC"

        # Generate the quad
        self.stkQuadruples.append(Quadruple('=', expOperand, None, VControl))

        # Push the VC memory direction
        self.stkOperand.append(VControl)
        self.stkType.append('int')

    def generateVCVFComparisonQuad(self):
        """
        Generate the quads where the VControl and VFinal are compared

        Raises:
            Exception: If the goal expression is not an integer
        """

        # Checks that the goal expresion is a integer
        expType = self.stkType.pop()
        if(expType != 'int'):
            raise Exception("The final expression on a FOR must be an integer")

        # Pop the fianl expresion
        expOperand = self.stkOperand.pop()

        print(self.stkOperand)

        # Generate the memory direction of the VFinal
        VFinal = "VF"

        # Generate memory for the temporal boolean
        tempBoolean = "T" + str(self.countTemporals)
        self.countTemporals += 1

        # Generate quads
        self.stkQuadruples.append(Quadruple('=', expOperand, None, VFinal))
        self.stkQuadruples.append(Quadruple('<', self.stkOperand[-1], VFinal, tempBoolean))

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

        # Pop the memory directions
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
