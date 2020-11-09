class FunctionTable:

    def __init__(self):
        """
        Initializes the dictionary that works as a variable table
        """
        self.functionTable = {
            'global': {
                'returnType': 'void',
                'paramsNumber': 0,
                'paramsType': [],
                'varTable': {},
                'numVars': 0,
                'numQuad': 0
            }
        }

    def addNewFunction(self, funcName, returnType, objMemory=None):
        """
        Add new function data into the Function Table after making 
        the needed validations.

        Args:
            funcName (string): Function name
            returnType (string): Function return type

        Raises:
            Exception: If the function name is already being used
            Exception: If the function name is already being used in a variable
        """

        # Check if the function name is repeated
        if funcName in self.functionTable:
            raise Exception('Function "{}" already exists'.format(funcName))

        # Check if the function name is already used a as variable name
        for func in self.functionTable.values():
            if funcName in func['varTable']:
                raise Exception(
                    '"{}" already exists as a variable'.format(funcName))

        # If all the validations were passed, then add the function to the table
        self.functionTable[funcName] = {
            'returnType': returnType,
            'paramsNumber': 0,
            'paramsType': [],
            'varTable': {},
            'numVars': 0,
            'numQuad': 0
        }

        if (returnType != 'void'):
            # Get the direction address
            memAddress = objMemory.getGlobalAddress(returnType)

            # Add the variable to store the return value
            self.functionTable['global']['varTable'][funcName] = {
                'dataType': returnType,
                'size': 1,
                'flgArray': False,
                'dimensions': 1,
                'memoryAddress' : memAddress
            }


    def searchFunction(self, funcName):
        """
        Method to search a function

        Args:
            funcName (string): Function name

        Raises:
            Exception: If the function do not exists

        Returns:
            Dictionary: The dictionary with the function data
        """

        # Check on the functiontable
        if funcName  in self.functionTable:
            return self.functionTable[funcName]

        # If not, the function do no exists
        else:
            raise Exception(
                'The function "{}" has not been declared'.format(funcName))

    def addVariables(self, funcName, varList, flgParams=False, objMemory=None):
        """
        Adds the variables to its corresponding function

        Args:
            funcName (string): The function name
            varList (list): A list of tuples with the format (DataType, VarName)
            flgParams (bool, optional): Flag to know if the list are 
            parameters of the current function. Defaults to False.

        Raises:
            Exception: If the function is already used
            Exception: If the function name is already used in a globl variable
            Exception: If the function name is already used in a local variable
        """
        # If the variables are parameters, store the amount
        if(flgParams):
            self.functionTable[funcName]['paramsNumber'] = len(varList)

        # Add the amount of variables
        self.functionTable[funcName]['numVars'] += len(varList)

        for var in varList:
            flgArray = False
            dimensions = 1
            size = 1

            # Check if the variable name is already used as function name
            if var[1] in self.functionTable:
                raise Exception(
                    'The name "{}" is already used as a function'.format(var[1]))

            # Check if the variable already exists on the global or local scope
            elif var[1] in self.functionTable['global']['varTable']:
                raise Exception(
                    'Variable "{}" already exists as a global variable'.format(var[1]))
                    
            elif var[1] in self.functionTable[funcName]['varTable']:
                raise Exception(
                    'Variable "{}" has already been declared'.format(var[1]))

            # Check if the variable is array or matrix
            if (len(var) == 3):
                flgArray = True
                dimensions = var[2]

                # Calculate the size if it is a matrix
                if(type(var[2]) == tuple):
                    size = var[2][0] * var[2][1]

                # Or just store the array size
                else:
                    size = var[2]
                    
            if(funcName == 'global'):
                # Get the direction address
                memAddress = objMemory.getGlobalAddress(var[0])
            else:
                memAddress = objMemory.getVariableLocalAddress(var[0])
            
            # Add the variable to the function variables table
            self.functionTable[funcName]['varTable'][var[1]] = {
                'dataType': var[0],
                'size': size,
                'flgArray': flgArray,
                'dimensions': dimensions,
                'memoryAddress' : memAddress
            }

            # If the variables are parameters, store the data type also on another list
            if(flgParams):
                self.functionTable[funcName]['paramsType'].append(var[0])

        print(self.functionTable)

    def searchVariable(self, funcName, varName):
        """
        Method to search a variable on the global and local scope.

        Args:
            funcName (string): Function name
            varName (string): Wanted variable name

        Raises:
            Exception: If the variable do not exists

        Returns:
            Dictionary: The dictionary with the variable data
        """

        # Check on the global scope
        if varName in self.functionTable['global']['varTable']:
            return self.functionTable['global']['varTable'][varName]

        # Check on local function scope
        elif varName in self.functionTable[funcName]['varTable']:
            return self.functionTable[funcName]['varTable'][varName]

        # If not, the variable do no exists
        else:
            raise Exception(
                'The variable "{}" has not been declared'.format(varName))
