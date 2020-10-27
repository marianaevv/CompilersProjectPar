
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMMA COMPARISON CTECHAR CTEFLOAT CTEINT CTESTRING DECREMENT DIFFERENT DIVIDE DO ELSE EQUALS FLOAT FOR GREATERHANOREQUAL GREATERTHAN ID IF INCREMENT INT LEFTBRACKET LEFTPARENTHESIS LEFTSQRBRACKET LESSTHAN LESSTHANOREQUAL MAIN MINUS MOD MODULE MULTIPLY OR PLUS PLUSEQUALS PROGRAM READ RETURN RIGHTBRACKET RIGHTPARENTHESIS RIGHTSQRBRACKET SEMICOLON SUBSTRACTEQUALS THEN TO VAR VOID WHILE WRITE\n    program : PROGRAM ID SEMICOLON vars MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block\n            | PROGRAM ID SEMICOLON functions_list MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block\n            | PROGRAM ID SEMICOLON MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block\n    \n    data_type : INT\n              | FLOAT\n              | CHAR\n    \n    vars : VAR vars_lists\n    \n    vars_lists : data_type ids_list SEMICOLON vars_lists\n               | data_type ids_list SEMICOLON functions_list\n               | data_type ids_list SEMICOLON\n    \n    ids_list : identifier COMMA ids_list\n             | identifier\n    \n    identifier : ID id_dimensions id_dimensions\n               | ID id_dimensions\n               | ID\n    \n    id_dimensions : LEFTSQRBRACKET expresion RIGHTSQRBRACKET\n    \n    return_type : data_type\n                | VOID\n    \n    function : return_type MODULE ID parameters_list vars block\n             | return_type MODULE ID parameters_list block\n    \n    functions_list : function functions_list\n                   | function\n    \n    parameters_list : LEFTPARENTHESIS parameter RIGHTPARENTHESIS\n                    | LEFTPARENTHESIS RIGHTPARENTHESIS\n    \n    parameter : data_type identifier COMMA parameter\n              | data_type identifier\n    \n    comparators : COMPARISON\n                | GREATERHANOREQUAL\n                | LESSTHANOREQUAL\n                | GREATERTHAN\n                | LESSTHAN\n                | DIFFERENT\n                | OR\n                | AND\n    \n    exp_operator : PLUS\n                 | MINUS\n    \n    term_operator : MULTIPLY\n                  | DIVIDE\n                  | MOD\n    \n    block : LEFTBRACKET statutes_list RIGHTBRACKET\n          | LEFTBRACKET RIGHTBRACKET\n    \n    statutes_list : statute statutes_list\n                  | statute\n    \n    statute : asignation\n            | reading\n            | writing\n            | decision\n            | loop\n            | function_return\n            | function_call SEMICOLON\n    \n    asignation : identifier EQUALS expresion SEMICOLON\n               | identifier PLUSEQUALS expresion SEMICOLON\n               | identifier SUBSTRACTEQUALS expresion SEMICOLON\n               | identifier INCREMENT SEMICOLON\n               | identifier DECREMENT SEMICOLON\n    \n    reading : READ LEFTPARENTHESIS ids_list RIGHTPARENTHESIS SEMICOLON\n    \n    writing : WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON\n    \n    writing_list : CTESTRING COMMA writing_list\n                 | expresion COMMA writing_list\n                 | CTESTRING\n                 | expresion\n    \n    decision : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block ELSE block\n             | IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block\n    \n    loop : conditional block\n         | non_conditional block\n    \n    conditional : WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO\n    \n    non_conditional : FOR ID EQUALS exp TO exp DO\n    \n    function_return : RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON\n    \n    function_call : ID LEFTPARENTHESIS expresion_list RIGHTPARENTHESIS\n    \n    expresion_list : expresion COMMA expresion_list\n                   | expresion\n    \n    expresion : exp comparators exp\n              | exp\n    \n    exp : term exp_operator exp\n        | term\n    \n    term : factor term_operator term\n         | factor\n    \n    factor : LEFTPARENTHESIS expresion RIGHTPARENTHESIS\n           | exp_operator opt_value\n           | opt_value\n    \n    opt_value : CTEINT\n              | CTEFLOAT\n              | CTECHAR\n              | function_call\n              | identifier\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,31,40,42,61,86,],[0,-3,-1,-41,-2,-40,]),'ID':([2,13,14,15,20,22,32,35,37,42,43,44,45,46,47,48,49,60,62,70,72,74,75,85,86,88,89,90,91,94,95,96,97,98,99,100,101,104,105,106,107,108,109,110,111,112,113,115,116,117,118,126,127,137,143,144,145,148,149,153,157,158,162,165,166,170,],[3,-4,-5,-6,28,29,58,28,58,-41,58,-44,-45,-46,-47,-48,-49,102,28,58,58,-35,-36,28,-40,-50,58,58,58,28,58,58,-64,-65,58,58,58,58,-27,-28,-29,-30,-31,-32,-33,-34,58,58,-37,-38,-39,-54,-55,58,-51,-52,-53,58,58,58,-56,-57,-68,58,-63,-62,]),'SEMICOLON':([3,26,27,28,36,50,58,65,66,68,69,71,73,76,77,78,79,80,92,93,103,114,123,124,125,138,139,140,141,146,147,151,152,],[4,34,-12,-15,-14,88,-15,-11,-13,-73,-75,-77,-80,-81,-82,-83,-84,-85,126,127,-16,-79,143,144,145,-72,-74,-76,-78,157,158,162,-69,]),'MAIN':([4,5,7,9,19,21,34,42,63,64,82,86,120,],[6,16,18,-22,-7,-21,-10,-41,-8,-9,-20,-40,-19,]),'VAR':([4,38,84,121,],[8,8,-24,-23,]),'VOID':([4,9,34,42,82,86,120,],[12,12,12,-41,-20,-40,-19,]),'INT':([4,8,9,34,39,42,82,86,120,142,],[13,13,13,13,13,-41,-20,-40,-19,13,]),'FLOAT':([4,8,9,34,39,42,82,86,120,142,],[14,14,14,14,14,-41,-20,-40,-19,14,]),'CHAR':([4,8,9,34,39,42,82,86,120,142,],[15,15,15,15,15,-41,-20,-40,-19,15,]),'LEFTPARENTHESIS':([6,16,18,29,37,52,53,54,57,58,59,72,74,75,89,90,91,95,96,99,100,101,104,105,106,107,108,109,110,111,112,113,115,116,117,118,137,148,149,153,165,],[17,23,25,39,72,94,95,96,99,100,101,72,-35,-36,72,72,72,72,72,72,72,72,72,-27,-28,-29,-30,-31,-32,-33,-34,72,72,-37,-38,-39,72,72,72,72,72,]),'LEFTBRACKET':([9,19,21,24,30,33,34,38,42,55,56,63,64,81,82,84,86,120,121,161,164,168,169,],[-22,-7,-21,32,32,32,-10,32,-41,32,32,-8,-9,32,-20,-24,-40,-19,-23,32,-66,32,-67,]),'MODULE':([10,11,12,13,14,15,62,],[22,-17,-18,-4,-5,-6,-17,]),'RIGHTPARENTHESIS':([17,23,25,27,28,36,39,58,65,66,68,69,71,73,76,77,78,79,80,83,103,114,119,122,128,129,130,131,132,133,134,135,136,138,139,140,141,152,156,159,160,163,],[24,30,33,-12,-15,-14,84,-15,-11,-13,-73,-75,-77,-80,-81,-82,-83,-84,-85,121,-16,-79,141,-26,146,147,-60,-61,150,151,152,-71,154,-72,-74,-76,-78,-69,-25,-58,-59,-70,]),'COMMA':([27,28,36,58,66,68,69,71,73,76,77,78,79,80,103,114,122,130,131,135,138,139,140,141,152,],[35,-15,-14,-15,-13,-73,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,142,148,149,153,-72,-74,-76,-78,-69,]),'LEFTSQRBRACKET':([28,36,58,103,],[37,37,37,-16,]),'RIGHTBRACKET':([32,41,42,43,44,45,46,47,48,49,86,87,88,97,98,126,127,143,144,145,157,158,162,166,170,],[42,86,-41,-43,-44,-45,-46,-47,-48,-49,-40,-42,-50,-64,-65,-54,-55,-51,-52,-53,-56,-57,-68,-63,-62,]),'READ':([32,42,43,44,45,46,47,48,49,86,88,97,98,126,127,143,144,145,157,158,162,166,170,],[52,-41,52,-44,-45,-46,-47,-48,-49,-40,-50,-64,-65,-54,-55,-51,-52,-53,-56,-57,-68,-63,-62,]),'WRITE':([32,42,43,44,45,46,47,48,49,86,88,97,98,126,127,143,144,145,157,158,162,166,170,],[53,-41,53,-44,-45,-46,-47,-48,-49,-40,-50,-64,-65,-54,-55,-51,-52,-53,-56,-57,-68,-63,-62,]),'IF':([32,42,43,44,45,46,47,48,49,86,88,97,98,126,127,143,144,145,157,158,162,166,170,],[54,-41,54,-44,-45,-46,-47,-48,-49,-40,-50,-64,-65,-54,-55,-51,-52,-53,-56,-57,-68,-63,-62,]),'RETURN':([32,42,43,44,45,46,47,48,49,86,88,97,98,126,127,143,144,145,157,158,162,166,170,],[57,-41,57,-44,-45,-46,-47,-48,-49,-40,-50,-64,-65,-54,-55,-51,-52,-53,-56,-57,-68,-63,-62,]),'WHILE':([32,42,43,44,45,46,47,48,49,86,88,97,98,126,127,143,144,145,157,158,162,166,170,],[59,-41,59,-44,-45,-46,-47,-48,-49,-40,-50,-64,-65,-54,-55,-51,-52,-53,-56,-57,-68,-63,-62,]),'FOR':([32,42,43,44,45,46,47,48,49,86,88,97,98,126,127,143,144,145,157,158,162,166,170,],[60,-41,60,-44,-45,-46,-47,-48,-49,-40,-50,-64,-65,-54,-55,-51,-52,-53,-56,-57,-68,-63,-62,]),'EQUALS':([36,51,58,66,102,103,],[-14,89,-15,-13,137,-16,]),'PLUSEQUALS':([36,51,58,66,103,],[-14,90,-15,-13,-16,]),'SUBSTRACTEQUALS':([36,51,58,66,103,],[-14,91,-15,-13,-16,]),'INCREMENT':([36,51,58,66,103,],[-14,92,-15,-13,-16,]),'DECREMENT':([36,51,58,66,103,],[-14,93,-15,-13,-16,]),'MULTIPLY':([36,58,66,71,73,76,77,78,79,80,103,114,141,152,],[-14,-15,-13,116,-80,-81,-82,-83,-84,-85,-16,-79,-78,-69,]),'DIVIDE':([36,58,66,71,73,76,77,78,79,80,103,114,141,152,],[-14,-15,-13,117,-80,-81,-82,-83,-84,-85,-16,-79,-78,-69,]),'MOD':([36,58,66,71,73,76,77,78,79,80,103,114,141,152,],[-14,-15,-13,118,-80,-81,-82,-83,-84,-85,-16,-79,-78,-69,]),'PLUS':([36,37,58,66,69,71,72,73,74,75,76,77,78,79,80,89,90,91,95,96,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,137,140,141,148,149,152,153,165,],[-14,74,-15,-13,74,-77,74,-80,-35,-36,-81,-82,-83,-84,-85,74,74,74,74,74,74,74,74,-16,74,-27,-28,-29,-30,-31,-32,-33,-34,74,-79,74,-37,-38,-39,74,-76,-78,74,74,-69,74,74,]),'MINUS':([36,37,58,66,69,71,72,73,74,75,76,77,78,79,80,89,90,91,95,96,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,137,140,141,148,149,152,153,165,],[-14,75,-15,-13,75,-77,75,-80,-35,-36,-81,-82,-83,-84,-85,75,75,75,75,75,75,75,75,-16,75,-27,-28,-29,-30,-31,-32,-33,-34,75,-79,75,-37,-38,-39,75,-76,-78,75,75,-69,75,75,]),'COMPARISON':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,105,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'GREATERHANOREQUAL':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,106,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'LESSTHANOREQUAL':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,107,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'GREATERTHAN':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,108,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'LESSTHAN':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,109,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'DIFFERENT':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,110,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'OR':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,111,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'AND':([36,58,66,68,69,71,73,76,77,78,79,80,103,114,139,140,141,152,],[-14,-15,-13,112,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,]),'RIGHTSQRBRACKET':([36,58,66,67,68,69,71,73,76,77,78,79,80,103,114,138,139,140,141,152,],[-14,-15,-13,103,-73,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-72,-74,-76,-78,-69,]),'TO':([36,58,66,69,71,73,76,77,78,79,80,103,114,139,140,141,152,155,],[-14,-15,-13,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,165,]),'DO':([36,58,66,69,71,73,76,77,78,79,80,103,114,139,140,141,152,154,167,],[-14,-15,-13,-75,-77,-80,-81,-82,-83,-84,-85,-16,-79,-74,-76,-78,-69,164,169,]),'CTEINT':([37,70,72,74,75,89,90,91,95,96,99,100,101,104,105,106,107,108,109,110,111,112,113,115,116,117,118,137,148,149,153,165,],[76,76,76,-35,-36,76,76,76,76,76,76,76,76,76,-27,-28,-29,-30,-31,-32,-33,-34,76,76,-37,-38,-39,76,76,76,76,76,]),'CTEFLOAT':([37,70,72,74,75,89,90,91,95,96,99,100,101,104,105,106,107,108,109,110,111,112,113,115,116,117,118,137,148,149,153,165,],[77,77,77,-35,-36,77,77,77,77,77,77,77,77,77,-27,-28,-29,-30,-31,-32,-33,-34,77,77,-37,-38,-39,77,77,77,77,77,]),'CTECHAR':([37,70,72,74,75,89,90,91,95,96,99,100,101,104,105,106,107,108,109,110,111,112,113,115,116,117,118,137,148,149,153,165,],[78,78,78,-35,-36,78,78,78,78,78,78,78,78,78,-27,-28,-29,-30,-31,-32,-33,-34,78,78,-37,-38,-39,78,78,78,78,78,]),'ELSE':([42,86,166,],[-41,-40,168,]),'CTESTRING':([95,148,149,],[130,130,130,]),'THEN':([150,],[161,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([4,38,],[5,81,]),'functions_list':([4,9,34,],[7,21,64,]),'function':([4,9,34,],[9,9,9,]),'return_type':([4,9,34,],[10,10,10,]),'data_type':([4,8,9,34,39,142,],[11,20,11,62,85,85,]),'vars_lists':([8,34,],[19,63,]),'ids_list':([20,35,62,94,],[26,65,26,128,]),'identifier':([20,32,35,37,43,62,70,72,85,89,90,91,94,95,96,99,100,101,104,113,115,137,148,149,153,165,],[27,51,27,80,51,27,80,80,122,80,80,80,27,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'block':([24,30,33,38,55,56,81,161,168,],[31,40,61,82,97,98,120,166,170,]),'id_dimensions':([28,36,58,],[36,66,36,]),'parameters_list':([29,],[38,]),'statutes_list':([32,43,],[41,87,]),'statute':([32,43,],[43,43,]),'asignation':([32,43,],[44,44,]),'reading':([32,43,],[45,45,]),'writing':([32,43,],[46,46,]),'decision':([32,43,],[47,47,]),'loop':([32,43,],[48,48,]),'function_return':([32,43,],[49,49,]),'function_call':([32,37,43,70,72,89,90,91,95,96,99,100,101,104,113,115,137,148,149,153,165,],[50,79,50,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'conditional':([32,43,],[55,55,]),'non_conditional':([32,43,],[56,56,]),'expresion':([37,72,89,90,91,95,96,100,101,148,149,153,],[67,119,123,124,125,131,132,135,136,131,131,135,]),'exp':([37,72,89,90,91,95,96,99,100,101,104,113,137,148,149,153,165,],[68,68,68,68,68,68,68,133,68,68,138,139,155,68,68,68,167,]),'term':([37,72,89,90,91,95,96,99,100,101,104,113,115,137,148,149,153,165,],[69,69,69,69,69,69,69,69,69,69,69,69,140,69,69,69,69,69,]),'exp_operator':([37,69,72,89,90,91,95,96,99,100,101,104,113,115,137,148,149,153,165,],[70,113,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'factor':([37,72,89,90,91,95,96,99,100,101,104,113,115,137,148,149,153,165,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'opt_value':([37,70,72,89,90,91,95,96,99,100,101,104,113,115,137,148,149,153,165,],[73,114,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'parameter':([39,142,],[83,156,]),'comparators':([68,],[104,]),'term_operator':([71,],[115,]),'writing_list':([95,148,149,],[129,159,160,]),'expresion_list':([100,153,],[134,163,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON vars MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block','program',8,'p_program','tokensAndGrammars.py',160),
  ('program -> PROGRAM ID SEMICOLON functions_list MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block','program',8,'p_program','tokensAndGrammars.py',161),
  ('program -> PROGRAM ID SEMICOLON MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block','program',7,'p_program','tokensAndGrammars.py',162),
  ('data_type -> INT','data_type',1,'p_data_type','tokensAndGrammars.py',170),
  ('data_type -> FLOAT','data_type',1,'p_data_type','tokensAndGrammars.py',171),
  ('data_type -> CHAR','data_type',1,'p_data_type','tokensAndGrammars.py',172),
  ('vars -> VAR vars_lists','vars',2,'p_vars','tokensAndGrammars.py',179),
  ('vars_lists -> data_type ids_list SEMICOLON vars_lists','vars_lists',4,'p_vars_lists','tokensAndGrammars.py',186),
  ('vars_lists -> data_type ids_list SEMICOLON functions_list','vars_lists',4,'p_vars_lists','tokensAndGrammars.py',187),
  ('vars_lists -> data_type ids_list SEMICOLON','vars_lists',3,'p_vars_lists','tokensAndGrammars.py',188),
  ('ids_list -> identifier COMMA ids_list','ids_list',3,'p_ids_list','tokensAndGrammars.py',195),
  ('ids_list -> identifier','ids_list',1,'p_ids_list','tokensAndGrammars.py',196),
  ('identifier -> ID id_dimensions id_dimensions','identifier',3,'p_identifier','tokensAndGrammars.py',203),
  ('identifier -> ID id_dimensions','identifier',2,'p_identifier','tokensAndGrammars.py',204),
  ('identifier -> ID','identifier',1,'p_identifier','tokensAndGrammars.py',205),
  ('id_dimensions -> LEFTSQRBRACKET expresion RIGHTSQRBRACKET','id_dimensions',3,'p_id_dimensions','tokensAndGrammars.py',212),
  ('return_type -> data_type','return_type',1,'p_return_type','tokensAndGrammars.py',221),
  ('return_type -> VOID','return_type',1,'p_return_type','tokensAndGrammars.py',222),
  ('function -> return_type MODULE ID parameters_list vars block','function',6,'p_function','tokensAndGrammars.py',229),
  ('function -> return_type MODULE ID parameters_list block','function',5,'p_function','tokensAndGrammars.py',230),
  ('functions_list -> function functions_list','functions_list',2,'p_functions_list','tokensAndGrammars.py',236),
  ('functions_list -> function','functions_list',1,'p_functions_list','tokensAndGrammars.py',237),
  ('parameters_list -> LEFTPARENTHESIS parameter RIGHTPARENTHESIS','parameters_list',3,'p_parameters_list','tokensAndGrammars.py',244),
  ('parameters_list -> LEFTPARENTHESIS RIGHTPARENTHESIS','parameters_list',2,'p_parameters_list','tokensAndGrammars.py',245),
  ('parameter -> data_type identifier COMMA parameter','parameter',4,'p_parameter','tokensAndGrammars.py',252),
  ('parameter -> data_type identifier','parameter',2,'p_parameter','tokensAndGrammars.py',253),
  ('comparators -> COMPARISON','comparators',1,'p_comparators','tokensAndGrammars.py',261),
  ('comparators -> GREATERHANOREQUAL','comparators',1,'p_comparators','tokensAndGrammars.py',262),
  ('comparators -> LESSTHANOREQUAL','comparators',1,'p_comparators','tokensAndGrammars.py',263),
  ('comparators -> GREATERTHAN','comparators',1,'p_comparators','tokensAndGrammars.py',264),
  ('comparators -> LESSTHAN','comparators',1,'p_comparators','tokensAndGrammars.py',265),
  ('comparators -> DIFFERENT','comparators',1,'p_comparators','tokensAndGrammars.py',266),
  ('comparators -> OR','comparators',1,'p_comparators','tokensAndGrammars.py',267),
  ('comparators -> AND','comparators',1,'p_comparators','tokensAndGrammars.py',268),
  ('exp_operator -> PLUS','exp_operator',1,'p_exp_operator','tokensAndGrammars.py',275),
  ('exp_operator -> MINUS','exp_operator',1,'p_exp_operator','tokensAndGrammars.py',276),
  ('term_operator -> MULTIPLY','term_operator',1,'p_term_operator','tokensAndGrammars.py',283),
  ('term_operator -> DIVIDE','term_operator',1,'p_term_operator','tokensAndGrammars.py',284),
  ('term_operator -> MOD','term_operator',1,'p_term_operator','tokensAndGrammars.py',285),
  ('block -> LEFTBRACKET statutes_list RIGHTBRACKET','block',3,'p_block','tokensAndGrammars.py',293),
  ('block -> LEFTBRACKET RIGHTBRACKET','block',2,'p_block','tokensAndGrammars.py',294),
  ('statutes_list -> statute statutes_list','statutes_list',2,'p_statutes_list','tokensAndGrammars.py',301),
  ('statutes_list -> statute','statutes_list',1,'p_statutes_list','tokensAndGrammars.py',302),
  ('statute -> asignation','statute',1,'p_statute','tokensAndGrammars.py',309),
  ('statute -> reading','statute',1,'p_statute','tokensAndGrammars.py',310),
  ('statute -> writing','statute',1,'p_statute','tokensAndGrammars.py',311),
  ('statute -> decision','statute',1,'p_statute','tokensAndGrammars.py',312),
  ('statute -> loop','statute',1,'p_statute','tokensAndGrammars.py',313),
  ('statute -> function_return','statute',1,'p_statute','tokensAndGrammars.py',314),
  ('statute -> function_call SEMICOLON','statute',2,'p_statute','tokensAndGrammars.py',315),
  ('asignation -> identifier EQUALS expresion SEMICOLON','asignation',4,'p_asignation','tokensAndGrammars.py',322),
  ('asignation -> identifier PLUSEQUALS expresion SEMICOLON','asignation',4,'p_asignation','tokensAndGrammars.py',323),
  ('asignation -> identifier SUBSTRACTEQUALS expresion SEMICOLON','asignation',4,'p_asignation','tokensAndGrammars.py',324),
  ('asignation -> identifier INCREMENT SEMICOLON','asignation',3,'p_asignation','tokensAndGrammars.py',325),
  ('asignation -> identifier DECREMENT SEMICOLON','asignation',3,'p_asignation','tokensAndGrammars.py',326),
  ('reading -> READ LEFTPARENTHESIS ids_list RIGHTPARENTHESIS SEMICOLON','reading',5,'p_reading','tokensAndGrammars.py',333),
  ('writing -> WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON','writing',5,'p_writing','tokensAndGrammars.py',340),
  ('writing_list -> CTESTRING COMMA writing_list','writing_list',3,'p_writing_list','tokensAndGrammars.py',347),
  ('writing_list -> expresion COMMA writing_list','writing_list',3,'p_writing_list','tokensAndGrammars.py',348),
  ('writing_list -> CTESTRING','writing_list',1,'p_writing_list','tokensAndGrammars.py',349),
  ('writing_list -> expresion','writing_list',1,'p_writing_list','tokensAndGrammars.py',350),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block ELSE block','decision',8,'p_decision','tokensAndGrammars.py',357),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block','decision',6,'p_decision','tokensAndGrammars.py',358),
  ('loop -> conditional block','loop',2,'p_loop','tokensAndGrammars.py',365),
  ('loop -> non_conditional block','loop',2,'p_loop','tokensAndGrammars.py',366),
  ('conditional -> WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO','conditional',5,'p_conditional','tokensAndGrammars.py',373),
  ('non_conditional -> FOR ID EQUALS exp TO exp DO','non_conditional',7,'p_non_conditional','tokensAndGrammars.py',380),
  ('function_return -> RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON','function_return',5,'p_function_return','tokensAndGrammars.py',387),
  ('function_call -> ID LEFTPARENTHESIS expresion_list RIGHTPARENTHESIS','function_call',4,'p_function_call','tokensAndGrammars.py',393),
  ('expresion_list -> expresion COMMA expresion_list','expresion_list',3,'p_expresion_list','tokensAndGrammars.py',400),
  ('expresion_list -> expresion','expresion_list',1,'p_expresion_list','tokensAndGrammars.py',401),
  ('expresion -> exp comparators exp','expresion',3,'p_expresion','tokensAndGrammars.py',408),
  ('expresion -> exp','expresion',1,'p_expresion','tokensAndGrammars.py',409),
  ('exp -> term exp_operator exp','exp',3,'p_exp','tokensAndGrammars.py',416),
  ('exp -> term','exp',1,'p_exp','tokensAndGrammars.py',417),
  ('term -> factor term_operator term','term',3,'p_term','tokensAndGrammars.py',424),
  ('term -> factor','term',1,'p_term','tokensAndGrammars.py',425),
  ('factor -> LEFTPARENTHESIS expresion RIGHTPARENTHESIS','factor',3,'p_factor','tokensAndGrammars.py',432),
  ('factor -> exp_operator opt_value','factor',2,'p_factor','tokensAndGrammars.py',433),
  ('factor -> opt_value','factor',1,'p_factor','tokensAndGrammars.py',434),
  ('opt_value -> CTEINT','opt_value',1,'p_opt_value','tokensAndGrammars.py',441),
  ('opt_value -> CTEFLOAT','opt_value',1,'p_opt_value','tokensAndGrammars.py',442),
  ('opt_value -> CTECHAR','opt_value',1,'p_opt_value','tokensAndGrammars.py',443),
  ('opt_value -> function_call','opt_value',1,'p_opt_value','tokensAndGrammars.py',444),
  ('opt_value -> identifier','opt_value',1,'p_opt_value','tokensAndGrammars.py',445),
]
