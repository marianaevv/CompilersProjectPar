
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMMA COMPARISON CTECHAR CTEFLOAT CTEINT CTESTRING DECREMENT DIFFERENT DIVIDE DO ELSE EQUALS FLOAT FOR GREATERHANOREQUAL GREATERTHAN ID IF INCREMENT INT LEFTBRACKET LEFTPARENTHESIS LEFTSQRBRACKET LESSTHAN LESSTHANOREQUAL MAIN MINUS MOD MODULE MULTIPLY OR PLUS PLUSEQUALS PROGRAM READ RETURN RIGHTBRACKET RIGHTPARENTHESIS RIGHTSQRBRACKET SEMICOLON SUBSTRACTEQUALS THEN TO VAR VOID WHILE WRITE\n    program : PROGRAM ID SEMICOLON vars functions_list neupoint_back_global MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block\n            | PROGRAM ID SEMICOLON vars MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block\n            | PROGRAM ID SEMICOLON functions_list neupoint_back_global MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block\n            | PROGRAM ID SEMICOLON MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block\n    \n    data_type : INT\n              | FLOAT\n              | CHAR\n    \n    vars : VAR vars_lists neupoint_add_vars\n    \n    vars_lists : data_type decla_ids_list SEMICOLON vars_lists\n               | data_type decla_ids_list SEMICOLON\n    \n    decla_ids_list : decla_identifier COMMA decla_ids_list\n                   | decla_identifier\n    \n    decla_identifier : ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET\n                     | ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET\n                     | ID\n    \n    ids_list : identifier COMMA ids_list\n             | identifier\n    \n    identifier : ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET LEFTSQRBRACKET expresion RIGHTSQRBRACKET\n               | ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET\n               | ID\n    \n    neupoint_add_vars :\n    \n    return_type : data_type\n                | VOID\n    \n    functions_list : function functions_list\n                   | function\n    \n    function : MODULE return_type ID neupoint_add_function parameters_list vars block\n             | MODULE return_type ID neupoint_add_function parameters_list block\n    \n    parameters_list : LEFTPARENTHESIS parameter RIGHTPARENTHESIS neupoint_add_parameters\n                    | LEFTPARENTHESIS RIGHTPARENTHESIS\n    \n    parameter : data_type decla_identifier COMMA parameter\n              | data_type decla_identifier\n    \n    neupoint_add_function : \n    \n    neupoint_add_parameters :\n    \n    neupoint_back_global : \n    \n    comparators : COMPARISON\n                | GREATERHANOREQUAL\n                | LESSTHANOREQUAL\n                | GREATERTHAN\n                | LESSTHAN\n                | DIFFERENT\n                | OR\n                | AND\n    \n    exp_operator : PLUS\n                 | MINUS\n    \n    term_operator : MULTIPLY\n                  | DIVIDE\n                  | MOD\n    \n    block : LEFTBRACKET statutes_list RIGHTBRACKET\n          | LEFTBRACKET RIGHTBRACKET\n    \n    statutes_list : statute statutes_list\n                  | statute\n    \n    statute : assignment\n            | reading\n            | writing\n            | decision\n            | loop\n            | function_return\n            | function_call SEMICOLON\n    \n    assignment : identifier neupoint_add_operand EQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON\n               | identifier neupoint_add_operand PLUSEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON\n               | identifier neupoint_add_operand SUBSTRACTEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON\n               | identifier neupoint_add_operand INCREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON\n               | identifier neupoint_add_operand DECREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON\n    \n    reading : READ LEFTPARENTHESIS ids_list RIGHTPARENTHESIS SEMICOLON\n    \n    writing : WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON\n    \n    writing_list : CTESTRING COMMA writing_list\n                 | expresion COMMA writing_list\n                 | CTESTRING\n                 | expresion\n    \n    decision : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block ELSE block\n             | IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block\n    \n    loop : conditional block\n         | non_conditional block\n    \n    conditional : WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO\n    \n    non_conditional : FOR ID EQUALS exp TO exp DO\n    \n    function_return : RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON\n    \n    function_call : ID LEFTPARENTHESIS expresion_list RIGHTPARENTHESIS\n    \n    expresion_list : expresion COMMA expresion_list\n                   | expresion\n    \n    expresion : exp comparators neupoint_add_operator exp\n              | exp\n    \n    exp : term neupoint_arithmetic_exp_quad exp_operator neupoint_add_operator exp\n        | term neupoint_arithmetic_exp_quad\n    \n    term : factor neupoint_arithmetic_term_quad term_operator neupoint_add_operator term\n         | factor neupoint_arithmetic_term_quad\n    \n    factor : LEFTPARENTHESIS neupoint_add_wall expresion neupoint_remove_wall RIGHTPARENTHESIS\n           | CTEINT neupoint_add_cte_operand\n           | CTEFLOAT neupoint_add_cte_operand\n           | CTECHAR neupoint_add_cte_operand\n           | function_call\n           | identifier neupoint_add_operand\n    \n    neupoint_add_operator : \n    \n    neupoint_add_operand : \n    \n    neupoint_add_cte_operand : \n    \n    neupoint_arithmetic_exp_quad : \n    \n    neupoint_arithmetic_term_quad : \n    \n    neupoint_add_wall : \n    \n    neupoint_remove_wall : \n    \n    neupoint_assignment_quad : \n    \n    neupoint_assignment_single_quad : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,36,43,46,71,72,92,],[0,-4,-2,-49,-3,-48,-1,]),'ID':([2,16,17,18,19,21,22,23,37,39,46,47,48,49,50,51,52,53,64,72,74,76,77,78,79,80,81,82,83,84,91,93,94,95,101,119,124,125,126,130,131,133,134,135,136,137,138,139,140,141,142,143,153,165,168,171,172,173,174,175,176,177,178,180,182,184,190,191,194,195,196,199,200,201,208,],[3,31,-5,-6,-7,32,-22,-23,62,31,-49,62,-52,-53,-54,-55,-56,-57,85,-48,-58,100,62,62,-72,-73,62,62,62,62,31,-92,-92,-92,-97,62,62,62,62,100,62,62,62,-92,-35,-36,-37,-38,-39,-40,-41,-42,62,-64,-65,62,-92,-43,-44,-92,-45,-46,-47,-76,62,62,-62,-63,62,62,-71,-59,-60,-61,-70,]),'SEMICOLON':([3,29,30,31,54,62,66,86,96,97,105,106,107,108,109,110,111,112,127,128,129,132,144,145,146,147,148,149,151,152,154,160,161,162,163,164,185,187,188,189,193,202,203,204,206,],[4,38,-12,-15,74,-20,-11,-14,-92,-92,-81,-95,-96,-94,-94,-94,-90,-93,-100,-100,165,168,-83,-85,-87,-88,-89,-91,180,-77,-19,-99,-99,-99,190,191,-13,199,200,201,-80,-86,-82,-84,-18,]),'MAIN':([4,5,6,9,11,13,15,20,24,28,38,46,65,72,88,121,],[7,12,-34,-25,-34,26,-21,-24,33,-8,-10,-49,-9,-48,-27,-26,]),'VAR':([4,68,90,122,158,],[8,8,-29,-33,-28,]),'MODULE':([4,5,9,15,28,38,46,65,72,88,121,],[10,10,10,-21,-8,-10,-49,-9,-48,-27,-26,]),'LEFTPARENTHESIS':([7,12,26,32,33,41,56,57,58,61,62,63,77,78,81,82,83,84,93,94,95,101,119,124,125,126,131,133,134,135,136,137,138,139,140,141,142,143,153,171,172,173,174,175,176,177,178,182,184,194,195,],[14,25,35,-32,42,69,76,77,78,81,82,84,101,101,101,101,101,101,-92,-92,-92,-97,101,101,101,101,101,101,101,-92,-35,-36,-37,-38,-39,-40,-41,-42,101,101,-92,-43,-44,-92,-45,-46,-47,101,101,101,101,]),'INT':([8,10,38,69,159,],[17,17,17,17,17,]),'FLOAT':([8,10,38,69,159,],[18,18,18,18,18,]),'CHAR':([8,10,38,69,159,],[19,19,19,19,19,]),'VOID':([10,],[23,]),'RIGHTPARENTHESIS':([14,25,31,35,42,62,69,86,89,98,99,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,118,123,144,145,146,147,148,149,152,154,166,167,169,170,181,185,186,192,193,202,203,204,206,],[27,34,-15,44,70,-20,90,-14,122,129,-17,-20,132,-68,-69,-81,-95,-96,-94,-94,-94,-90,-93,150,151,152,-79,155,-31,-83,-85,-87,-88,-89,-91,-77,-19,-16,-98,-66,-67,-78,-13,-30,202,-80,-86,-82,-84,-18,]),'LEFTBRACKET':([15,27,28,34,38,44,59,60,65,68,70,87,90,122,158,179,183,205,207,],[-21,37,-8,37,-10,37,37,37,-9,37,37,37,-29,-33,-28,37,-74,37,-75,]),'COMMA':([30,31,62,86,99,100,103,104,105,106,107,108,109,110,111,112,116,123,144,145,146,147,148,149,152,154,185,193,202,203,204,206,],[39,-15,-20,-14,130,-20,133,134,-81,-95,-96,-94,-94,-94,-90,-93,153,159,-83,-85,-87,-88,-89,-91,-77,-19,-13,-80,-86,-82,-84,-18,]),'LEFTSQRBRACKET':([31,62,86,100,154,],[40,83,120,83,182,]),'RIGHTBRACKET':([37,45,46,47,48,49,50,51,52,53,72,73,74,79,80,165,168,180,190,191,196,199,200,201,208,],[46,72,-49,-51,-52,-53,-54,-55,-56,-57,-48,-50,-58,-72,-73,-64,-65,-76,-62,-63,-71,-59,-60,-61,-70,]),'READ':([37,46,47,48,49,50,51,52,53,72,74,79,80,165,168,180,190,191,196,199,200,201,208,],[56,-49,56,-52,-53,-54,-55,-56,-57,-48,-58,-72,-73,-64,-65,-76,-62,-63,-71,-59,-60,-61,-70,]),'WRITE':([37,46,47,48,49,50,51,52,53,72,74,79,80,165,168,180,190,191,196,199,200,201,208,],[57,-49,57,-52,-53,-54,-55,-56,-57,-48,-58,-72,-73,-64,-65,-76,-62,-63,-71,-59,-60,-61,-70,]),'IF':([37,46,47,48,49,50,51,52,53,72,74,79,80,165,168,180,190,191,196,199,200,201,208,],[58,-49,58,-52,-53,-54,-55,-56,-57,-48,-58,-72,-73,-64,-65,-76,-62,-63,-71,-59,-60,-61,-70,]),'RETURN':([37,46,47,48,49,50,51,52,53,72,74,79,80,165,168,180,190,191,196,199,200,201,208,],[61,-49,61,-52,-53,-54,-55,-56,-57,-48,-58,-72,-73,-64,-65,-76,-62,-63,-71,-59,-60,-61,-70,]),'WHILE':([37,46,47,48,49,50,51,52,53,72,74,79,80,165,168,180,190,191,196,199,200,201,208,],[63,-49,63,-52,-53,-54,-55,-56,-57,-48,-58,-72,-73,-64,-65,-76,-62,-63,-71,-59,-60,-61,-70,]),'FOR':([37,46,47,48,49,50,51,52,53,72,74,79,80,165,168,180,190,191,196,199,200,201,208,],[64,-49,64,-52,-53,-54,-55,-56,-57,-48,-58,-72,-73,-64,-65,-76,-62,-63,-71,-59,-60,-61,-70,]),'CTEINT':([40,77,78,81,82,83,84,93,94,95,101,119,120,124,125,126,131,133,134,135,136,137,138,139,140,141,142,143,153,171,172,173,174,175,176,177,178,182,184,194,195,],[67,108,108,108,108,108,108,-92,-92,-92,-97,108,157,108,108,108,108,108,108,-92,-35,-36,-37,-38,-39,-40,-41,-42,108,108,-92,-43,-44,-92,-45,-46,-47,108,108,108,108,]),'ELSE':([46,72,196,],[-49,-48,205,]),'EQUALS':([55,62,75,85,154,206,],[-93,-20,93,119,-19,-18,]),'PLUSEQUALS':([55,62,75,154,206,],[-93,-20,94,-19,-18,]),'SUBSTRACTEQUALS':([55,62,75,154,206,],[-93,-20,95,-19,-18,]),'INCREMENT':([55,62,75,154,206,],[-93,-20,96,-19,-18,]),'DECREMENT':([55,62,75,154,206,],[-93,-20,97,-19,-18,]),'MULTIPLY':([62,107,108,109,110,111,112,145,146,147,148,149,152,154,202,206,],[-20,-96,-94,-94,-94,-90,-93,176,-87,-88,-89,-91,-77,-19,-86,-18,]),'DIVIDE':([62,107,108,109,110,111,112,145,146,147,148,149,152,154,202,206,],[-20,-96,-94,-94,-94,-90,-93,177,-87,-88,-89,-91,-77,-19,-86,-18,]),'MOD':([62,107,108,109,110,111,112,145,146,147,148,149,152,154,202,206,],[-20,-96,-94,-94,-94,-90,-93,178,-87,-88,-89,-91,-77,-19,-86,-18,]),'PLUS':([62,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,204,206,],[-20,-95,-96,-94,-94,-94,-90,-93,173,-85,-87,-88,-89,-91,-77,-19,-86,-84,-18,]),'MINUS':([62,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,204,206,],[-20,-95,-96,-94,-94,-94,-90,-93,174,-85,-87,-88,-89,-91,-77,-19,-86,-84,-18,]),'COMPARISON':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,136,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'GREATERHANOREQUAL':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,137,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'LESSTHANOREQUAL':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,138,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'GREATERTHAN':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,139,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'LESSTHAN':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,140,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'DIFFERENT':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,141,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'OR':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,142,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'AND':([62,105,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,202,203,204,206,],[-20,143,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,-86,-82,-84,-18,]),'RIGHTSQRBRACKET':([62,67,105,106,107,108,109,110,111,112,117,144,145,146,147,148,149,152,154,157,193,197,202,203,204,206,],[-20,86,-81,-95,-96,-94,-94,-94,-90,-93,154,-83,-85,-87,-88,-89,-91,-77,-19,185,-80,206,-86,-82,-84,-18,]),'TO':([62,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,156,202,203,204,206,],[-20,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,184,-86,-82,-84,-18,]),'DO':([62,106,107,108,109,110,111,112,144,145,146,147,148,149,152,154,155,198,202,203,204,206,],[-20,-95,-96,-94,-94,-94,-90,-93,-83,-85,-87,-88,-89,-91,-77,-19,183,207,-86,-82,-84,-18,]),'CTESTRING':([77,133,134,],[103,103,103,]),'CTEFLOAT':([77,78,81,82,83,84,93,94,95,101,119,124,125,126,131,133,134,135,136,137,138,139,140,141,142,143,153,171,172,173,174,175,176,177,178,182,184,194,195,],[109,109,109,109,109,109,-92,-92,-92,-97,109,109,109,109,109,109,109,-92,-35,-36,-37,-38,-39,-40,-41,-42,109,109,-92,-43,-44,-92,-45,-46,-47,109,109,109,109,]),'CTECHAR':([77,78,81,82,83,84,93,94,95,101,119,124,125,126,131,133,134,135,136,137,138,139,140,141,142,143,153,171,172,173,174,175,176,177,178,182,184,194,195,],[110,110,110,110,110,110,-92,-92,-92,-97,110,110,110,110,110,110,110,-92,-35,-36,-37,-38,-39,-40,-41,-42,110,110,-92,-43,-44,-92,-45,-46,-47,110,110,110,110,]),'THEN':([150,],[179,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([4,68,],[5,87,]),'functions_list':([4,5,9,],[6,11,20,]),'function':([4,5,9,],[9,9,9,]),'neupoint_back_global':([6,11,],[13,24,]),'vars_lists':([8,38,],[15,65,]),'data_type':([8,10,38,69,159,],[16,22,16,91,91,]),'return_type':([10,],[21,]),'neupoint_add_vars':([15,],[28,]),'decla_ids_list':([16,39,],[29,66,]),'decla_identifier':([16,39,91,],[30,30,123,]),'block':([27,34,44,59,60,68,70,87,179,205,],[36,43,71,79,80,88,92,121,196,208,]),'neupoint_add_function':([32,],[41,]),'statutes_list':([37,47,],[45,73,]),'statute':([37,47,],[47,47,]),'assignment':([37,47,],[48,48,]),'reading':([37,47,],[49,49,]),'writing':([37,47,],[50,50,]),'decision':([37,47,],[51,51,]),'loop':([37,47,],[52,52,]),'function_return':([37,47,],[53,53,]),'function_call':([37,47,77,78,81,82,83,84,119,124,125,126,131,133,134,153,171,182,184,194,195,],[54,54,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'identifier':([37,47,76,77,78,81,82,83,84,119,124,125,126,130,131,133,134,153,171,182,184,194,195,],[55,55,99,112,112,112,112,112,112,112,112,112,112,99,112,112,112,112,112,112,112,112,112,]),'conditional':([37,47,],[59,59,]),'non_conditional':([37,47,],[60,60,]),'parameters_list':([41,],[68,]),'neupoint_add_operand':([55,112,],[75,149,]),'parameter':([69,159,],[89,186,]),'ids_list':([76,130,],[98,166,]),'writing_list':([77,133,134,],[102,169,170,]),'expresion':([77,78,82,83,84,124,125,126,131,133,134,153,182,],[104,113,116,117,118,160,161,162,167,104,104,116,197,]),'exp':([77,78,81,82,83,84,119,124,125,126,131,133,134,153,171,182,184,194,],[105,105,114,105,105,105,156,105,105,105,105,105,105,105,193,105,198,203,]),'term':([77,78,81,82,83,84,119,124,125,126,131,133,134,153,171,182,184,194,195,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,204,]),'factor':([77,78,81,82,83,84,119,124,125,126,131,133,134,153,171,182,184,194,195,],[107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'expresion_list':([82,153,],[115,181,]),'neupoint_add_operator':([93,94,95,96,97,135,172,175,],[124,125,126,127,128,171,194,195,]),'neupoint_add_wall':([101,],[131,]),'comparators':([105,],[135,]),'neupoint_arithmetic_exp_quad':([106,],[144,]),'neupoint_arithmetic_term_quad':([107,],[145,]),'neupoint_add_cte_operand':([108,109,110,],[146,147,148,]),'neupoint_add_parameters':([122,],[158,]),'neupoint_assignment_single_quad':([127,128,],[163,164,]),'exp_operator':([144,],[172,]),'term_operator':([145,],[175,]),'neupoint_assignment_quad':([160,161,162,],[187,188,189,]),'neupoint_remove_wall':([167,],[192,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON vars functions_list neupoint_back_global MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block','program',10,'p_program','tokensAndGrammars.py',168),
  ('program -> PROGRAM ID SEMICOLON vars MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block','program',8,'p_program','tokensAndGrammars.py',169),
  ('program -> PROGRAM ID SEMICOLON functions_list neupoint_back_global MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block','program',9,'p_program','tokensAndGrammars.py',170),
  ('program -> PROGRAM ID SEMICOLON MAIN LEFTPARENTHESIS RIGHTPARENTHESIS block','program',7,'p_program','tokensAndGrammars.py',171),
  ('data_type -> INT','data_type',1,'p_data_type','tokensAndGrammars.py',178),
  ('data_type -> FLOAT','data_type',1,'p_data_type','tokensAndGrammars.py',179),
  ('data_type -> CHAR','data_type',1,'p_data_type','tokensAndGrammars.py',180),
  ('vars -> VAR vars_lists neupoint_add_vars','vars',3,'p_vars','tokensAndGrammars.py',187),
  ('vars_lists -> data_type decla_ids_list SEMICOLON vars_lists','vars_lists',4,'p_vars_lists','tokensAndGrammars.py',194),
  ('vars_lists -> data_type decla_ids_list SEMICOLON','vars_lists',3,'p_vars_lists','tokensAndGrammars.py',195),
  ('decla_ids_list -> decla_identifier COMMA decla_ids_list','decla_ids_list',3,'p_decla_ids_list','tokensAndGrammars.py',209),
  ('decla_ids_list -> decla_identifier','decla_ids_list',1,'p_decla_ids_list','tokensAndGrammars.py',210),
  ('decla_identifier -> ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET','decla_identifier',7,'p_decla_identifier','tokensAndGrammars.py',221),
  ('decla_identifier -> ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET','decla_identifier',4,'p_decla_identifier','tokensAndGrammars.py',222),
  ('decla_identifier -> ID','decla_identifier',1,'p_decla_identifier','tokensAndGrammars.py',223),
  ('ids_list -> identifier COMMA ids_list','ids_list',3,'p_ids_list','tokensAndGrammars.py',236),
  ('ids_list -> identifier','ids_list',1,'p_ids_list','tokensAndGrammars.py',237),
  ('identifier -> ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET LEFTSQRBRACKET expresion RIGHTSQRBRACKET','identifier',7,'p_identifier','tokensAndGrammars.py',244),
  ('identifier -> ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET','identifier',4,'p_identifier','tokensAndGrammars.py',245),
  ('identifier -> ID','identifier',1,'p_identifier','tokensAndGrammars.py',246),
  ('neupoint_add_vars -> <empty>','neupoint_add_vars',0,'p_neupoint_add_vars','tokensAndGrammars.py',254),
  ('return_type -> data_type','return_type',1,'p_return_type','tokensAndGrammars.py',262),
  ('return_type -> VOID','return_type',1,'p_return_type','tokensAndGrammars.py',263),
  ('functions_list -> function functions_list','functions_list',2,'p_functions_list','tokensAndGrammars.py',270),
  ('functions_list -> function','functions_list',1,'p_functions_list','tokensAndGrammars.py',271),
  ('function -> MODULE return_type ID neupoint_add_function parameters_list vars block','function',7,'p_function','tokensAndGrammars.py',278),
  ('function -> MODULE return_type ID neupoint_add_function parameters_list block','function',6,'p_function','tokensAndGrammars.py',279),
  ('parameters_list -> LEFTPARENTHESIS parameter RIGHTPARENTHESIS neupoint_add_parameters','parameters_list',4,'p_parameters_list','tokensAndGrammars.py',298),
  ('parameters_list -> LEFTPARENTHESIS RIGHTPARENTHESIS','parameters_list',2,'p_parameters_list','tokensAndGrammars.py',299),
  ('parameter -> data_type decla_identifier COMMA parameter','parameter',4,'p_parameter','tokensAndGrammars.py',306),
  ('parameter -> data_type decla_identifier','parameter',2,'p_parameter','tokensAndGrammars.py',307),
  ('neupoint_add_function -> <empty>','neupoint_add_function',0,'p_neupoint_add_function','tokensAndGrammars.py',332),
  ('neupoint_add_parameters -> <empty>','neupoint_add_parameters',0,'p_neupoint_add_parameters','tokensAndGrammars.py',341),
  ('neupoint_back_global -> <empty>','neupoint_back_global',0,'p_neupoint_back_global','tokensAndGrammars.py',348),
  ('comparators -> COMPARISON','comparators',1,'p_comparators','tokensAndGrammars.py',356),
  ('comparators -> GREATERHANOREQUAL','comparators',1,'p_comparators','tokensAndGrammars.py',357),
  ('comparators -> LESSTHANOREQUAL','comparators',1,'p_comparators','tokensAndGrammars.py',358),
  ('comparators -> GREATERTHAN','comparators',1,'p_comparators','tokensAndGrammars.py',359),
  ('comparators -> LESSTHAN','comparators',1,'p_comparators','tokensAndGrammars.py',360),
  ('comparators -> DIFFERENT','comparators',1,'p_comparators','tokensAndGrammars.py',361),
  ('comparators -> OR','comparators',1,'p_comparators','tokensAndGrammars.py',362),
  ('comparators -> AND','comparators',1,'p_comparators','tokensAndGrammars.py',363),
  ('exp_operator -> PLUS','exp_operator',1,'p_exp_operator','tokensAndGrammars.py',370),
  ('exp_operator -> MINUS','exp_operator',1,'p_exp_operator','tokensAndGrammars.py',371),
  ('term_operator -> MULTIPLY','term_operator',1,'p_term_operator','tokensAndGrammars.py',378),
  ('term_operator -> DIVIDE','term_operator',1,'p_term_operator','tokensAndGrammars.py',379),
  ('term_operator -> MOD','term_operator',1,'p_term_operator','tokensAndGrammars.py',380),
  ('block -> LEFTBRACKET statutes_list RIGHTBRACKET','block',3,'p_block','tokensAndGrammars.py',388),
  ('block -> LEFTBRACKET RIGHTBRACKET','block',2,'p_block','tokensAndGrammars.py',389),
  ('statutes_list -> statute statutes_list','statutes_list',2,'p_statutes_list','tokensAndGrammars.py',396),
  ('statutes_list -> statute','statutes_list',1,'p_statutes_list','tokensAndGrammars.py',397),
  ('statute -> assignment','statute',1,'p_statute','tokensAndGrammars.py',404),
  ('statute -> reading','statute',1,'p_statute','tokensAndGrammars.py',405),
  ('statute -> writing','statute',1,'p_statute','tokensAndGrammars.py',406),
  ('statute -> decision','statute',1,'p_statute','tokensAndGrammars.py',407),
  ('statute -> loop','statute',1,'p_statute','tokensAndGrammars.py',408),
  ('statute -> function_return','statute',1,'p_statute','tokensAndGrammars.py',409),
  ('statute -> function_call SEMICOLON','statute',2,'p_statute','tokensAndGrammars.py',410),
  ('assignment -> identifier neupoint_add_operand EQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON','assignment',7,'p_assignment','tokensAndGrammars.py',417),
  ('assignment -> identifier neupoint_add_operand PLUSEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON','assignment',7,'p_assignment','tokensAndGrammars.py',418),
  ('assignment -> identifier neupoint_add_operand SUBSTRACTEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON','assignment',7,'p_assignment','tokensAndGrammars.py',419),
  ('assignment -> identifier neupoint_add_operand INCREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON','assignment',6,'p_assignment','tokensAndGrammars.py',420),
  ('assignment -> identifier neupoint_add_operand DECREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON','assignment',6,'p_assignment','tokensAndGrammars.py',421),
  ('reading -> READ LEFTPARENTHESIS ids_list RIGHTPARENTHESIS SEMICOLON','reading',5,'p_reading','tokensAndGrammars.py',428),
  ('writing -> WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON','writing',5,'p_writing','tokensAndGrammars.py',435),
  ('writing_list -> CTESTRING COMMA writing_list','writing_list',3,'p_writing_list','tokensAndGrammars.py',442),
  ('writing_list -> expresion COMMA writing_list','writing_list',3,'p_writing_list','tokensAndGrammars.py',443),
  ('writing_list -> CTESTRING','writing_list',1,'p_writing_list','tokensAndGrammars.py',444),
  ('writing_list -> expresion','writing_list',1,'p_writing_list','tokensAndGrammars.py',445),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block ELSE block','decision',8,'p_decision','tokensAndGrammars.py',452),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS THEN block','decision',6,'p_decision','tokensAndGrammars.py',453),
  ('loop -> conditional block','loop',2,'p_loop','tokensAndGrammars.py',460),
  ('loop -> non_conditional block','loop',2,'p_loop','tokensAndGrammars.py',461),
  ('conditional -> WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS DO','conditional',5,'p_conditional','tokensAndGrammars.py',468),
  ('non_conditional -> FOR ID EQUALS exp TO exp DO','non_conditional',7,'p_non_conditional','tokensAndGrammars.py',475),
  ('function_return -> RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON','function_return',5,'p_function_return','tokensAndGrammars.py',482),
  ('function_call -> ID LEFTPARENTHESIS expresion_list RIGHTPARENTHESIS','function_call',4,'p_function_call','tokensAndGrammars.py',490),
  ('expresion_list -> expresion COMMA expresion_list','expresion_list',3,'p_expresion_list','tokensAndGrammars.py',497),
  ('expresion_list -> expresion','expresion_list',1,'p_expresion_list','tokensAndGrammars.py',498),
  ('expresion -> exp comparators neupoint_add_operator exp','expresion',4,'p_expresion','tokensAndGrammars.py',505),
  ('expresion -> exp','expresion',1,'p_expresion','tokensAndGrammars.py',506),
  ('exp -> term neupoint_arithmetic_exp_quad exp_operator neupoint_add_operator exp','exp',5,'p_exp','tokensAndGrammars.py',513),
  ('exp -> term neupoint_arithmetic_exp_quad','exp',2,'p_exp','tokensAndGrammars.py',514),
  ('term -> factor neupoint_arithmetic_term_quad term_operator neupoint_add_operator term','term',5,'p_term','tokensAndGrammars.py',521),
  ('term -> factor neupoint_arithmetic_term_quad','term',2,'p_term','tokensAndGrammars.py',522),
  ('factor -> LEFTPARENTHESIS neupoint_add_wall expresion neupoint_remove_wall RIGHTPARENTHESIS','factor',5,'p_factor','tokensAndGrammars.py',529),
  ('factor -> CTEINT neupoint_add_cte_operand','factor',2,'p_factor','tokensAndGrammars.py',530),
  ('factor -> CTEFLOAT neupoint_add_cte_operand','factor',2,'p_factor','tokensAndGrammars.py',531),
  ('factor -> CTECHAR neupoint_add_cte_operand','factor',2,'p_factor','tokensAndGrammars.py',532),
  ('factor -> function_call','factor',1,'p_factor','tokensAndGrammars.py',533),
  ('factor -> identifier neupoint_add_operand','factor',2,'p_factor','tokensAndGrammars.py',534),
  ('neupoint_add_operator -> <empty>','neupoint_add_operator',0,'p_neupoint_add_operator','tokensAndGrammars.py',541),
  ('neupoint_add_operand -> <empty>','neupoint_add_operand',0,'p_neupoint_add_operand','tokensAndGrammars.py',548),
  ('neupoint_add_cte_operand -> <empty>','neupoint_add_cte_operand',0,'p_neupoint_add_cte_operand','tokensAndGrammars.py',561),
  ('neupoint_arithmetic_exp_quad -> <empty>','neupoint_arithmetic_exp_quad',0,'p_neupoint_arithmetic_exp_quad','tokensAndGrammars.py',575),
  ('neupoint_arithmetic_term_quad -> <empty>','neupoint_arithmetic_term_quad',0,'p_neupoint_arithmetic_term_quad','tokensAndGrammars.py',584),
  ('neupoint_add_wall -> <empty>','neupoint_add_wall',0,'p_neupoint_add_wall','tokensAndGrammars.py',593),
  ('neupoint_remove_wall -> <empty>','neupoint_remove_wall',0,'p_neupoint_remove_wall','tokensAndGrammars.py',600),
  ('neupoint_assignment_quad -> <empty>','neupoint_assignment_quad',0,'p_neupoint_assignment_quad','tokensAndGrammars.py',609),
  ('neupoint_assignment_single_quad -> <empty>','neupoint_assignment_single_quad',0,'p_neupoint_assignment_single_quad','tokensAndGrammars.py',619),
]
