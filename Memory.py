class Memory:
    def __init__(self):
        """
        Global Memory - Starts at 1000 and ends at 16999
        Temporal Global Memory - 17000 and ends at 32999
        Local Memory - Starts at 33000 and ends at 48999
        Temporal Local Memory - 49000 and ends at 64999
        Constant Memory - Starts at 65000 and ends at 84999

        Each memory context (global, local or constant) will be divided into types context (int, bool, float, char, str)
        avoiding the use of casting values. Also, the contexts global and local will have a temporal version.
        """

        self.baseAddress = {
            1: 1000,
            2: 33000,
            3: 65000
        }

        self.baseTemporalAddress = {
            1: 17000,
            2: 49000
        }

        self.dataTypeRangeStart = {
            'int': 0,
            'float': 4000,
            'char': 8000,
            'bool': 12000,
            'str': 16000
        }

        self.countPositions = {
            1: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            2: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            3: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'str': 0
            }
        }

        self.countTemporalPositions = {
            1: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            2: {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            }
        }

        self.constantValues = {}

    def getMemoryAddress(self, varType, size, scope, flgTemp):
        """
        Function to get the memory address for a variable

        Args:
            varType (string): The data type of the variable [int | float | char | string]
            size (integer): Size of the vairibale
            scope (string): Name of the current function
            flgTemp (bool): To know it is a teporal varible

        Returns:
            [integer]: Assigned memory address
        """

        # Define the scope integer
        if(scope == 'global'):
            scope = 1
        else:
            scope = 2

        # Check if it's a temporal variable or not
        if(not flgTemp):
            # Calculate the address using the non temporal ranges
            memAddress = self.baseAddress[scope] + self.dataTypeRangeStart[varType] + \
                self.countPositions[scope][varType]

            self.countPositions[scope][varType] += size

        else:
            # Calculate the address using the termporal ranges
            memAddress = self.baseTemporalAddress[scope] + self.dataTypeRangeStart[varType] + \
                self.countTemporalPositions[scope][varType]

            self.countTemporalPositions[scope][varType] += size

        return memAddress

    def getMemoryAddressToConstant(self, dataType, value):
        """
        Function to get the memory address for a constant value. Checks if the constant already 
        exists and return the assigned address or calculate a new one.

        Args:
            dataType (string): The data type of the constant [int | float | char | string]
            value (int | float | str): Value of the constant

        Returns:
            [integer]: Assigned memory address
        """

        # If the constant already exists, return the address
        if(value in self.constantValues):
            return self.constantValues[value]

        else:
            # Calculate the address to a constant value
            memAddress = self.baseAddress[3] + self.dataTypeRangeStart[dataType] + \
                self.countPositions[3][dataType]

            # Store the new address
            self.constantValues[value] = memAddress

            # Increase the counter
            self.countPositions[3][dataType] += 1

            return memAddress

    def resetLocalCounters(self):
        """
        Reset to 0 the counters of the local context every time a ENDFUC quad is pushed
        """
        self.countPositions[2] = {
            'int': 0,
            'float': 0,
            'char': 0,
            'bool': 0
        }

        self.countTemporalPositions[2] = {
            'int': 0,
            'float': 0,
            'char': 0,
            'bool': 0
        }
