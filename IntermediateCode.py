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

    def generateArithmeticQuadruple(self, groupOperators):
        """
        Function to generate the arithmetich operation quadruples

        Args:
            groupOperators (list): List with the arithmetich operators to look for

        Raises:
            Exception: If the operation is invalid
        """

        # If the last operator is a PLUS or MINUS..
        if(self.stkOperator):
            if(self.stkOperator[-1] in groupOperators):
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

                print(self.stkQuadruples)

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

        print(self.stkQuadruples)

    def generateAssignmentSingleQuad(self):

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

        print(self.stkQuadruples)
