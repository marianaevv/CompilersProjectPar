class Quadruple:
    """
    Class with the structure and representation of a Quadruple
    """
    def __init__(self, intOperator, lftOperand, rghtOperand, dirResult):
        """
        Build the quadruple object

        Args:
            intOperator (integer): The integer that represent the operand or intermediate code
            lftOperand (int): Memory address that stores the left operand
            rghtOperand (integer): Memory address that stores the rigth operand
            dirResult (integer): Memory address that stores the operation result
        """
        self.intOperator = intOperator
        self.lftOperand = lftOperand
        self.rghtOperand = rghtOperand
        self.dirResult = dirResult


    def __repr__(self):
        """
        Function that saves the format that is shown every time a quadruple is printed
        """
        return "({}, {}, {}, {})".format(self.intOperator, self.lftOperand, self.rghtOperand, self.dirResult)