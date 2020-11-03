class Quadruple:
    """
    Class with the structure and representation of a Quadruple
    """
    def __init__(self, operator, lftOperand, rghtOperand, result):
        """
        Build the quadruple object

        Args:
            operator (integer): The integer that represent the operand or intermediate code
            lftOperand (int): Memory address that stores the left operand
            rghtOperand (integer): Memory address that stores the rigth operand
            result (integer): Memory address that stores the operation result
        """
        self.operator = operator
        self.lftOperand = lftOperand
        self.rghtOperand = rghtOperand
        self.result = result


    def __repr__(self):
        """
        Function that saves the format that is shown every time a quadruple is printed
        """
        return "({}, {}, {}, {})".format(self.operator, self.lftOperand, self.rghtOperand, self.result)