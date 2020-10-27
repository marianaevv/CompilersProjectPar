class SemanticCube:

    def __init__(self):
        """
        Constructor to load the semantic cube
        """
        self.__theCube = {
            'ArithmeticOps': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'char': 'error',
                    'bool': 'error'
                },
                'float': {
                    'float': 'float',
                    'int': 'float',
                    'char': 'error',
                    'bool': 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error'
                },
                'bool': {
                    'bool': 'error',
                    'int': 'error',
                    'float': 'error',
                    'char': 'error'
                }
            },

            'Division': {
                'int': {

                    'int': 'float',
                    'float': 'float',
                    'char': 'error',
                    'bool': 'error'
                },
                'float': {
                    'float': 'float',
                    'int': 'float',
                    'char': 'error',
                    'bool': 'error'
                },
                'char': {


                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error'
                },
                'bool': {
                    'bool': 'error',
                    'int': 'error',
                    'float': 'error',
                    'char': 'error'
                }
            },

            'ComparisonOps': {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'error',
                    'bool': 'error'
                },
                'float': {
                    'float': 'bool',
                    'int': 'bool',
                    'char': 'error',
                    'bool': 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error'
                },
                'bool': {

                    'bool': 'error',
                    'int': 'error',
                    'float': 'error',
                    'char': 'error'
                }
            },

            'ExcepComparisonOps': {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'error',
                    'bool': 'error'
                },
                'float': {
                    'float': 'bool',
                    'int': 'bool',
                    'char': 'error',
                    'bool': 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'bool',
                    'bool': 'error'
                },
                'bool': {
                    'bool': 'bool',
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                }
            },

            'LogicalOps': {
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error'
                },
                'float': {
                    'float': 'error',
                    'int': 'error',
                    'char': 'error',
                    'bool': 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error'
                },
                'bool': {
                    'bool': 'bool',
                    'int': 'error',
                    'float': 'error',
                    'char': 'error'

                }
            }
        }

    def verifyOperations(self, operator, leftOperand, rightOper):
        """
        Function that checks the type of the operations and return
        the result type of the operation or it is a invalid operation
        """
        ArithmeticOps = ['+', '-', '*', '%']
        Division = ['/']
        ComparisonOps = ['>=', '<=', '>', '<']
        ExcepComparisonOps = ['==', '!=']
        LogicalOps = ['|', '&']

        # To store the operator type
        operatorType = ''

        # Check the type of the operator
        if operator in ArithmeticOps:
            operatorType = 'ArithmeticOps'
        elif operator in Division:
            operatorType = 'Division'
        elif operator in ComparisonOps:
            operatorType = 'ComparisonOps'
        elif operator in ExcepComparisonOps:
            operatorType = 'ExcepComparisonOps'
        elif operator in LogicalOps:
            operatorType = 'LogicalOps'

        # Return the value the result type of the operation
        return self.__theCube[operatorType][leftOperand][rightOper]