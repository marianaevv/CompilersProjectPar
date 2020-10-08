import ply.lex as lex
import ply.yacc as yacc
import sys

# Flag to know if there was an error or not
bError = False

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
    'COLON',
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
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_ignore = ' \t\n'


def t_CTECHAR(token):
    r'"([^"])"'
    token.value = str(token.value)
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


def t_error(token):
    print('No apropiado')
    token.lexer.skip(1)


lexer = lex.lex()

# Grammars Definitions
# program : PROGRAM ID SEMICOLON vars funciones main LEFTPARENTHESIS RIGHTPARENTHESIS bloque
#         | PROGRAM ID SEMICOLON vars main LEFTPARENTHESIS RIGHTPARENTHESIS bloque
#         | PROGRAM ID SEMICOLON funciones main LEFTPARENTHESIS RIGHTPARENTHESIS bloque


def p_program(p):
    '''
    program : mas_estatutos
    '''
    pass


def p_vars(p):
    '''
    vars : VAR vartipo
    '''
    pass


def p_vartipo(p):
    '''
    vartipo : tipo COLON ids SEMICOLON vartipo
            | tipo COLON ids SEMICOLON 
    '''
    pass


def p_ids(p):
    '''
    ids : declaraid COMMA ids
        | declaraid
    '''
    pass


def p_declaraid(p):
    '''
    declaraid : ID dimen_declara dimen_declara
              | ID dimen_declara
              | ID
    '''
    pass


def p_dimen_declara(p):
    '''
    dimen_declara : LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET
    '''
    pass


def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | CHAR
    '''
    pass


def p_funcvoid(p):
    '''
    funcvoid : MODULE ID parametros SEMICOLON vars bloque
             | MODULE ID parametros SEMICOLON bloque
    '''
    pass


def p_funcreturn(p):  # To be fixed
    '''
    funcreturn : tipo MODULE ID parametros SEMICOLON vars bloque
               | tipo MODULE ID parametros SEMICOLON bloque
    '''
    pass


def p_funciones(p):
    '''
    funciones : funcvoid funciones
              | funcreturn funciones
              | funcvoid
              | funcreturn
    '''
    pass


def p_parametros(p):
    '''
    parametros : LEFTPARENTHESIS paramlist RIGHTPARENTHESIS
    '''
    pass


def p_paramlist(p):
    '''
    paramlist : tipo declaraid COMMA paramlist
              | tipo declaraid
    '''
    pass


def p_bloque(p):
    '''
    bloque : LEFTBRACKET mas_estatutos RIGHTBRACKET
           | LEFTBRACKET RIGHTBRACKET
    '''
    pass


def p_mas_estatutos(p):
    '''
    mas_estatutos : estatuto mas_estatutos
                  | estatuto
    '''
    pass


def p_estatuto(p):
    '''
    estatuto : asignacion
             | lectura
             | escritura
             | decision
             | repeticion
    '''
#              | llamada_func
    pass


def p_asignacion(p):
    '''
    asignacion : id_dimensiones EQUALS expresion SEMICOLON
    '''
    pass


# def p_llamada_func(p):
#     '''
#     llamada_func : ID parametros SEMICOLON
#     '''
#     pass

def p_lista_ids(p):
    '''
    lista_ids : id_dimensiones COMMA lista_ids
             | id_dimensiones
    '''
    pass


def p_lectura(p):
    '''
    lectura : READ LEFTPARENTHESIS lista_ids RIGHTPARENTHESIS SEMICOLON
    '''
    pass


def p_escritura(p):
    '''
    escritura : WRITE LEFTPARENTHESIS poswrite RIGHTPARENTHESIS SEMICOLON
    '''
    pass


def p_poswrite(p):
    '''
    poswrite : CTESTRING COMMA poswrite
             | expresion COMMA poswrite
             | CTESTRING
             | expresion
    '''
    pass


def p_decision(p):
    '''
    decision : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN bloque ELSE bloque
             | IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN bloque
    '''
    pass


def p_repeticion(p):
    '''
    repeticion : condicional bloque
               | no_condicional bloque
    '''
    pass


def p_condicional(p):
    '''
    condicional : WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO
    '''
    pass


def p_no_condicional(p):
    '''
    no_condicional : FOR ID EQUALS exp TO exp DO
    '''
    pass


def p_expresion(p):
    '''
    expresion : exp comparadores exp
              | exp
    '''
    pass


def p_comparadores(p):
    '''
    comparadores : COMPARISON
                 | GREATERHANOREQUAL
                 | LESSTHANOREQUAL
                 | GREATERTHAN
                 | LESSTHAN
                 | DIFFERENT
    '''
    pass


def p_exp(p):
    '''
    exp : termino opera_exp exp
        | termino
    '''
    pass


def p_opera_exp(p):
    '''
    opera_exp : PLUS
              | MINUS
    '''
    pass


def p_termino(p):
    '''
    termino : factor opera_term termino
            | factor
    '''
    pass


def p_opera_term(p):
    '''
    opera_term : MULTIPLY
               | DIVIDE
    '''
    pass


def p_factor(p):
    '''
    factor : LEFTPARENTHESIS expresion RIGHTPARENTHESIS
           | opera_exp valor_opt
           | valor_opt
    '''
    pass


def p_id_dimensiones(p):
    '''
    id_dimensiones : ID dimen_expre dimen_expre
                   | ID dimen_expre
                   | ID
    '''
    pass


def p_dimen_expre(p):
    '''
    dimen_expre : LEFTSQRBRACKET expresion RIGHTSQRBRACKET
    '''
    pass


def p_valor_opt(p):
    '''
    valor_opt : id_dimensiones
              | CTEINT
              | CTEFLOAT
    '''
    # | llamada_func
    pass


def p_error(p):
    # Error rule for syntax errors
    global bError
    bError = True
    print("\n-> No apropiado\n")


# Build the parser
parser = yacc.yacc()

try:
    # Read the source file
    fileName = './Input.txt'
    f = open(fileName, "r")
    srcFile = f.read()

    # Parser the input
    result = parser.parse(srcFile)

    if not bError:
        print("\n-> Apropiado\n")
except:
    print("\n-> No existe el archivo\n")
