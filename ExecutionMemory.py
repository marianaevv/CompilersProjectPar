import json


class ExecutionMemory():
    """
    Class to simulate the memory in execution and store the variables and functions returns.
    """

    def __init__(self):
        """
        Dictionaries to save values according to the context and the value type
        """
        self.__localContext = {
            0: [],     # Integer stack
            1: [],     # Float stack
            2: [],     # Char stack
            3: [],     # Temporal Integer stack
            4: [],     # Temporal Float stack
            5: [],     # Temporal Char stack
            6: []      # Temporal Boolean stack
        }

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
            1: self.__localContext.copy(),

            # Constant context
            2: {
                0: [],     # Integer st°ack
                1: [],     # Float stack
                2: [],     # Char stack
                3: []      # String stack
            }
        }

        self.quadsList = []
        self.instrucPointers = []
        self.paramsList = []

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

    def reserveContextMemmory(self, contextDict, contextNum):
        """
        Load the global variables to the global memory

        Args:
            contextDict (Dictionary): Dictionary with counters for each type of data that the function needs
            contextNum (integer): A number 0 if it is to the global memory or 1 if it is local
        """
        if(contextNum == 0):
            self.ExecMemory[0][0] = [None] * contextDict['int']
            self.ExecMemory[0][1] = [None] * contextDict['float']
            self.ExecMemory[0][2] = [None] * contextDict['char']

        else:
            self.paramsList = []
            copyLocalMem = self.__localContext.copy()

            # Separate memory for each type of data
            copyLocalMem[0] = [None] * contextDict['int']
            copyLocalMem[1] = [None] * contextDict['float']
            copyLocalMem[2] = [None] * contextDict['char']

            self.instrucPointers.append(copyLocalMem)

    def sendParams(self, currentAddr, value):
        # Get data type
        _, dataType, _ = self.getPositionMemory(currentAddr)

        # Add it to the list
        self.paramsList.append({'dataType': dataType, 'value': value})

    def copyArgsToParms(self):
        countDict = {
            0: 0,
            1: 0,
            2: 0
        }

        for arg in self.paramsList:
            self.instrucPointers[-1][arg['dataType']
                                     ][countDict[arg['dataType']]] = arg['value']
            countDict[arg['dataType']] += 1

    def loadQuads(self, quadsList):
        """
        Set ready the list of quadruples. It cast the strings to real list of quads.

        Args:
            quadsList (list): List of strings with the quads
        """
        self.quadsList = tuple(map(lambda quad: json.loads(quad), quadsList))

    def getPositionMemory(self, memoryAddr):
        """
        Calculate the context, data type and position where a memory address 
        belongs.

        Args:
            memoryAddr (int | str): The memery address or a pointer

        Returns:
            integer: Number of context: Global(0), Local(1) or Constant(2)
            integer: Number of data type integer(0), float(1), char(2),
                     bool (3, temporal context) or string (3, constant context)
            integer: Position in the corresponding stack
        """
        # Check if the variable is on the global(0), local(1) or constant(2) context
        contextNum = (memoryAddr - 1000) // 27999
        modNum = (memoryAddr - 1000) % 28000

        # Check if the variable is an integer(0), float(1), char(2),
        # bool (3, temporal context) or string (3, constant context)
        dataType = modNum // 4000
        # Check the position of the varible on the Context[DataType] list
        positionNum = modNum % 4000

        return contextNum, dataType, positionNum

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

        # Calculate the corresponding position
        contextNum, dataType, positionNum = self.getPositionMemory(memoryAddr)

        # Return the wanted value
        return self.ExecMemory[contextNum][dataType][positionNum]

    def saveOnMemory(self, memoryAddr, value, toCast=False):
        """
        Function that receive a value and the memory address where the data is going to 
        be stored.

        Args:
            memoryAddr (integer | string):  Memory address
            value (int | float | char | str): Value to store
            toCast (bool, optional): Flag to know if it is necessary to cast the value
        """
        # Check if it is a pointer
        if(type(memoryAddr) is str):
            # Get the memory address that is pointed
            # and be able to store on the actual wanted address
            memoryAddr = self.getFromMemory(int(memoryAddr[2:]))

        # Calculate the corresponding position
        contextNum, dataType, positionNum = self.getPositionMemory(memoryAddr)

        # Check if it is necessary to cast the data
        if(toCast):
            toCast = {
                # Global context
                0: int,
                1: float,
                2: str,
                3: "integer",
                4: "float",
                5: "char"
            }

            # Try to cast the value to the corresponding data type
            try:
                value = toCast[dataType](value)

            # Catch and raise the need value error exception
            except ValueError:
                raise ValueError(
                    "The input should be a(n) {}".format(toCast[dataType+3]))

        # Check if the memory position already exists or not
        if(len(self.ExecMemory[contextNum][dataType]) <= positionNum):
            self.ExecMemory[contextNum][dataType].append(value)
        else:
            self.ExecMemory[contextNum][dataType][positionNum] = value

    def saveInstructionPointers(self, instrucPointer):
        """
        Function to save the current Instruction Pointer and the current local mememory
        when a function is called.

        Args:
            instrucPointer (integer): Number of the current quad.
        """
        newLocalMen = self.instrucPointers.pop()

        # Make a dictionary with the current local memory and the pointer
        currentMemory = {
            "Memory": self.ExecMemory[1].copy(),
            "IP": instrucPointer
        }

        # Store the current flow control
        self.instrucPointers.append(currentMemory)

        # Change the local context
        self.ExecMemory[1] = newLocalMen

    def restoreInstructionPointer(self):
        """
        Function to restore the control to the previous function.
        And loading it's local memory.

        Returns:
            integer: Instruction pointer to the previous control flow.
        """
        prevControl = self.instrucPointers.pop()
        self.ExecMemory[1] = prevControl['Memory']

        return prevControl['IP']
