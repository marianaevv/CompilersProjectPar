import json

class ExecutionMemory():
    """
    Class to simulate the memory in execution and store the variables and functions returns.
    """

    def __init__(self):
        """
        Dictionaries to save values according to the context and the value type
        """
        self.globalMemory = {}
        self.localMemory = {}
        self.constantsMemory = {}
        self.quadsList = []

    def addConstantMemory(self, constantsDir):
        """
        Load the constant values to memory and flip the hash to be able to access to the constant
        using the memory address

        Args:
            constantsDir (Direcotory): A dictionary with the constant values and their
                                       memory address.
        """

        # Make the memory address the key and the variable value the has value
        self.constantsMemory = {int(value): key for key, value in
                                constantsDir.items()}

    def addGlobalMemory(self, globalDict):
        """
        Load the global variables to the global memory

        Args:
            globalDict (Dictionary): A dict with the variable table from the global context
        """
        # Per each variable...
        for _, value in globalDict.items():
            # Store the memory address 
            globalAddr = value['memoryAddress']
            # Delete the memory address from the dict
            del value['memoryAddress']

            # Add the dict to the global memory
            self.globalMemory[globalAddr] = value


    def loadQuads(self, quadsList):
        """
        Set ready the list of quadruples. It cast the strings to real list of quads.

        Args:
            quadsList (list): List of strings with the quads
        """
        self.quadsList = tuple(map(lambda quad: json.loads(quad), quadsList))