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
    # Assignment Operators
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
    program : PROGRAM ID SEMICOLON vars functions_list neupoint_back_global MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block
            | PROGRAM ID SEMICOLON vars MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block
            | PROGRAM ID SEMICOLON functions_list neupoint_back_global MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block
            | PROGRAM ID SEMICOLON MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block
    '''


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


def p_ids_list(p):
    '''
    ids_list : identifier COMMA ids_list
             | identifier
    '''
    pass


def p_identifier(p):
    '''
    identifier : ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET LEFTSQRBRACKET expresion RIGHTSQRBRACKET
               | ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET
               | ID
    '''
    p[0] = p[1]


# --------------- Variables Neural Points ---------------
def p_neupoint_add_vars(p):
    '''
    neupoint_add_vars :
    '''
    funcTable.addVariables(interCode.currentFunction, p[-1])


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
    function : MODULE return_type ID neupoint_add_function parameters_list vars block
             | MODULE return_type ID neupoint_add_function parameters_list block
    '''
    global flgHaveReturn

    # Makes the validation if the function is not void and does not have a return
    if(p[2] != 'void' and not flgHaveReturn):
        raise Exception(
            'Function "{}" need a return of type {}'.format(p[3], p[2]))

    # or if the function is void and have a return
    elif(p[1] == 'void' and flgHaveReturn):
        raise Exception(
            'Function "{}" is void and does not need a return'.format(p[3]))

    flgHaveReturn = False


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
    funcTable.addNewFunction(interCode.currentFunction, p[-2])


def p_neupoint_add_parameters(p):
    '''
    neupoint_add_parameters :
    '''
    funcTable.addVariables(interCode.currentFunction, p[-2], True)


def p_neupoint_back_global(p):
    '''
    neupoint_back_global : 
    '''
    interCode.currentFunction = 'global'


# ====================== Operators ======================
def p_comparators(p):
    '''
    comparators : COMPARISON
                | GREATERHANOREQUAL
                | LESSTHANOREQUAL
                | GREATERTHAN
                | LESSTHAN
                | DIFFERENT
                | OR
                | AND
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
    statute : asignation
            | reading
            | writing
            | decision
            | loop
            | function_return
            | function_call SEMICOLON
    '''
    pass


def p_asignation(p):
    '''
    asignation : identifier EQUALS expresion SEMICOLON
               | identifier PLUSEQUALS expresion SEMICOLON
               | identifier SUBSTRACTEQUALS expresion SEMICOLON
               | identifier INCREMENT SEMICOLON
               | identifier DECREMENT SEMICOLON
    '''
    pass


def p_reading(p):
    '''
    reading : READ LEFTPARENTHESIS ids_list RIGHTPARENTHESIS SEMICOLON
    '''
    pass


def p_writing(p):
    '''
    writing : WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON
    '''
    pass


def p_writing_list(p):
    '''
    writing_list : CTESTRING COMMA writing_list
                 | expresion COMMA writing_list
                 | CTESTRING
                 | expresion
    '''
    pass


def p_decision(p):
    '''
    decision : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block ELSE block
             | IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block
    '''
    pass


def p_loop(p):
    '''
    loop : conditional block
         | non_conditional block
    '''
    pass


def p_conditional(p):
    '''
    conditional : WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO
    '''
    pass


def p_non_conditional(p):
    '''
    non_conditional : FOR ID EQUALS exp TO exp DO
    '''
    pass


def p_function_return(p):
    '''
    function_return : RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON
    '''
    global flgHaveReturn
    flgHaveReturn = True


def p_function_call(p):
    '''
    function_call : ID LEFTPARENTHESIS expresion_list RIGHTPARENTHESIS
    '''
    pass


def p_expresion_list(p):
    '''
    expresion_list : expresion COMMA expresion_list
                   | expresion
    '''
    pass


def p_expresion(p):
    '''
    expresion : exp comparators neupoint_add_operator exp
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
    factor : LEFTPARENTHESIS neupoint_add_wall expresion RIGHTPARENTHESIS neupoint_remove_wall
           | CTEINT neupoint_add_cte_operand
           | CTEFLOAT neupoint_add_cte_operand
           | CTECHAR neupoint_add_cte_operand
           | function_call
           | identifier neupoint_add_operand
    '''


# --------------- Expressions Neural Points ---------------
def p_neupoint_add_operator(p):
    '''
    neupoint_add_operator : 
    '''
    interCode.stkOperator.append(p[-1])


def p_neupoint_add_operand(p):
    '''
    neupoint_add_operand : 
    '''
    # Get the operand data type
    operandType = funcTable.searchVariable(
        interCode.currentFunction, p[-1])['dataType']

    # Add name and datatype to the stacks
    interCode.stkOperand.append(p[-1])
    interCode.stkType.append(operandType)


def p_neupoint_add_cte_operand(p):
    '''
    neupoint_add_cte_operand : 
    '''
    interCode.stkOperand.append(p[-1])
    if(type(p[-1]).__name__ == 'str'):
        if(len(p[-1]) == 1):
            interCode.stkType.append('char')
        else:
            interCode.stkType.append('str')
    else:
        interCode.stkType.append(type(p[-1]).__name__)


def p_neupoint_arithmetic_exp_quad(p):
    '''
    neupoint_arithmetic_exp_quad : 
    '''

    # If the last operator is a PLUS or MINUS..
    interCode.generateArithmeticQuadruple(['+', '-'])


def p_neupoint_arithmetic_term_quad(p):
    '''
    neupoint_arithmetic_term_quad : 
    '''

    # If the last operator is a MULTIPLY, DIVIDE or MODULE..
    interCode.generateArithmeticQuadruple(['*', '/', '%'])


def p_neupoint_add_wall(p):
    '''
    neupoint_add_wall : 
    '''
    interCode.stkOperator.append('(')


def p_neupoint_remove_wall(p):
    '''
    neupoint_remove_wall : 
    '''
    if(interCode.stkOperator.pop() != '('):
        raise Exception('Parenthesis Missing')


# ====================== Rule for syntax errors ======================
def p_error(p):
    global flgError
    flgError = True
    print("\n-> No apropiado\n")


# Build the parser
parser = yacc.yacc()

try:
    # Read the source file
    fileName = './Tests/Input.txt'
    f = open(fileName, "r")
    srcFile = f.read()

    # Parser the input
    result = parser.parse(srcFile)

    if not flgError:
        print("\n-> Apropiado\n")

except FileNotFoundError:
    print("\n-> No existe el archivo\n")
