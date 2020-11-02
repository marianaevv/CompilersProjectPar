class IntermediateCode:
    def __init__(self):
        # Needed stacks to the quadruples process
        self.stkOperand = list()
        self.stkType = list()
        self.stkOperator = list()
        self.stkJumps = list()

        self.currentFunction = 'global'
