# A00513571 Mariana Villegas
# A00820323 Noé Campos

import ply.lex as lex
import ply.yacc as yacc
import sys

from IntermediateCode import IntermediateCode
from FunctionTable import FunctionTable

# Initialize the helper objects
funcTable = FunctionTable()
interCode = IntermediateCode()

# Flags to make certain validations
flgError = False
flgHaveReturn = False

# Global variables
countArgs = 0
callingFunc = ""
programName = ""
arrayData = ""

# Tokens definition
tokens = [
    # Arithmetic Operators
    'MINUS',
    'PLUS',
    'MULTIPLY',
    'DIVIDE',
    'MOD',
    'INCREMENT',
    'DECREMENT',
    # Relational Operators
    'COMPARISON',
    'DIFFERENT',
    'GREATERTHAN',
    'LESSTHAN',
    'GREATERHANOREQUAL',
    'LESSTHANOREQUAL',
    # Logical Operators
    'AND',
    'OR',
    # Asignment Operators
    'EQUALS',
    'PLUSEQUALS',
    'SUBSTRACTEQUALS',
    # Others
    'ID',
    'COMMA',
    'LEFTBRACKET',
    'RIGHTBRACKET',
    'LEFTSQRBRACKET',
    'RIGHTSQRBRACKET',
    'LEFTPARENTHESIS',
    'RIGHTPARENTHESIS',
    'SEMICOLON',
    'CTESTRING',
    'CTECHAR',
    'CTEFLOAT',
    'CTEINT'
]

# Reserved words definition
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'var': 'VAR',
    'module': 'MODULE',
    'return': 'RETURN',
    'while': 'WHILE',
    'for': 'FOR',
    'do': 'DO',
    'to': 'TO',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'read': 'READ',
    'write': 'WRITE',
    'program': 'PROGRAM',
    'main': 'MAIN'
}

tokens += list(reserved.values())

# Token expressions
t_MINUS = r'\-'
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_MOD = r'\%'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'

t_COMPARISON = r'\=\='
t_GREATERHANOREQUAL = r'\>\='
t_LESSTHANOREQUAL = r'\<\='
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_DIFFERENT = r'\!\='

t_AND = r'\&'
t_OR = r'\|'

t_EQUALS = r'\='
t_PLUSEQUALS = r'\+\='
t_SUBSTRACTEQUALS = r'\-\='
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'
t_LEFTSQRBRACKET = r'\['
t_RIGHTSQRBRACKET = r'\]'
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_ignore = ' \t'


def t_CTECHAR(token):
    r'"([^"])"'
    token.value = str(token.value)[1]
    return token


def t_CTESTRING(token):
    r'"([^"]*)"'
    token.value = str(token.value)
    return token


def t_CTEFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_CTEINT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CTEBOOL(t):
    r'(true|false)'
    t.value(t.value == "true")
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(token):
    print('No apropiado')
    token.lexer.skip(1)


lexer = lex.lex()


# ====================== Main ======================
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON neupoint_goto_main vars functions_list MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end
            | PROGRAM ID SEMICOLON neupoint_goto_main vars MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end
            | PROGRAM ID SEMICOLON neupoint_goto_main functions_list MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end
            | PROGRAM ID SEMICOLON neupoint_goto_main MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end
    '''
    global programName

    p[0] = "Program {} was compiled succesfully".format(programName)

    # Generate the object code
    interCode.compileCode(funcTable, programName)

    print(interCode.stkOperator)
    print(interCode.stkOperand)
    print(interCode.stkType)
    print(interCode.stkIndexes)
    for i in interCode.stkQuadruples:
        print(i)


def p_neupoint_goto_main(p):
    '''
    neupoint_goto_main :
    '''
    global programName
    programName = p[-2]
    interCode.generateGOTOMain()


def p_neupoint_fill_goto_main(p):
    '''
    neupoint_fill_goto_main :
    '''
    interCode.currentFunction = 'global'
    interCode.fillGOTOMain()


def p_neupoint_end(p):
    '''
    neupoint_end :
    '''
    interCode.endQuad()

# ====================== Variables ======================


def p_data_type(p):
    '''
    data_type : INT
              | FLOAT
              | CHAR
    '''
    p[0] = p[1]


def p_vars(p):
    '''
    vars : VAR vars_lists neupoint_add_vars
    '''
    pass


def p_vars_lists(p):
    '''
    vars_lists : data_type decla_ids_list SEMICOLON vars_lists
               | data_type decla_ids_list SEMICOLON
    '''
    # Map the id list to a tupple format (VarType, ID)
    p[0] = list(map(lambda x: (p[1], x[0], x[1]) if (
        type(x) == tuple) else (p[1], x), p[2]))

    # Put all the IDs list together
    if(len(p) > 4):
        if(type(p[4]) == list):
            p[0] += p[4]


def p_decla_ids_list(p):
    '''
    decla_ids_list : decla_identifier COMMA decla_ids_list
                   | decla_identifier
    '''
    # Return an array with all the IDs of the current id list
    if(len(p) == 2):
        p[0] = [p[1]]
    elif(len(p) > 2):
        p[0] = [p[1]] + p[3]


def p_decla_identifier(p):
    '''
    decla_identifier : ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET
                     | ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET
                     | ID
    '''

    if (len(p) == 8):
        p[0] = p[1], (p[3], p[6])
    elif (len(p) == 5):
        p[0] = p[1], p[3]
    else:
        p[0] = p[1]


def p_identifier(p):
    '''
    identifier : ID neupoint_add_identifier LEFTSQRBRACKET neupoint_index_array exp neupoint_remove_wall RIGHTSQRBRACKET LEFTSQRBRACKET neupoint_index_matrix exp neupoint_remove_wall RIGHTSQRBRACKET neupoint_update_matrix_addr
               | ID neupoint_add_identifier LEFTSQRBRACKET neupoint_index_array exp neupoint_remove_wall RIGHTSQRBRACKET neupoint_update_array_addr
               | ID neupoint_add_identifier
    '''
    pass


# --------------- Variables Neural Points ---------------
def p_neupoint_add_vars(p):
    '''
    neupoint_add_vars :
    '''
    interCode.addVariablesToTables(funcTable, interCode.currentFunction, p[-1])


def p_neupoint_add_identifier(p):
    '''
    neupoint_add_identifier :
    '''
    interCode.addIdentifiers(funcTable, p[-1])


def p_neupoint_index_array(p):
    '''
    neupoint_index_array : 
    '''
    global arrayData
    arrayData = funcTable.searchVariable(interCode.currentFunction, p[-3])

    # Remove base address
    interCode.stkOperand.pop()
    interCode.stkType.pop()

    # Make the validation to see if the variable is an array
    if(arrayData['numDimensions'] == 0):
        raise Exception('Variable {} is not an array'.format(p[-3]))

    # Add a false wall to give priority to the exp inside the index
    interCode.stkOperator.append('(')


def p_neupoint_index_matrix(p):
    '''
    neupoint_index_matrix : 
    '''
    global arrayData

    # Make the validation to see if the variable is a matrix
    if(arrayData['numDimensions'] == 1):
        raise Exception('Variable {} is not a matrix'.format(p[-7]))

    # Add a false wall to give priority to the exp inside the index
    interCode.stkOperator.append('(')


def p_neupoint_update_array_addr(p):
    '''
    neupoint_update_array_addr : 
    '''
    global arrayData
    interCode.updateArrayAddress(arrayData, p[-7])


def p_neupoint_update_matrix_addr(p):
    '''
    neupoint_update_matrix_addr : 
    '''
    global arrayData
    interCode.updateMatrixAddress(arrayData)


# ====================== Functions ======================
def p_return_type(p):
    '''
    return_type : data_type
                | VOID
    '''
    p[0] = p[1]


def p_functions_list(p):
    '''
    functions_list : function functions_list
                   | function
    '''
    pass


def p_function(p):
    '''
    function : MODULE return_type ID neupoint_add_function parameters_list vars neupoint_start_function block neupoint_check_for_return neupoint_end_function
             | MODULE return_type ID neupoint_add_function parameters_list neupoint_start_function block neupoint_check_for_return neupoint_end_function
    '''
    pass


def p_parameters_list(p):
    '''
    parameters_list : LEFTPARENTHESIS parameter RIGHTPARENTHESIS neupoint_add_parameters
                    | LEFTPARENTHESIS RIGHTPARENTHESIS
    '''
    pass


def p_parameter(p):
    '''
    parameter : data_type decla_identifier COMMA parameter
              | data_type decla_identifier
    '''
    # Check if any parameter is a array or matrix
    if(type(p[2]) == tuple):
        tempId = p[2][0]
        tempDimen = p[2][1]

        # Put together the tuple list with (ParamType, Name)
        if(len(p) == 5):
            p[0] = [(p[1], tempId, tempDimen)] + p[4]
        else:
            p[0] = [(p[1], tempId, tempDimen)]

    # If not, just pass the type and id
    else:
        # Put together the tuple list with (ParamType, Name)
        if(len(p) == 5):
            p[0] = [(p[1], p[2])] + p[4]
        else:
            p[0] = [(p[1], p[2])]


# --------------- Functions Neural Points ---------------
def p_neupoint_add_function(p):
    '''
    neupoint_add_function : 
    '''
    interCode.currentFunction = p[-1]
    # Create the function table
    interCode.addFunctionToTable(funcTable, interCode.currentFunction, p[-2])


def p_neupoint_add_parameters(p):
    '''
    neupoint_add_parameters :
    '''
    interCode.addVariablesToTables(
        funcTable, interCode.currentFunction, p[-2], True)


def p_neupoint_start_function(p):
    '''
    neupoint_start_function : 
    '''

    funcTable.functionTable[interCode.currentFunction]['numQuad'] = len(
        interCode.stkQuadruples) + 1


def p_neupoint_check_for_return(p):
    '''
    neupoint_check_for_return : 
    '''

    # Get the name and return type
    if(p[-8] == 'module'):
        returnType = p[-7]

    else:
        returnType = p[-6]

    global flgHaveReturn

    # Makes the validation if the function is not void and does not have a return
    if(returnType != 'void' and not flgHaveReturn):
        raise Exception(
            'Function "{}" need a return of type {}'.format(interCode.currentFunction, returnType))

    flgHaveReturn = False


def p_neupoint_end_function(p):
    '''
    neupoint_end_function : 
    '''

    # Insert the end quadruple of a function
    interCode.endFunctionQuad()

    # Release the Local Variable Table
    funcTable.functionTable[interCode.currentFunction]['varTable'] = {}


# ====================== Operators ======================
def p_comparators(p):
    '''
    comparators : COMPARISON
                | GREATERHANOREQUAL
                | LESSTHANOREQUAL
                | GREATERTHAN
                | LESSTHAN
                | DIFFERENT
    '''
    p[0] = p[1]


def p_exp_operator(p):
    '''
    exp_operator : PLUS
                 | MINUS
    '''
    p[0] = p[1]


def p_term_operator(p):
    '''
    term_operator : MULTIPLY
                  | DIVIDE
                  | MOD
    '''
    p[0] = p[1]


# ====================== Statutes ======================
def p_block(p):
    '''
    block : LEFTBRACKET statutes_list RIGHTBRACKET
          | LEFTBRACKET RIGHTBRACKET
    '''
    pass


def p_statutes_list(p):
    '''
    statutes_list : statute statutes_list
                  | statute
    '''
    pass


def p_statute(p):
    '''
    statute : assignment
            | function_return
            | reading
            | writing
            | decision
            | loop
            | function_call_void
    '''
    pass


def p_assignment(p):
    '''
    assignment : identifier EQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON
               | identifier PLUSEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON
               | identifier SUBSTRACTEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON
               | identifier INCREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON
               | identifier DECREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON
    '''
    pass


def p_reading(p):
    '''
    reading : READ LEFTPARENTHESIS reading_list RIGHTPARENTHESIS SEMICOLON
    '''
    pass


def p_reading_list(p):
    '''
    reading_list : identifier  COMMA reading_list
                 | identifier
    '''
    # Push the writing quad
    interCode.readQuad()


def p_writing(p):
    '''
    writing : WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON
    '''
    pass


def p_writing_list(p):
    '''
    writing_list : CTESTRING neupoint_add_cte_operand neupoint_write_quad COMMA writing_list
                 | expresion neupoint_write_quad COMMA writing_list
                 | CTESTRING neupoint_add_cte_operand neupoint_write_quad
                 | expresion neupoint_write_quad
    '''
    pass


def p_decision(p):
    '''
    decision : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad THEN block ELSE neupoint_else_conditional_quad block neupoint_end_conditional_quad
             | IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad THEN block neupoint_end_conditional_quad
    '''
    pass


def p_loop(p):
    '''
    loop : conditional
         | non_conditional
    '''
    pass


def p_conditional(p):
    '''
    conditional : WHILE neupoint_while_start LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad DO block neupoint_while_end
    '''
    pass


def p_non_conditional(p):
    '''
    non_conditional : FOR ID neupoint_add_operand_integer EQUALS neupoint_add_operator exp neupoint_assignment_quad neupoint_add_operand_for TO exp  neupoint_comparison_quad DO block neupoint_for_end
    '''
    pass


def p_function_return(p):
    '''
    function_return : RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON
    '''
    global flgHaveReturn
    flgHaveReturn = True

    # Search the function data
    funcData = funcTable.searchFunction(interCode.currentFunction)

    # Validate the return type
    interCode.returnFunctionQuad(
        interCode.currentFunction, funcData['returnType'])


def p_function_call_void(p):
    '''
    function_call_void : function_call SEMICOLON
    '''
    pass


def p_function_call(p):
    '''
    function_call : ID neupoint_validate_function LEFTPARENTHESIS neupoint_era_quad neupoint_add_wall ags_list neupoint_validate_num_args RIGHTPARENTHESIS neupoint_gosub_quad
                  | ID neupoint_validate_function LEFTPARENTHESIS neupoint_era_quad neupoint_add_wall neupoint_validate_num_args RIGHTPARENTHESIS neupoint_gosub_quad
    '''
    pass


def p_ags_list(p):
    '''
    ags_list : expresion neupoint_validate_args COMMA ags_list
             | expresion neupoint_validate_args
    '''
    pass


def p_expresion(p):
    '''
    expresion : exp_relational AND neupoint_add_operator expresion neupoint_logical_relational_opt
              | exp_relational OR neupoint_add_operator expresion neupoint_logical_relational_opt
              | exp_relational
    '''
    pass


def p_exp_relational(p):
    '''
    exp_relational : exp comparators neupoint_add_operator exp neupoint_logical_relational_opt
                   | exp
    '''
    pass


def p_exp(p):
    '''
    exp : term neupoint_arithmetic_exp_quad exp_operator neupoint_add_operator exp
        | term neupoint_arithmetic_exp_quad
    '''
    pass


def p_term(p):
    '''
    term : factor neupoint_arithmetic_term_quad term_operator neupoint_add_operator term
         | factor neupoint_arithmetic_term_quad
    '''
    pass


def p_factor(p):
    '''
    factor : LEFTPARENTHESIS neupoint_add_wall expresion neupoint_remove_wall RIGHTPARENTHESIS
           | CTEINT neupoint_add_cte_operand
           | CTEFLOAT neupoint_add_cte_operand
           | CTECHAR neupoint_add_cte_operand
           | function_call
           | identifier
    '''


# --------------- Expressions Neural Points ---------------
def p_neupoint_add_operator(p):
    '''
    neupoint_add_operator : 
    '''
    interCode.stkOperator.append(p[-1])


def p_neupoint_add_cte_operand(p):
    '''
    neupoint_add_cte_operand : 
    '''
    # Add a constant variable to the stacks and memory
    interCode.addConstantValue(p[-1])


def p_neupoint_arithmetic_exp_quad(p):
    '''
    neupoint_arithmetic_exp_quad : 
    '''

    # If the last operator is a PLUS or MINUS..
    interCode.generateOperatorQuadruple(interCode.currentFunction, ['+', '-'])


def p_neupoint_arithmetic_term_quad(p):
    '''
    neupoint_arithmetic_term_quad : 
    '''

    # If the last operator is a MULTIPLY, DIVIDE or MODULE..
    interCode.generateOperatorQuadruple(interCode.currentFunction,
                                        ['*', '/', '%'])


def p_neupoint_add_wall(p):
    '''
    neupoint_add_wall : 
    '''
    interCode.stkOperator.append('(')


def p_neupoint_remove_wall(p):
    '''
    neupoint_remove_wall : 
    '''
    openWall = interCode.stkOperator.pop()
    if(openWall != '('):
        raise Exception('Parenthesis Missing')


def p_neupoint_assignment_quad(p):
    '''
    neupoint_assignment_quad : 
    '''
    interCode.generateAssignmentQuad()


def p_neupoint_assignment_single_quad(p):
    '''
    neupoint_assignment_single_quad : 
    '''
    interCode.generateAssignmentSingleQuad()


def p_neupoint_logical_relational_opt(p):
    '''
    neupoint_logical_relational_opt : 
    '''
    interCode.generateOperatorQuadruple(
        interCode.currentFunction, flgArithmetic=False)


def p_neupoint_conditional_quad(p):
    '''
    neupoint_conditional_quad : 
    '''
    interCode.generateConditionQuad()


def p_neupoint_else_conditional_quad(p):
    '''
    neupoint_else_conditional_quad : 
    '''
    interCode.elseConditionQuad()


def p_neupoint_end_conditional_quad(p):
    '''
    neupoint_end_conditional_quad : 
    '''
    interCode.endConditionQuad()


def p_neupoint_while_start(p):
    '''
    neupoint_while_start : 
    '''
    # Push the jump quad num
    interCode.stkJumps.append(len(interCode.stkQuadruples))


def p_neupoint_while_end(p):
    '''
    neupoint_while_end : 
    '''
    # Push the jump quad num
    interCode.endWhileQuad()


def p_neupoint_validate_function(p):
    '''
    neupoint_validate_function : 
    '''
    global callingFunc
    callingFunc = p[-1]

    # Validate that function exists
    funcTable.searchFunction(callingFunc)


def p_neupoint_era_quad(p):
    '''
    neupoint_era_quad : 
    '''
    global callingFunc
    # Get the num of variables
    numVars = funcTable.searchFunction(callingFunc)['numVars']

    # Append the ERA quadruple
    interCode.eraQuad(numVars)

    # Initilize the args counter
    global countArgs
    countArgs = 0


def p_neupoint_validate_args(p):
    '''
    neupoint_validate_args : 
    '''
    global countArgs
    global callingFunc

    # Get the data type of the arguments
    argType = funcTable.searchFunction(callingFunc)['paramsType']

    # Check if there are more args
    if(countArgs > len(argType) - 1):
        raise Exception('Sending {} arguments but function "{}" needs {}'.format(
            countArgs + 1, callingFunc, len(argType)))

    # Validate the type are correct and push the quad
    interCode.argumentQuad(argType[countArgs], countArgs)

    # Increase the argument counter
    countArgs += 1


def p_neupoint_validate_num_args(p):
    '''
    neupoint_validate_num_args : 
    '''
    global countArgs
    global callingFunc

    # Get the data type of the arguments
    paramsNumber = funcTable.searchFunction(callingFunc)['paramsNumber']

    # Check if there are less args
    if(countArgs < paramsNumber):
        raise Exception('Sending {} arguments but function "{}" needs {}'.format(
            countArgs, callingFunc, paramsNumber))


def p_neupoint_gosub_quad(p):
    '''
    neupoint_gosub_quad : 
    '''
    # Remove the wall
    interCode.stkOperator.pop()

    # Get the called func data
    funcData = funcTable.searchFunction(callingFunc)

    # Get the return memory address if the function is not void
    if (funcData['returnType'] != 'void'):
        returnAddress = funcTable.searchVariable(
            'global', callingFunc)['memoryAddress']
    else:
        returnAddress = None

    # Add the GOSUB quad
    interCode.gosubQuad(funcData['returnType'], funcData['numQuad'],
                        interCode.currentFunction, returnAddress)


def p_neupoint_write_quad(p):
    '''
    neupoint_write_quad : 
    '''
    interCode.writeQuad()


def p_neupoint_add_operand_integer(p):
    '''
    neupoint_add_operand_integer : 
    '''
    # Get the operand data type
    operandData = funcTable.searchVariable(
        interCode.currentFunction, p[-1])

    if(operandData['dataType'] != 'int'):
        raise Exception("Variable used in a FOR must be an integer")

    # Add name and datatype to the stacks
    interCode.stkOperand.append(operandData['memoryAddress'])
    interCode.stkType.append(operandData['dataType'])
    interCode.stkOperand.append(operandData['memoryAddress'])
    interCode.stkType.append(operandData['dataType'])


def p_neupoint_add_operand_for(p):
    '''
    neupoint_add_operand_for : 
    '''
    # Generate the VControl Quad
    interCode.generateVControlQuad(interCode.currentFunction)


def p_neupoint_comparison_quad(p):
    '''
    neupoint_comparison_quad : 
    '''
    # Generate quads
    interCode.generateVCVFComparisonQuad(interCode.currentFunction)


def p_neupoint_for_end(p):
    '''
    neupoint_for_end : 
    '''

    # Generate las FOR quad and fill the GOTOs
    interCode.fillForQuad()


# ====================== Rule for syntax errors ======================
def p_error(p):
    global flgError
    flgError = True
    print("\n-> No apropiado\n")


# Build the parser
parser = yacc.yacc()

try:
    # Read the source file
    fileName = './Tests/Input2.txt'
    f = open(fileName, "r")
    srcFile = f.read()

    # Parser the input
    result = parser.parse(srcFile)

    if not flgError:
        print("\n-> Apropiado\n")

except FileNotFoundError:
    print("\n-> No existe el archivo\n")
