class FunctionTable:

    def __init__(self):
        """
        Initializes the dictionary that works as a variable table
        """
        self.__functionTable = {}

    def addNewFunction(self, funcName, returnType, numParameters, typeParameters):
        """
        Add new function data into the Function Table after making 
        the needed validations.

        Args:
            funcName (string): Function name
            returnType (string): Function return type
            numParameters (integer): Number of parameters the function has
            typeParameters (list): List with the parameters data type
        """

        # Check if the function name is repeated
        if funcName in self.__functionTable:
            raise Exception('Function "{}" already exists'.format(funcName))

        # Check if the function name is already used a as variable name
        for func in self.__functionTable:
            if funcName in func['varTable']:
                raise Exception('"{}" already exists as a variable'.format(funcName))


        # If all the validations were passed, then add the function to the table
        self.__functionTable[funcName] = {
                                        'returnType': returnType,
                                        'numParameters': numParameters,
                                        'typeParameters': typeParameters,
                                        'varTable': {}
                                     }
