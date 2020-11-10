from json import JSONEncoder
import json

mapOperators = {
    '=': 1, '+': 2,
    '-': 3, '*': 4,
    '%': 5, '/': 6,
    '>=': 7, '<=': 8,
    '>': 9, '<': 10,
    '==': 11, '!=': 12,
    '|': 13, '&': 14,
    'WRITE': 15, 'READ': 16,
    'PARAM': 17, 'ERA': 18,
    'RETURN': 19, 'ENDFUNC': 20,
    'GOTO': 21, 'GOSUB': 22,
    'GOTOF': 23, 'END': 24,
}


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
        return "({}, {}, {}, {})".format(mapOperators[self.operator], self.lftOperand, self.rghtOperand, self.result)


class QuadrupleEncoder(JSONEncoder):
    """
    A specialised JSONEncoder that encodes Quadruple objects as JSON
    """

    def default(self, object):
        if isinstance(object, Quadruple):
            return object.__dict__
        else:
            # Call base class implementation which takes care of
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)
