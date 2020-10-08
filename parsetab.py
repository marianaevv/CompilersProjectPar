
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMMA COMPARISON CTECHAR CTEFLOAT CTEINT CTESTRING DECREMENT DIFFERENT DIVIDE DO ELSE EQUALS FLOAT FOR GREATERHANOREQUAL GREATERTHAN ID IF INCREMENT INT LEFTBRACKET LEFTPARENTHESIS LEFTSQRBRACKET LESSTHAN LESSTHANOREQUAL MAIN MINUS MOD MODULE MULTIPLY OR PLUS PLUSEQUALS PROGRAM READ RETURN RIGHTBRACKET RIGHTPARENTHESIS RIGHTSQRBRACKET SEMICOLON SUBSTRACTEQUALS THEN TO VAR WHILE WRITE\n    program : mas_estatutos\n    \n    vars : VAR vartipo\n    \n    vartipo : tipo COLON ids SEMICOLON vartipo\n            | tipo COLON ids SEMICOLON \n    \n    ids : declaraid COMMA ids\n        | declaraid\n    \n    declaraid : ID dimen_declara dimen_declara\n              | ID dimen_declara\n              | ID\n    \n    dimen_declara : LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET\n    \n    tipo : INT\n         | FLOAT\n         | CHAR\n    \n    funcvoid : MODULE ID parametros SEMICOLON vars bloque\n             | MODULE ID parametros SEMICOLON bloque\n    \n    funcreturn : tipo MODULE ID parametros SEMICOLON vars bloque\n               | tipo MODULE ID parametros SEMICOLON bloque\n    \n    funciones : funcvoid funciones\n              | funcreturn funciones\n              | funcvoid\n              | funcreturn\n    \n    parametros : LEFTPARENTHESIS paramlist RIGHTPARENTHESIS\n    \n    paramlist : tipo declaraid COMMA paramlist\n              | tipo declaraid\n    \n    bloque : LEFTBRACKET mas_estatutos RIGHTBRACKET\n           | LEFTBRACKET RIGHTBRACKET\n    \n    mas_estatutos : estatuto mas_estatutos\n                  | estatuto\n    \n    estatuto : asignacion\n             | lectura\n             | escritura\n             | decision\n             | repeticion\n    \n    asignacion : id_dimensiones EQUALS expresion SEMICOLON\n    \n    lista_ids : id_dimensiones COMMA lista_ids\n             | id_dimensiones\n    \n    lectura : READ LEFTPARENTHESIS lista_ids RIGHTPARENTHESIS SEMICOLON\n    \n    escritura : WRITE LEFTPARENTHESIS poswrite RIGHTPARENTHESIS SEMICOLON\n    \n    poswrite : CTESTRING COMMA poswrite\n             | expresion COMMA poswrite\n             | CTESTRING\n             | expresion\n    \n    decision : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN bloque ELSE bloque\n             | IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN bloque\n    \n    repeticion : condicional bloque\n               | no_condicional bloque\n    \n    condicional : WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO\n    \n    no_condicional : FOR ID EQUALS exp TO exp DO\n    \n    expresion : exp comparadores exp\n              | exp\n    \n    comparadores : COMPARISON\n                 | GREATERHANOREQUAL\n                 | LESSTHANOREQUAL\n                 | GREATERTHAN\n                 | LESSTHAN\n                 | DIFFERENT\n    \n    exp : termino opera_exp exp\n        | termino\n    \n    opera_exp : PLUS\n              | MINUS\n    \n    termino : factor opera_term termino\n            | factor\n    \n    opera_term : MULTIPLY\n               | DIVIDE\n    \n    factor : LEFTPARENTHESIS expresion RIGHTPARENTHESIS\n           | opera_exp valor_opt\n           | valor_opt\n    \n    id_dimensiones : ID dimen_expre dimen_expre\n                   | ID dimen_expre\n                   | ID\n    \n    dimen_expre : LEFTSQRBRACKET expresion RIGHTSQRBRACKET\n    \n    valor_opt : id_dimensiones\n              | CTEINT\n              | CTEFLOAT\n    '
    
_lr_action_items = {'READ':([0,3,4,5,6,7,8,23,24,25,49,54,74,82,84,90,94,],[10,10,-29,-30,-31,-32,-33,-45,10,-46,-26,-34,-25,-37,-38,-44,-43,]),'WRITE':([0,3,4,5,6,7,8,23,24,25,49,54,74,82,84,90,94,],[11,11,-29,-30,-31,-32,-33,-45,11,-46,-26,-34,-25,-37,-38,-44,-43,]),'IF':([0,3,4,5,6,7,8,23,24,25,49,54,74,82,84,90,94,],[12,12,-29,-30,-31,-32,-33,-45,12,-46,-26,-34,-25,-37,-38,-44,-43,]),'ID':([0,3,4,5,6,7,8,17,19,20,21,22,23,24,25,27,28,34,36,38,39,49,53,54,55,56,57,58,59,60,61,62,64,65,66,69,71,72,74,82,84,89,90,94,],[15,15,-29,-30,-31,-32,-33,29,15,15,15,15,-45,15,-46,15,15,15,15,-59,-60,-26,15,-34,15,-51,-52,-53,-54,-55,-56,15,15,-63,-64,15,15,15,-25,-37,-38,15,-44,-43,]),'WHILE':([0,3,4,5,6,7,8,23,24,25,49,54,74,82,84,90,94,],[16,16,-29,-30,-31,-32,-33,-45,16,-46,-26,-34,-25,-37,-38,-44,-43,]),'FOR':([0,3,4,5,6,7,8,23,24,25,49,54,74,82,84,90,94,],[17,17,-29,-30,-31,-32,-33,-45,17,-46,-26,-34,-25,-37,-38,-44,-43,]),'$end':([1,2,3,4,5,6,7,8,18,23,25,49,54,74,82,84,90,94,],[0,-1,-28,-29,-30,-31,-32,-33,-27,-45,-46,-26,-34,-25,-37,-38,-44,-43,]),'RIGHTBRACKET':([3,4,5,6,7,8,18,23,24,25,48,49,54,74,82,84,90,94,],[-28,-29,-30,-31,-32,-33,-27,-45,49,-46,74,-26,-34,-25,-37,-38,-44,-43,]),'EQUALS':([9,15,26,29,50,75,],[19,-70,-69,53,-68,-71,]),'LEFTPARENTHESIS':([10,11,12,16,19,21,22,27,28,36,38,39,53,55,56,57,58,59,60,61,62,64,65,66,71,72,89,],[20,21,22,28,36,36,36,36,36,36,-59,-60,36,36,-51,-52,-53,-54,-55,-56,36,36,-63,-64,36,36,36,]),'LEFTBRACKET':([13,14,87,88,92,93,],[24,24,24,-47,24,-48,]),'MULTIPLY':([15,26,30,35,37,40,41,50,63,75,81,],[-70,-69,-72,65,-67,-73,-74,-68,-66,-71,-65,]),'DIVIDE':([15,26,30,35,37,40,41,50,63,75,81,],[-70,-69,-72,66,-67,-73,-74,-68,-66,-71,-65,]),'PLUS':([15,19,21,22,26,27,28,30,33,35,36,37,38,39,40,41,50,53,55,56,57,58,59,60,61,62,63,64,65,66,71,72,75,80,81,89,],[-70,38,38,38,-69,38,38,-72,38,-62,38,-67,-59,-60,-73,-74,-68,38,38,-51,-52,-53,-54,-55,-56,38,-66,38,-63,-64,38,38,-71,-61,-65,38,]),'MINUS':([15,19,21,22,26,27,28,30,33,35,36,37,38,39,40,41,50,53,55,56,57,58,59,60,61,62,63,64,65,66,71,72,75,80,81,89,],[-70,39,39,39,-69,39,39,-72,39,-62,39,-67,-59,-60,-73,-74,-68,39,39,-51,-52,-53,-54,-55,-56,39,-66,39,-63,-64,39,39,-71,-61,-65,39,]),'COMPARISON':([15,26,30,32,33,35,37,40,41,50,63,75,79,80,81,],[-70,-69,-72,56,-58,-62,-67,-73,-74,-68,-66,-71,-57,-61,-65,]),'GREATERHANOREQUAL':([15,26,30,32,33,35,37,40,41,50,63,75,79,80,81,],[-70,-69,-72,57,-58,-62,-67,-73,-74,-68,-66,-71,-57,-61,-65,]),'LESSTHANOREQUAL':([15,26,30,32,33,35,37,40,41,50,63,75,79,80,81,],[-70,-69,-72,58,-58,-62,-67,-73,-74,-68,-66,-71,-57,-61,-65,]),'GREATERTHAN':([15,26,30,32,33,35,37,40,41,50,63,75,79,80,81,],[-70,-69,-72,59,-58,-62,-67,-73,-74,-68,-66,-71,-57,-61,-65,]),'LESSTHAN':([15,26,30,32,33,35,37,40,41,50,63,75,79,80,81,],[-70,-69,-72,60,-58,-62,-67,-73,-74,-68,-66,-71,-57,-61,-65,]),'DIFFERENT':([15,26,30,32,33,35,37,40,41,50,63,75,79,80,81,],[-70,-69,-72,61,-58,-62,-67,-73,-74,-68,-66,-71,-57,-61,-65,]),'SEMICOLON':([15,26,30,31,32,33,35,37,40,41,50,63,68,70,75,78,79,80,81,],[-70,-69,-72,54,-50,-58,-62,-67,-73,-74,-68,-66,82,84,-71,-49,-57,-61,-65,]),'COMMA':([15,26,30,32,33,35,37,40,41,43,45,46,50,63,75,78,79,80,81,],[-70,-69,-72,-50,-58,-62,-67,-73,-74,69,71,72,-68,-66,-71,-49,-57,-61,-65,]),'RIGHTPARENTHESIS':([15,26,30,32,33,35,37,40,41,42,43,44,45,46,47,50,52,63,67,75,78,79,80,81,83,85,86,],[-70,-69,-72,-50,-58,-62,-67,-73,-74,68,-36,70,-41,-42,73,-68,76,-66,81,-71,-49,-57,-61,-65,-35,-39,-40,]),'RIGHTSQRBRACKET':([15,26,30,32,33,35,37,40,41,50,51,63,75,78,79,80,81,],[-70,-69,-72,-50,-58,-62,-67,-73,-74,-68,75,-66,-71,-49,-57,-61,-65,]),'TO':([15,26,30,33,35,37,40,41,50,63,75,77,79,80,81,],[-70,-69,-72,-58,-62,-67,-73,-74,-68,-66,-71,89,-57,-61,-65,]),'DO':([15,26,30,33,35,37,40,41,50,63,75,76,79,80,81,91,],[-70,-69,-72,-58,-62,-67,-73,-74,-68,-66,-71,88,-57,-61,-65,93,]),'LEFTSQRBRACKET':([15,26,75,],[27,27,-71,]),'CTEINT':([19,21,22,27,28,34,36,38,39,53,55,56,57,58,59,60,61,62,64,65,66,71,72,89,],[40,40,40,40,40,40,40,-59,-60,40,40,-51,-52,-53,-54,-55,-56,40,40,-63,-64,40,40,40,]),'CTEFLOAT':([19,21,22,27,28,34,36,38,39,53,55,56,57,58,59,60,61,62,64,65,66,71,72,89,],[41,41,41,41,41,41,41,-59,-60,41,41,-51,-52,-53,-54,-55,-56,41,41,-63,-64,41,41,41,]),'CTESTRING':([21,71,72,],[45,45,45,]),'ELSE':([49,74,90,],[-26,-25,92,]),'THEN':([73,],[87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'mas_estatutos':([0,3,24,],[2,18,48,]),'estatuto':([0,3,24,],[3,3,3,]),'asignacion':([0,3,24,],[4,4,4,]),'lectura':([0,3,24,],[5,5,5,]),'escritura':([0,3,24,],[6,6,6,]),'decision':([0,3,24,],[7,7,7,]),'repeticion':([0,3,24,],[8,8,8,]),'id_dimensiones':([0,3,19,20,21,22,24,27,28,34,36,53,55,62,64,69,71,72,89,],[9,9,30,43,30,30,9,30,30,30,30,30,30,30,30,43,30,30,30,]),'condicional':([0,3,24,],[13,13,13,]),'no_condicional':([0,3,24,],[14,14,14,]),'bloque':([13,14,87,92,],[23,25,90,94,]),'dimen_expre':([15,26,],[26,50,]),'expresion':([19,21,22,27,28,36,71,72,],[31,46,47,51,52,67,46,46,]),'exp':([19,21,22,27,28,36,53,55,62,71,72,89,],[32,32,32,32,32,32,77,78,79,32,32,91,]),'termino':([19,21,22,27,28,36,53,55,62,64,71,72,89,],[33,33,33,33,33,33,33,33,33,80,33,33,33,]),'opera_exp':([19,21,22,27,28,33,36,53,55,62,64,71,72,89,],[34,34,34,34,34,62,34,34,34,34,34,34,34,34,]),'factor':([19,21,22,27,28,36,53,55,62,64,71,72,89,],[35,35,35,35,35,35,35,35,35,35,35,35,35,]),'valor_opt':([19,21,22,27,28,34,36,53,55,62,64,71,72,89,],[37,37,37,37,37,63,37,37,37,37,37,37,37,37,]),'lista_ids':([20,69,],[42,83,]),'poswrite':([21,71,72,],[44,85,86,]),'comparadores':([32,],[55,]),'opera_term':([35,],[64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> mas_estatutos','program',1,'p_program','tokensAndGrammars.py',151),
  ('vars -> VAR vartipo','vars',2,'p_vars','tokensAndGrammars.py',158),
  ('vartipo -> tipo COLON ids SEMICOLON vartipo','vartipo',5,'p_vartipo','tokensAndGrammars.py',165),
  ('vartipo -> tipo COLON ids SEMICOLON','vartipo',4,'p_vartipo','tokensAndGrammars.py',166),
  ('ids -> declaraid COMMA ids','ids',3,'p_ids','tokensAndGrammars.py',173),
  ('ids -> declaraid','ids',1,'p_ids','tokensAndGrammars.py',174),
  ('declaraid -> ID dimen_declara dimen_declara','declaraid',3,'p_declaraid','tokensAndGrammars.py',181),
  ('declaraid -> ID dimen_declara','declaraid',2,'p_declaraid','tokensAndGrammars.py',182),
  ('declaraid -> ID','declaraid',1,'p_declaraid','tokensAndGrammars.py',183),
  ('dimen_declara -> LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET','dimen_declara',3,'p_dimen_declara','tokensAndGrammars.py',190),
  ('tipo -> INT','tipo',1,'p_tipo','tokensAndGrammars.py',197),
  ('tipo -> FLOAT','tipo',1,'p_tipo','tokensAndGrammars.py',198),
  ('tipo -> CHAR','tipo',1,'p_tipo','tokensAndGrammars.py',199),
  ('funcvoid -> MODULE ID parametros SEMICOLON vars bloque','funcvoid',6,'p_funcvoid','tokensAndGrammars.py',206),
  ('funcvoid -> MODULE ID parametros SEMICOLON bloque','funcvoid',5,'p_funcvoid','tokensAndGrammars.py',207),
  ('funcreturn -> tipo MODULE ID parametros SEMICOLON vars bloque','funcreturn',7,'p_funcreturn','tokensAndGrammars.py',214),
  ('funcreturn -> tipo MODULE ID parametros SEMICOLON bloque','funcreturn',6,'p_funcreturn','tokensAndGrammars.py',215),
  ('funciones -> funcvoid funciones','funciones',2,'p_funciones','tokensAndGrammars.py',222),
  ('funciones -> funcreturn funciones','funciones',2,'p_funciones','tokensAndGrammars.py',223),
  ('funciones -> funcvoid','funciones',1,'p_funciones','tokensAndGrammars.py',224),
  ('funciones -> funcreturn','funciones',1,'p_funciones','tokensAndGrammars.py',225),
  ('parametros -> LEFTPARENTHESIS paramlist RIGHTPARENTHESIS','parametros',3,'p_parametros','tokensAndGrammars.py',232),
  ('paramlist -> tipo declaraid COMMA paramlist','paramlist',4,'p_paramlist','tokensAndGrammars.py',239),
  ('paramlist -> tipo declaraid','paramlist',2,'p_paramlist','tokensAndGrammars.py',240),
  ('bloque -> LEFTBRACKET mas_estatutos RIGHTBRACKET','bloque',3,'p_bloque','tokensAndGrammars.py',247),
  ('bloque -> LEFTBRACKET RIGHTBRACKET','bloque',2,'p_bloque','tokensAndGrammars.py',248),
  ('mas_estatutos -> estatuto mas_estatutos','mas_estatutos',2,'p_mas_estatutos','tokensAndGrammars.py',255),
  ('mas_estatutos -> estatuto','mas_estatutos',1,'p_mas_estatutos','tokensAndGrammars.py',256),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','tokensAndGrammars.py',263),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','tokensAndGrammars.py',264),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','tokensAndGrammars.py',265),
  ('estatuto -> decision','estatuto',1,'p_estatuto','tokensAndGrammars.py',266),
  ('estatuto -> repeticion','estatuto',1,'p_estatuto','tokensAndGrammars.py',267),
  ('asignacion -> id_dimensiones EQUALS expresion SEMICOLON','asignacion',4,'p_asignacion','tokensAndGrammars.py',275),
  ('lista_ids -> id_dimensiones COMMA lista_ids','lista_ids',3,'p_lista_ids','tokensAndGrammars.py',288),
  ('lista_ids -> id_dimensiones','lista_ids',1,'p_lista_ids','tokensAndGrammars.py',289),
  ('lectura -> READ LEFTPARENTHESIS lista_ids RIGHTPARENTHESIS SEMICOLON','lectura',5,'p_lectura','tokensAndGrammars.py',295),
  ('escritura -> WRITE LEFTPARENTHESIS poswrite RIGHTPARENTHESIS SEMICOLON','escritura',5,'p_escritura','tokensAndGrammars.py',302),
  ('poswrite -> CTESTRING COMMA poswrite','poswrite',3,'p_poswrite','tokensAndGrammars.py',309),
  ('poswrite -> expresion COMMA poswrite','poswrite',3,'p_poswrite','tokensAndGrammars.py',310),
  ('poswrite -> CTESTRING','poswrite',1,'p_poswrite','tokensAndGrammars.py',311),
  ('poswrite -> expresion','poswrite',1,'p_poswrite','tokensAndGrammars.py',312),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN bloque ELSE bloque','decision',8,'p_decision','tokensAndGrammars.py',319),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN bloque','decision',6,'p_decision','tokensAndGrammars.py',320),
  ('repeticion -> condicional bloque','repeticion',2,'p_repeticion','tokensAndGrammars.py',327),
  ('repeticion -> no_condicional bloque','repeticion',2,'p_repeticion','tokensAndGrammars.py',328),
  ('condicional -> WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO','condicional',5,'p_condicional','tokensAndGrammars.py',335),
  ('no_condicional -> FOR ID EQUALS exp TO exp DO','no_condicional',7,'p_no_condicional','tokensAndGrammars.py',342),
  ('expresion -> exp comparadores exp','expresion',3,'p_expresion','tokensAndGrammars.py',348),
  ('expresion -> exp','expresion',1,'p_expresion','tokensAndGrammars.py',349),
  ('comparadores -> COMPARISON','comparadores',1,'p_comparadores','tokensAndGrammars.py',356),
  ('comparadores -> GREATERHANOREQUAL','comparadores',1,'p_comparadores','tokensAndGrammars.py',357),
  ('comparadores -> LESSTHANOREQUAL','comparadores',1,'p_comparadores','tokensAndGrammars.py',358),
  ('comparadores -> GREATERTHAN','comparadores',1,'p_comparadores','tokensAndGrammars.py',359),
  ('comparadores -> LESSTHAN','comparadores',1,'p_comparadores','tokensAndGrammars.py',360),
  ('comparadores -> DIFFERENT','comparadores',1,'p_comparadores','tokensAndGrammars.py',361),
  ('exp -> termino opera_exp exp','exp',3,'p_exp','tokensAndGrammars.py',368),
  ('exp -> termino','exp',1,'p_exp','tokensAndGrammars.py',369),
  ('opera_exp -> PLUS','opera_exp',1,'p_opera_exp','tokensAndGrammars.py',376),
  ('opera_exp -> MINUS','opera_exp',1,'p_opera_exp','tokensAndGrammars.py',377),
  ('termino -> factor opera_term termino','termino',3,'p_termino','tokensAndGrammars.py',384),
  ('termino -> factor','termino',1,'p_termino','tokensAndGrammars.py',385),
  ('opera_term -> MULTIPLY','opera_term',1,'p_opera_term','tokensAndGrammars.py',392),
  ('opera_term -> DIVIDE','opera_term',1,'p_opera_term','tokensAndGrammars.py',393),
  ('factor -> LEFTPARENTHESIS expresion RIGHTPARENTHESIS','factor',3,'p_factor','tokensAndGrammars.py',400),
  ('factor -> opera_exp valor_opt','factor',2,'p_factor','tokensAndGrammars.py',401),
  ('factor -> valor_opt','factor',1,'p_factor','tokensAndGrammars.py',402),
  ('id_dimensiones -> ID dimen_expre dimen_expre','id_dimensiones',3,'p_id_dimensiones','tokensAndGrammars.py',409),
  ('id_dimensiones -> ID dimen_expre','id_dimensiones',2,'p_id_dimensiones','tokensAndGrammars.py',410),
  ('id_dimensiones -> ID','id_dimensiones',1,'p_id_dimensiones','tokensAndGrammars.py',411),
  ('dimen_expre -> LEFTSQRBRACKET expresion RIGHTSQRBRACKET','dimen_expre',3,'p_dimen_expre','tokensAndGrammars.py',418),
  ('valor_opt -> id_dimensiones','valor_opt',1,'p_valor_opt','tokensAndGrammars.py',425),
  ('valor_opt -> CTEINT','valor_opt',1,'p_valor_opt','tokensAndGrammars.py',426),
  ('valor_opt -> CTEFLOAT','valor_opt',1,'p_valor_opt','tokensAndGrammars.py',427),
]
