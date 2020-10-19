ArithmeticOps = ['+','-','*','%']
ExceptionOps = ['/']
ComparisonOps = ['>=','<=','>','<']
ExceptionComparisonOps = ['==', '!=']
LogicalOps = ['|', '&']

def arithmeticOperators(leftOper, rightOper):
    for operator in ArithmeticOps:
        if (leftOper == 'int' and rightOper 'int')
        return 'int'
        elif (leftOper == 'int' and rightOper 'float')
        return 'float'
        elif(leftOper == 'int' and rightOper 'char')
        return 'error'
        elif(leftOper == 'int' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'float' and rightOper 'float')
        return 'float'
        elif(leftOper == 'float' and rightOper 'int')
        return 'float'
        elif(leftOper == 'float' and rightOper 'char')
        return 'error'
        elif(leftOper == 'float' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'char' and rightOper 'int')
        return 'error'
        elif(leftOper == 'char' and rightOper 'float')
        return 'error'
        elif(leftOper == 'char' and rightOper 'char')
        return 'error'
        elif(leftOper == 'char' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'int')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'float')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'char')
        return 'error'

def exceptionOperator(leftOper, rightOper):
    for operator in ExceptionOps:
        if (leftOper == 'int' and rightOper 'int')
        return 'float'
        elif (leftOper == 'int' and rightOper 'float')
        return 'float'
        elif(leftOper == 'int' and rightOper 'char')
        return 'error'
        elif(leftOper == 'int' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'float' and rightOper 'float')
        return 'float'
        elif(leftOper == 'float' and rightOper 'int')
        return 'float'
        elif(leftOper == 'float' and rightOper 'char')
        return 'error'
        elif(leftOper == 'float' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'char' and rightOper 'int')
        return 'error'
        elif(leftOper == 'char' and rightOper 'float')
        return 'error'
        elif(leftOper == 'char' and rightOper 'char')
        return 'error'
        elif(leftOper == 'char' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'int')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'float')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'char')
        return 'error'

def comparisonOperators(leftOper, rightOper):
    for operator in ComparisonOps:
        if (leftOper == 'int' and rightOper 'int')
        return 'bool'
        elif (leftOper == 'int' and rightOper 'float')
        return 'bool'
        elif(leftOper == 'int' and rightOper 'char')
        return 'error'
        elif(leftOper == 'int' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'float' and rightOper 'float')
        return 'bool'
        elif(leftOper == 'float' and rightOper 'int')
        return 'bool'
        elif(leftOper == 'float' and rightOper 'char')
        return 'error'
        elif(leftOper == 'float' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'char' and rightOper 'int')
        return 'error'
        elif(leftOper == 'char' and rightOper 'float')
        return 'error'
        elif(leftOper == 'char' and rightOper 'char')
        return 'error'
        elif(leftOper == 'char' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'int')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'float')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'char')
        return 'error'

def exceptionComparisonOperators(leftOper, rightOper):
    for operator in ExceptionComparisonOps:
        if (leftOper == 'int' and rightOper 'int')
        return 'bool'
        elif (leftOper == 'int' and rightOper 'float')
        return 'bool'
        elif(leftOper == 'int' and rightOper 'char')
        return 'error'
        elif(leftOper == 'int' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'float' and rightOper 'float')
        return 'bool'
        elif(leftOper == 'float' and rightOper 'int')
        return 'bool'
        elif(leftOper == 'float' and rightOper 'char')
        return 'error'
        elif(leftOper == 'float' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'char' and rightOper 'int')
        return 'error'
        elif(leftOper == 'char' and rightOper 'float')
        return 'error'
        elif(leftOper == 'char' and rightOper 'char')
        return 'bool'
        elif(leftOper == 'char' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'bool')
        return 'bool'
        elif(leftOper == 'bool' and rightOper 'int')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'float')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'char')
        return 'error'

def exceptionComparisonOperators(leftOper, rightOper):
    for operator in LogicalOps:
        if (leftOper == 'int' and rightOper 'int')
        return 'error'
        elif (leftOper == 'int' and rightOper 'float')
        return 'error'
        elif(leftOper == 'int' and rightOper 'char')
        return 'error'
        elif(leftOper == 'int' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'float' and rightOper 'float')
        return 'error'
        elif(leftOper == 'float' and rightOper 'int')
        return 'error'
        elif(leftOper == 'float' and rightOper 'char')
        return 'error'
        elif(leftOper == 'float' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'char' and rightOper 'int')
        return 'error'
        elif(leftOper == 'char' and rightOper 'float')
        return 'error'
        elif(leftOper == 'char' and rightOper 'char')
        return 'error'
        elif(leftOper == 'char' and rightOper 'bool')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'bool')
        return 'bool'
        elif(leftOper == 'bool' and rightOper 'int')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'float')
        return 'error'
        elif(leftOper == 'bool' and rightOper 'char')
        return 'error'