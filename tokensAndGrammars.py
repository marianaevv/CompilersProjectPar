import ply.lex as lex
import ply.yacc as yacc
import sys

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
    'Program': 'PROGRAM',
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


lexer = lex.lex()


lexer.input(
    '- + * / % ++ -- == != > < >= <= & | = += -= resultado : ; , { } ( ) 32 32.55 "A" "abasd_ \#!#c"')
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Grammars Definitions


def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON vars funciones main LEFTPARENTHESIS RIGHTPARENTHESIS bloque
            | PROGRAM ID SEMICOLON vars main LEFTPARENTHESIS RIGHTPARENTHESIS bloque
            | PROGRAM ID SEMICOLON funciones main LEFTPARENTHESIS RIGHTPARENTHESIS bloque
            | PROGRAM ID SEMICOLON main LEFTPARENTHESIS RIGHTPARENTHESIS bloque
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
    funcvoid : MODULE ID PARAMETROS SEMICOLON vars bloque
             | MODULE ID PARAMETROS SEMICOLON bloque
    '''
    pass


def p_funcreturn(p):  # To be fixed
    '''
    funcreturn : tipo MODULE ID PARAMETROS SEMICOLON vars bloque
               | tipo MODULE ID PARAMETROS SEMICOLON bloque
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
    parametros : LEFTPARENTHESIS tipo 
    '''
    pass
