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

        self.countTemporals = 0

        self.currentFunction = 'global'

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
        # Push the Goto quad
        self.stkQuadruples.append(Quadruple('GOTO', None, None, None))

        # Pop the jump quad
        falseLine = self.stkJumps.pop()

        # Append the new jump
        self.stkJumps.append(len(self.stkQuadruples) - 1)

        # Fill the GotoF
        self.stkQuadruples[falseLine].result = len(self.stkQuadruples)

    def endConditionQuad(self):
        # Pop the jump quad
        endLine = self.stkJumps.pop()

        # Fill the Goto
        self.stkQuadruples[endLine].result = len(self.stkQuadruples)

    def endWhileQuad(self):
        # Get the jump
        endLine = self.stkJumps.pop()

        # Get the return jump
        returnLine = self.stkJumps.pop()

        # Push the return quad
        self.stkQuadruples.append(Quadruple('GOTO', None, None, returnLine))

        # Fill the end line
        self.stkQuadruples[endLine].result = len(self.stkQuadruples)

    def returnFunctionQuad(self, funcName, returnType):
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
        self.stkQuadruples.append(Quadruple('ENDFUNC', None, None, None))
