import json


class ExecutionMemory():
    """
    Class to simulate the memory in execution and store the variables and functions returns.
    """

    def __init__(self):
        """
        Dictionaries to save values according to the context and the value type
        """
        self.ExecMemory = {
            # Global context
            0: {
                0: [],     # Integer stack
                1: [],     # Float stack
                2: [],     # Char stack
                3: [],     # Temporal Integer stack
                4: [],     # Temporal Float stack
                5: [],     # Temporal Char stack
                6: []      # Temporal Boolean stack
            },
            # Local context
            1: {
                0: [],     # Integer stack
                1: [],     # Float stack
                2: [],     # Char stack
                3: [],     # Temporal Integer stack
                4: [],     # Temporal Float stack
                5: [],     # Temporal Char stack
                6: []      # Temporal Boolean stack
            },
            # Constant context
            2: {
                0: [],     # Integer st°ack
                1: [],     # Float stack
                2: [],     # Char stack
                3: []      # String stack
            }
        }

        self.quadsList = []

    def addConstantMemory(self, constantsDir):
        """
        Load the constant values and add them to the memory

        Args:
            constantsDir (Direcotory): A dictionary with the constant values and their
                                       memory address.
        """

        # Add to memory each constant data
        for addr, value in constantsDir.items():
            self.saveOnMemory(int(addr), value)

    def addGlobalMemory(self, globalDict):
        """
        Load the global variables to the global memory

        Args:
            globalDict (Dictionary): A dict with the variable table from the global context
        """
        countDit = {
            "int" : 0,
            "float" : 0,
            "char": 0
        }

        # Per each variable...
        for value in globalDict.values():
            countDit[value['dataType']] += value['size']
        
        # Separate memory for each type of data
        self.ExecMemory[0][0] = [None] * countDit['int']
        self.ExecMemory[0][1] = [None] * countDit['float']
        self.ExecMemory[0][2] = [None] * countDit['char']

    def loadQuads(self, quadsList):
        """
        Set ready the list of quadruples. It cast the strings to real list of quads.

        Args:
            quadsList (list): List of strings with the quads
        """
        self.quadsList = tuple(map(lambda quad: json.loads(quad), quadsList))

    def getFromMemory(self, memoryAddr):
        """
        Function that receive a memory address and calculate the context and datatype 
        to be able to return the value on the position.

        Args:
            memoryAddr (integer | string): Memory address

        Returns:
            int | float | char | str: The searched value
        """

        # If the received memory address is a pointer...
        if(type(memoryAddr) is str):
            # Get the memory address that is pointed
            # and be able to return the actual searched address
            memoryAddr = self.getFromMemory(int(memoryAddr[2:]))

        # Check if the variable is on the global(0), local(1) or constant(2) context
        contextNum = (memoryAddr - 1000) // 27999
        modNum = (memoryAddr - 1000) % 28000

        # Check if the variable is an integer(0), float(1), char(2),
        # bool (3, temporal context) or string (3, constant context)
        typeData = modNum // 4000
        # Check the position of the varible on the Context[DataType] list
        positionNum = modNum % 4000

        # Return the wanted value
        return self.ExecMemory[contextNum][typeData][positionNum]

    def saveOnMemory(self, memoryAddr, value):
        """
        Function that receive a value and the memory address where the data is going to 
        be stored.

        Args:
            memoryAddr (integer | string):  Memory address
            value (int | float | char | str): Value to store
        """

        # Check if it is a pointer
        if(type(memoryAddr) is str):
            # Get the memory address that is pointed
            # and be able to store on the actual wanted address
            memoryAddr = self.getFromMemory(int(memoryAddr[2:]))

        # Check if the variable is on the global(0), local(1) or constant(2) context
        contextNum = (memoryAddr - 1000) // 27999
        modNum = (memoryAddr - 1000) % 28000

        # Check if the variable is an integer(0), float(1), char(2),
        # bool (3, temporal context) or string (3, constant context)
        typeData = modNum // 4000
        # Check the position of the varible on the Context[DataType] list
        positionNum = modNum % 4000

        # Check if the memory position already exists or not
        if(len(self.ExecMemory[contextNum][typeData]) <= positionNum):
            self.ExecMemory[contextNum][typeData].append(value)
        else:
            self.ExecMemory[contextNum][typeData][positionNum] = value
