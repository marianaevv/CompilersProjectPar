import json
from ExecutionMemory import ExecutionMemory

class VirtualMachine():
    """
    Class to simula a computer executing a compiled program
    """
    
    def __init__(self, inputName):

        # Instance of the virtual memory
        virtMemory = ExecutionMemory()

        # Open file with the compiled code
        with open(inputName, 'r') as inputFile:
            # Load the JSON
            compiledCode = json.load(inputFile)

            # Load the constant and global variables
            virtMemory.addConstantMemory(compiledCode['ConstantValues'])
            virtMemory.addGlobalMemory(compiledCode['FuncTable']['global']['varTable'])
            virtMemory.loadQuads(compiledCode['Quadruples'])


    # def proccessQuads():

virMachine = VirtualMachine('patito3.obj')