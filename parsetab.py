
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMMA COMPARISON CTECHAR CTEFLOAT CTEINT CTESTRING DECREMENT DIFFERENT DIVIDE DO ELSE EQUALS FLOAT FOR GREATERHANOREQUAL GREATERTHAN ID IF INCREMENT INT LEFTBRACKET LEFTPARENTHESIS LEFTSQRBRACKET LESSTHAN LESSTHANOREQUAL MAIN MINUS MOD MODULE MULTIPLY OR PLUS PLUSEQUALS PROGRAM READ RETURN RIGHTBRACKET RIGHTPARENTHESIS RIGHTSQRBRACKET SEMICOLON SUBSTRACTEQUALS THEN TO VAR VOID WHILE WRITE\n    program : PROGRAM ID SEMICOLON neupoint_goto_main vars functions_list MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end\n            | PROGRAM ID SEMICOLON neupoint_goto_main vars MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end\n            | PROGRAM ID SEMICOLON neupoint_goto_main functions_list MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end\n            | PROGRAM ID SEMICOLON neupoint_goto_main MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end\n    \n    neupoint_goto_main : \n    \n    neupoint_fill_goto_main : \n    \n    neupoint_end : \n    \n    data_type : INT\n              | FLOAT\n              | CHAR\n    \n    vars : VAR vars_lists neupoint_add_vars\n    \n    vars_lists : data_type decla_ids_list SEMICOLON vars_lists\n               | data_type decla_ids_list SEMICOLON\n    \n    decla_ids_list : decla_identifier COMMA decla_ids_list\n                   | decla_identifier\n    \n    decla_identifier : ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET\n                     | ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET\n                     | ID\n    \n    identifier : ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET LEFTSQRBRACKET expresion RIGHTSQRBRACKET\n               | ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET\n               | ID\n    \n    neupoint_add_vars :\n    \n    return_type : data_type\n                | VOID\n    \n    functions_list : function functions_list\n                   | function\n    \n    function : MODULE return_type ID neupoint_add_function parameters_list vars neupoint_start_function block neupoint_check_for_return neupoint_end_function\n             | MODULE return_type ID neupoint_add_function parameters_list neupoint_start_function block neupoint_check_for_return neupoint_end_function\n    \n    parameters_list : LEFTPARENTHESIS parameter RIGHTPARENTHESIS neupoint_add_parameters\n                    | LEFTPARENTHESIS RIGHTPARENTHESIS\n    \n    parameter : data_type decla_identifier COMMA parameter\n              | data_type decla_identifier\n    \n    neupoint_add_function : \n    \n    neupoint_add_parameters :\n    \n    neupoint_start_function : \n    \n    neupoint_check_for_return : \n    \n    neupoint_end_function : \n    \n    comparators : COMPARISON\n                | GREATERHANOREQUAL\n                | LESSTHANOREQUAL\n                | GREATERTHAN\n                | LESSTHAN\n                | DIFFERENT\n    \n    exp_operator : PLUS\n                 | MINUS\n    \n    term_operator : MULTIPLY\n                  | DIVIDE\n                  | MOD\n    \n    block : LEFTBRACKET statutes_list RIGHTBRACKET\n          | LEFTBRACKET RIGHTBRACKET\n    \n    statutes_list : statute statutes_list\n                  | statute\n    \n    statute : assignment\n            | function_return\n            | reading\n            | writing\n            | decision\n            | loop\n            | function_call_void\n    \n    assignment : identifier neupoint_add_operand EQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON\n               | identifier neupoint_add_operand PLUSEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON\n               | identifier neupoint_add_operand SUBSTRACTEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON\n               | identifier neupoint_add_operand INCREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON\n               | identifier neupoint_add_operand DECREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON\n    \n    reading : READ LEFTPARENTHESIS reading_list RIGHTPARENTHESIS SEMICOLON\n    \n    reading_list : identifier neupoint_add_operand  COMMA reading_list\n                 | identifier neupoint_add_operand\n    \n    writing : WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON\n    \n    writing_list : CTESTRING neupoint_add_cte_operand neupoint_write_quad COMMA writing_list\n                 | expresion neupoint_write_quad COMMA writing_list\n                 | CTESTRING neupoint_add_cte_operand neupoint_write_quad\n                 | expresion neupoint_write_quad\n    \n    decision : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad THEN block ELSE neupoint_else_conditional_quad block neupoint_end_conditional_quad\n             | IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad THEN block neupoint_end_conditional_quad\n    \n    loop : conditional\n         | non_conditional\n    \n    conditional : WHILE neupoint_while_start LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad DO block neupoint_while_end\n    \n    non_conditional : FOR ID neupoint_add_operand_integer EQUALS neupoint_add_operator exp neupoint_assignment_quad neupoint_add_operand_for TO exp  neupoint_comparison_quad DO block neupoint_for_end\n    \n    function_return : RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON\n    \n    function_call_void : function_call SEMICOLON\n    \n    function_call : ID neupoint_validate_function LEFTPARENTHESIS neupoint_era_quad neupoint_add_wall ags_list neupoint_validate_num_args RIGHTPARENTHESIS neupoint_gosub_quad\n                  | ID neupoint_validate_function LEFTPARENTHESIS neupoint_era_quad neupoint_add_wall neupoint_validate_num_args RIGHTPARENTHESIS neupoint_gosub_quad\n    \n    ags_list : expresion neupoint_validate_args COMMA ags_list\n             | expresion neupoint_validate_args\n    \n    expresion : exp_relational AND neupoint_add_operator expresion neupoint_logical_relational_opt\n              | exp_relational OR neupoint_add_operator expresion neupoint_logical_relational_opt\n              | exp_relational\n    \n    exp_relational : exp comparators neupoint_add_operator exp neupoint_logical_relational_opt\n                   | exp\n    \n    exp : term neupoint_arithmetic_exp_quad exp_operator neupoint_add_operator exp\n        | term neupoint_arithmetic_exp_quad\n    \n    term : factor neupoint_arithmetic_term_quad term_operator neupoint_add_operator term\n         | factor neupoint_arithmetic_term_quad\n    \n    factor : LEFTPARENTHESIS neupoint_add_wall expresion neupoint_remove_wall RIGHTPARENTHESIS\n           | CTEINT neupoint_add_cte_operand\n           | CTEFLOAT neupoint_add_cte_operand\n           | CTECHAR neupoint_add_cte_operand\n           | function_call\n           | identifier neupoint_add_operand\n    \n    neupoint_add_operator : \n    \n    neupoint_add_operand : \n    \n    neupoint_add_cte_operand : \n    \n    neupoint_arithmetic_exp_quad : \n    \n    neupoint_arithmetic_term_quad : \n    \n    neupoint_add_wall : \n    \n    neupoint_remove_wall : \n    \n    neupoint_assignment_quad : \n    \n    neupoint_assignment_single_quad : \n    \n    neupoint_logical_relational_opt : \n    \n    neupoint_conditional_quad : \n    \n    neupoint_else_conditional_quad : \n    \n    neupoint_end_conditional_quad : \n    \n    neupoint_while_start : \n    \n    neupoint_while_end : \n    \n    neupoint_validate_function : \n    \n    neupoint_era_quad : \n    \n    neupoint_validate_args : \n    \n    neupoint_validate_num_args : \n    \n    neupoint_gosub_quad : \n    \n    neupoint_write_quad : \n    \n    neupoint_add_operand_integer : \n    \n    neupoint_add_operand_for : \n    \n    neupoint_comparison_quad : \n    \n    neupoint_for_end : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,45,53,54,55,57,83,84,85,86,103,],[0,-7,-7,-7,-4,-50,-7,-2,-3,-49,-1,]),'ID':([2,17,18,19,20,22,23,24,39,46,57,58,59,60,61,62,63,64,65,71,72,76,82,86,89,90,91,92,93,94,104,105,106,109,129,130,137,138,139,142,155,156,157,158,159,160,161,162,163,166,168,179,180,181,182,183,184,185,186,187,188,189,191,192,193,194,196,197,199,204,205,207,208,210,222,223,224,232,240,243,244,249,250,251,253,256,257,],[3,32,-8,-9,-10,33,-23,-24,32,74,-50,74,-53,-54,-55,-56,-57,-58,-59,-75,-76,97,32,-49,118,121,118,118,-80,118,-100,-100,-100,-105,-116,118,118,118,118,118,-100,-100,-100,-38,-39,-40,-41,-42,-43,-105,-100,-79,-100,-44,-45,-100,-46,-47,-48,-65,121,-68,118,118,118,118,118,118,118,-63,-64,118,118,118,-60,-61,-62,-112,-74,118,-114,-77,118,-112,-73,-124,-78,]),'SEMICOLON':([3,30,31,32,48,73,77,107,108,111,112,113,114,115,116,117,118,125,126,140,141,143,144,145,146,147,148,149,150,152,165,169,173,174,175,176,177,201,202,203,212,213,214,225,226,227,229,230,231,233,235,241,242,247,],[4,38,-15,-18,-14,93,-17,-100,-100,-103,-104,-102,-102,-102,-98,-101,-21,-87,-89,-108,-108,179,-91,-93,-95,-96,-97,-99,187,189,-20,-16,-107,-107,-107,204,205,222,223,224,-109,-109,-109,-94,-90,-92,-85,-86,-88,-19,-119,-119,-82,-81,]),'MAIN':([4,5,6,7,10,12,16,21,29,38,47,57,86,100,133,134,170,171,200,],[-5,8,13,14,-26,25,-22,-25,-11,-13,-12,-50,-49,-36,-36,-37,-37,-28,-27,]),'VAR':([4,5,50,81,101,135,],[-5,9,9,-30,-34,-29,]),'MODULE':([4,5,6,10,16,29,38,47,57,86,100,133,134,170,171,200,],[-5,11,11,11,-22,-11,-13,-12,-50,-49,-36,-36,-37,-37,-28,-27,]),'LEFTPARENTHESIS':([8,13,14,15,25,26,27,33,34,41,67,68,69,70,74,75,89,91,92,94,95,96,104,105,106,109,118,129,130,137,138,139,142,155,156,157,158,159,160,161,162,163,166,168,180,181,182,183,184,185,186,191,192,193,194,196,197,199,207,208,210,243,250,],[-6,-6,-6,28,-6,35,36,-33,42,51,89,90,91,92,-115,-113,109,109,109,109,129,130,-100,-100,-100,-105,-115,-116,109,109,109,109,109,-100,-100,-100,-38,-39,-40,-41,-42,-43,-105,-100,-100,-44,-45,-100,-46,-47,-48,109,109,109,109,109,109,109,109,109,109,109,109,]),'INT':([9,11,38,51,136,],[18,18,18,18,18,]),'FLOAT':([9,11,38,51,136,],[19,19,19,19,19,]),'CHAR':([9,11,38,51,136,],[20,20,20,20,20,]),'VOID':([11,],[24,]),'LEFTBRACKET':([16,29,37,38,43,44,47,50,52,78,79,81,99,101,135,215,237,239,246,255,],[-22,-11,46,-13,46,46,-12,-35,46,-35,46,-30,46,-34,-29,46,46,-111,46,46,]),'RIGHTPARENTHESIS':([28,32,35,36,42,51,77,80,102,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,144,145,146,147,148,149,151,153,154,165,166,167,169,172,178,190,197,206,209,211,212,213,214,217,218,219,225,226,227,228,229,230,231,233,234,235,236,241,242,247,248,],[37,-18,43,44,52,81,-17,101,-32,143,-103,-104,-102,-102,-102,-98,-101,-21,150,-101,-21,152,-102,-120,-87,-89,164,-116,-91,-93,-95,-96,-97,-99,-67,-120,-72,-20,-105,198,-16,-31,-106,-71,-118,225,-66,-70,-109,-109,-109,-118,235,-117,-94,-90,-92,-69,-85,-86,-88,-19,241,-119,-84,-119,-82,-81,-83,]),'COMMA':([31,32,77,102,111,112,113,114,115,116,117,118,120,121,123,124,125,126,144,145,146,147,148,149,151,153,154,165,169,190,212,213,214,219,225,226,227,229,230,231,233,235,236,241,242,247,],[39,-18,-17,136,-103,-104,-102,-102,-102,-98,-101,-21,-101,-21,-102,-120,-87,-89,-91,-93,-95,-96,-97,-99,188,-120,191,-20,-16,210,-109,-109,-109,-117,-94,-90,-92,-85,-86,-88,-19,-119,243,-119,-82,-81,]),'LEFTSQRBRACKET':([32,74,77,118,121,165,],[40,94,98,94,94,196,]),'CTEINT':([40,89,91,92,94,98,104,105,106,109,129,130,137,138,139,142,155,156,157,158,159,160,161,162,163,166,168,180,181,182,183,184,185,186,191,192,193,194,196,197,199,207,208,210,243,250,],[49,113,113,113,113,132,-100,-100,-100,-105,-116,113,113,113,113,113,-100,-100,-100,-38,-39,-40,-41,-42,-43,-105,-100,-100,-44,-45,-100,-46,-47,-48,113,113,113,113,113,113,113,113,113,113,113,113,]),'RIGHTBRACKET':([46,56,57,58,59,60,61,62,63,64,65,71,72,86,87,93,179,187,189,204,205,222,223,224,232,240,244,249,251,253,256,257,],[57,86,-50,-52,-53,-54,-55,-56,-57,-58,-59,-75,-76,-49,-51,-80,-79,-65,-68,-63,-64,-60,-61,-62,-112,-74,-114,-77,-112,-73,-124,-78,]),'RETURN':([46,57,58,59,60,61,62,63,64,65,71,72,86,93,179,187,189,204,205,222,223,224,232,240,244,249,251,253,256,257,],[67,-50,67,-53,-54,-55,-56,-57,-58,-59,-75,-76,-49,-80,-79,-65,-68,-63,-64,-60,-61,-62,-112,-74,-114,-77,-112,-73,-124,-78,]),'READ':([46,57,58,59,60,61,62,63,64,65,71,72,86,93,179,187,189,204,205,222,223,224,232,240,244,249,251,253,256,257,],[68,-50,68,-53,-54,-55,-56,-57,-58,-59,-75,-76,-49,-80,-79,-65,-68,-63,-64,-60,-61,-62,-112,-74,-114,-77,-112,-73,-124,-78,]),'WRITE':([46,57,58,59,60,61,62,63,64,65,71,72,86,93,179,187,189,204,205,222,223,224,232,240,244,249,251,253,256,257,],[69,-50,69,-53,-54,-55,-56,-57,-58,-59,-75,-76,-49,-80,-79,-65,-68,-63,-64,-60,-61,-62,-112,-74,-114,-77,-112,-73,-124,-78,]),'IF':([46,57,58,59,60,61,62,63,64,65,71,72,86,93,179,187,189,204,205,222,223,224,232,240,244,249,251,253,256,257,],[70,-50,70,-53,-54,-55,-56,-57,-58,-59,-75,-76,-49,-80,-79,-65,-68,-63,-64,-60,-61,-62,-112,-74,-114,-77,-112,-73,-124,-78,]),'WHILE':([46,57,58,59,60,61,62,63,64,65,71,72,86,93,179,187,189,204,205,222,223,224,232,240,244,249,251,253,256,257,],[75,-50,75,-53,-54,-55,-56,-57,-58,-59,-75,-76,-49,-80,-79,-65,-68,-63,-64,-60,-61,-62,-112,-74,-114,-77,-112,-73,-124,-78,]),'FOR':([46,57,58,59,60,61,62,63,64,65,71,72,86,93,179,187,189,204,205,222,223,224,232,240,244,249,251,253,256,257,],[76,-50,76,-53,-54,-55,-56,-57,-58,-59,-75,-76,-49,-80,-79,-65,-68,-63,-64,-60,-61,-62,-112,-74,-114,-77,-112,-73,-124,-78,]),'RIGHTSQRBRACKET':([49,111,112,113,114,115,116,117,118,125,126,128,132,144,145,146,147,148,149,165,212,213,214,216,225,226,227,229,230,231,233,235,241,242,247,],[77,-103,-104,-102,-102,-102,-98,-101,-21,-87,-89,165,169,-91,-93,-95,-96,-97,-99,-20,-109,-109,-109,233,-94,-90,-92,-85,-86,-88,-19,-119,-119,-82,-81,]),'ELSE':([57,86,232,],[-50,-49,239,]),'EQUALS':([66,74,88,97,131,165,233,],[-101,-21,104,-121,168,-20,-19,]),'PLUSEQUALS':([66,74,88,165,233,],[-101,-21,105,-20,-19,]),'SUBSTRACTEQUALS':([66,74,88,165,233,],[-101,-21,106,-20,-19,]),'INCREMENT':([66,74,88,165,233,],[-101,-21,107,-20,-19,]),'DECREMENT':([66,74,88,165,233,],[-101,-21,108,-20,-19,]),'CTEFLOAT':([89,91,92,94,104,105,106,109,129,130,137,138,139,142,155,156,157,158,159,160,161,162,163,166,168,180,181,182,183,184,185,186,191,192,193,194,196,197,199,207,208,210,243,250,],[114,114,114,114,-100,-100,-100,-105,-116,114,114,114,114,114,-100,-100,-100,-38,-39,-40,-41,-42,-43,-105,-100,-100,-44,-45,-100,-46,-47,-48,114,114,114,114,114,114,114,114,114,114,114,114,]),'CTECHAR':([89,91,92,94,104,105,106,109,129,130,137,138,139,142,155,156,157,158,159,160,161,162,163,166,168,180,181,182,183,184,185,186,191,192,193,194,196,197,199,207,208,210,243,250,],[115,115,115,115,-100,-100,-100,-105,-116,115,115,115,115,115,-100,-100,-100,-38,-39,-40,-41,-42,-43,-105,-100,-100,-44,-45,-100,-46,-47,-48,115,115,115,115,115,115,115,115,115,115,115,115,]),'CTESTRING':([91,191,210,],[123,123,123,]),'PLUS':([111,112,113,114,115,116,117,118,144,145,146,147,148,149,165,225,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,181,-93,-95,-96,-97,-99,-20,-94,-92,-19,-119,-119,-82,-81,]),'MINUS':([111,112,113,114,115,116,117,118,144,145,146,147,148,149,165,225,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,182,-93,-95,-96,-97,-99,-20,-94,-92,-19,-119,-119,-82,-81,]),'COMPARISON':([111,112,113,114,115,116,117,118,126,144,145,146,147,148,149,165,225,226,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,158,-91,-93,-95,-96,-97,-99,-20,-94,-90,-92,-19,-119,-119,-82,-81,]),'GREATERHANOREQUAL':([111,112,113,114,115,116,117,118,126,144,145,146,147,148,149,165,225,226,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,159,-91,-93,-95,-96,-97,-99,-20,-94,-90,-92,-19,-119,-119,-82,-81,]),'LESSTHANOREQUAL':([111,112,113,114,115,116,117,118,126,144,145,146,147,148,149,165,225,226,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,160,-91,-93,-95,-96,-97,-99,-20,-94,-90,-92,-19,-119,-119,-82,-81,]),'GREATERTHAN':([111,112,113,114,115,116,117,118,126,144,145,146,147,148,149,165,225,226,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,161,-91,-93,-95,-96,-97,-99,-20,-94,-90,-92,-19,-119,-119,-82,-81,]),'LESSTHAN':([111,112,113,114,115,116,117,118,126,144,145,146,147,148,149,165,225,226,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,162,-91,-93,-95,-96,-97,-99,-20,-94,-90,-92,-19,-119,-119,-82,-81,]),'DIFFERENT':([111,112,113,114,115,116,117,118,126,144,145,146,147,148,149,165,225,226,227,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,163,-91,-93,-95,-96,-97,-99,-20,-94,-90,-92,-19,-119,-119,-82,-81,]),'AND':([111,112,113,114,115,116,117,118,125,126,144,145,146,147,148,149,165,214,225,226,227,231,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,155,-89,-91,-93,-95,-96,-97,-99,-20,-109,-94,-90,-92,-88,-19,-119,-119,-82,-81,]),'OR':([111,112,113,114,115,116,117,118,125,126,144,145,146,147,148,149,165,214,225,226,227,231,233,235,241,242,247,],[-103,-104,-102,-102,-102,-98,-101,-21,156,-89,-91,-93,-95,-96,-97,-99,-20,-109,-94,-90,-92,-88,-19,-119,-119,-82,-81,]),'TO':([111,112,113,114,115,116,117,118,144,145,146,147,148,149,165,221,225,226,227,233,235,238,241,242,245,247,],[-103,-104,-102,-102,-102,-98,-101,-21,-91,-93,-95,-96,-97,-99,-20,-107,-94,-90,-92,-19,-119,-122,-119,-82,250,-81,]),'DO':([111,112,113,114,115,116,117,118,144,145,146,147,148,149,165,198,220,225,226,227,233,235,241,242,247,252,254,],[-103,-104,-102,-102,-102,-98,-101,-21,-91,-93,-95,-96,-97,-99,-20,-110,237,-94,-90,-92,-19,-119,-119,-82,-81,-123,255,]),'MULTIPLY':([112,113,114,115,116,117,118,145,146,147,148,149,165,225,233,235,241,242,247,],[-104,-102,-102,-102,-98,-101,-21,184,-95,-96,-97,-99,-20,-94,-19,-119,-119,-82,-81,]),'DIVIDE':([112,113,114,115,116,117,118,145,146,147,148,149,165,225,233,235,241,242,247,],[-104,-102,-102,-102,-98,-101,-21,185,-95,-96,-97,-99,-20,-94,-19,-119,-119,-82,-81,]),'MOD':([112,113,114,115,116,117,118,145,146,147,148,149,165,225,233,235,241,242,247,],[-104,-102,-102,-102,-98,-101,-21,186,-95,-96,-97,-99,-20,-94,-19,-119,-119,-82,-81,]),'THEN':([164,195,],[-110,215,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'neupoint_goto_main':([4,],[5,]),'vars':([5,50,],[6,78,]),'functions_list':([5,6,10,],[7,12,21,]),'function':([5,6,10,],[10,10,10,]),'neupoint_fill_goto_main':([8,13,14,25,],[15,26,27,34,]),'vars_lists':([9,38,],[16,47,]),'data_type':([9,11,38,51,136,],[17,23,17,82,82,]),'return_type':([11,],[22,]),'neupoint_add_vars':([16,],[29,]),'decla_ids_list':([17,39,],[30,48,]),'decla_identifier':([17,39,82,],[31,31,102,]),'neupoint_add_function':([33,],[41,]),'block':([37,43,44,52,79,99,215,237,246,255,],[45,53,54,83,100,133,232,244,251,256,]),'parameters_list':([41,],[50,]),'neupoint_end':([45,53,54,83,],[55,84,85,103,]),'statutes_list':([46,58,],[56,87,]),'statute':([46,58,],[58,58,]),'assignment':([46,58,],[59,59,]),'function_return':([46,58,],[60,60,]),'reading':([46,58,],[61,61,]),'writing':([46,58,],[62,62,]),'decision':([46,58,],[63,63,]),'loop':([46,58,],[64,64,]),'function_call_void':([46,58,],[65,65,]),'identifier':([46,58,89,90,91,92,94,130,137,138,139,142,188,191,192,193,194,196,197,199,207,208,210,243,250,],[66,66,117,120,117,117,117,117,117,117,117,117,120,117,117,117,117,117,117,117,117,117,117,117,117,]),'conditional':([46,58,],[71,71,]),'non_conditional':([46,58,],[72,72,]),'function_call':([46,58,89,91,92,94,130,137,138,139,142,191,192,193,194,196,197,199,207,208,210,243,250,],[73,73,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'neupoint_start_function':([50,78,],[79,99,]),'parameter':([51,136,],[80,172,]),'neupoint_add_operand':([66,117,120,],[88,149,151,]),'neupoint_validate_function':([74,118,],[95,95,]),'neupoint_while_start':([75,],[96,]),'exp':([89,91,92,94,130,137,138,139,142,191,192,193,194,196,197,199,207,210,243,250,],[110,126,126,126,126,126,126,126,126,126,126,126,214,126,126,221,226,126,126,252,]),'term':([89,91,92,94,130,137,138,139,142,191,192,193,194,196,197,199,207,208,210,243,250,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,227,111,111,111,]),'factor':([89,91,92,94,130,137,138,139,142,191,192,193,194,196,197,199,207,208,210,243,250,],[112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'reading_list':([90,188,],[119,209,]),'writing_list':([91,191,210,],[122,211,228,]),'expresion':([91,92,94,130,137,138,139,142,191,192,193,196,197,210,243,],[124,127,128,167,173,174,175,178,124,212,213,216,219,124,219,]),'exp_relational':([91,92,94,130,137,138,139,142,191,192,193,196,197,210,243,],[125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,]),'neupoint_add_operand_integer':([97,],[131,]),'neupoint_check_for_return':([100,133,],[134,170,]),'neupoint_add_parameters':([101,],[135,]),'neupoint_add_operator':([104,105,106,107,108,155,156,157,168,180,183,],[137,138,139,140,141,192,193,194,199,207,208,]),'neupoint_add_wall':([109,166,],[142,197,]),'neupoint_arithmetic_exp_quad':([111,],[144,]),'neupoint_arithmetic_term_quad':([112,],[145,]),'neupoint_add_cte_operand':([113,114,115,123,],[146,147,148,153,]),'neupoint_write_quad':([124,153,],[154,190,]),'comparators':([126,],[157,]),'neupoint_era_quad':([129,],[166,]),'neupoint_end_function':([134,170,],[171,200,]),'neupoint_assignment_single_quad':([140,141,],[176,177,]),'exp_operator':([144,],[180,]),'term_operator':([145,],[183,]),'neupoint_conditional_quad':([164,198,],[195,220,]),'neupoint_assignment_quad':([173,174,175,221,],[201,202,203,238,]),'neupoint_remove_wall':([178,],[206,]),'ags_list':([197,243,],[217,248,]),'neupoint_validate_num_args':([197,217,],[218,234,]),'neupoint_logical_relational_opt':([212,213,214,],[229,230,231,]),'neupoint_validate_args':([219,],[236,]),'neupoint_end_conditional_quad':([232,251,],[240,253,]),'neupoint_gosub_quad':([235,241,],[242,247,]),'neupoint_add_operand_for':([238,],[245,]),'neupoint_else_conditional_quad':([239,],[246,]),'neupoint_while_end':([244,],[249,]),'neupoint_comparison_quad':([252,],[254,]),'neupoint_for_end':([256,],[257,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON neupoint_goto_main vars functions_list MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end','program',12,'p_program','tokensAndGrammars.py',172),
  ('program -> PROGRAM ID SEMICOLON neupoint_goto_main vars MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end','program',11,'p_program','tokensAndGrammars.py',173),
  ('program -> PROGRAM ID SEMICOLON neupoint_goto_main functions_list MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end','program',11,'p_program','tokensAndGrammars.py',174),
  ('program -> PROGRAM ID SEMICOLON neupoint_goto_main MAIN neupoint_fill_goto_main LEFTPARENTHESIS RIGHTPARENTHESIS block neupoint_end','program',10,'p_program','tokensAndGrammars.py',175),
  ('neupoint_goto_main -> <empty>','neupoint_goto_main',0,'p_neupoint_goto_main','tokensAndGrammars.py',190),
  ('neupoint_fill_goto_main -> <empty>','neupoint_fill_goto_main',0,'p_neupoint_fill_goto_main','tokensAndGrammars.py',197),
  ('neupoint_end -> <empty>','neupoint_end',0,'p_neupoint_end','tokensAndGrammars.py',205),
  ('data_type -> INT','data_type',1,'p_data_type','tokensAndGrammars.py',214),
  ('data_type -> FLOAT','data_type',1,'p_data_type','tokensAndGrammars.py',215),
  ('data_type -> CHAR','data_type',1,'p_data_type','tokensAndGrammars.py',216),
  ('vars -> VAR vars_lists neupoint_add_vars','vars',3,'p_vars','tokensAndGrammars.py',223),
  ('vars_lists -> data_type decla_ids_list SEMICOLON vars_lists','vars_lists',4,'p_vars_lists','tokensAndGrammars.py',230),
  ('vars_lists -> data_type decla_ids_list SEMICOLON','vars_lists',3,'p_vars_lists','tokensAndGrammars.py',231),
  ('decla_ids_list -> decla_identifier COMMA decla_ids_list','decla_ids_list',3,'p_decla_ids_list','tokensAndGrammars.py',245),
  ('decla_ids_list -> decla_identifier','decla_ids_list',1,'p_decla_ids_list','tokensAndGrammars.py',246),
  ('decla_identifier -> ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET','decla_identifier',7,'p_decla_identifier','tokensAndGrammars.py',257),
  ('decla_identifier -> ID LEFTSQRBRACKET CTEINT RIGHTSQRBRACKET','decla_identifier',4,'p_decla_identifier','tokensAndGrammars.py',258),
  ('decla_identifier -> ID','decla_identifier',1,'p_decla_identifier','tokensAndGrammars.py',259),
  ('identifier -> ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET LEFTSQRBRACKET expresion RIGHTSQRBRACKET','identifier',7,'p_identifier','tokensAndGrammars.py',272),
  ('identifier -> ID LEFTSQRBRACKET expresion RIGHTSQRBRACKET','identifier',4,'p_identifier','tokensAndGrammars.py',273),
  ('identifier -> ID','identifier',1,'p_identifier','tokensAndGrammars.py',274),
  ('neupoint_add_vars -> <empty>','neupoint_add_vars',0,'p_neupoint_add_vars','tokensAndGrammars.py',282),
  ('return_type -> data_type','return_type',1,'p_return_type','tokensAndGrammars.py',290),
  ('return_type -> VOID','return_type',1,'p_return_type','tokensAndGrammars.py',291),
  ('functions_list -> function functions_list','functions_list',2,'p_functions_list','tokensAndGrammars.py',298),
  ('functions_list -> function','functions_list',1,'p_functions_list','tokensAndGrammars.py',299),
  ('function -> MODULE return_type ID neupoint_add_function parameters_list vars neupoint_start_function block neupoint_check_for_return neupoint_end_function','function',10,'p_function','tokensAndGrammars.py',306),
  ('function -> MODULE return_type ID neupoint_add_function parameters_list neupoint_start_function block neupoint_check_for_return neupoint_end_function','function',9,'p_function','tokensAndGrammars.py',307),
  ('parameters_list -> LEFTPARENTHESIS parameter RIGHTPARENTHESIS neupoint_add_parameters','parameters_list',4,'p_parameters_list','tokensAndGrammars.py',314),
  ('parameters_list -> LEFTPARENTHESIS RIGHTPARENTHESIS','parameters_list',2,'p_parameters_list','tokensAndGrammars.py',315),
  ('parameter -> data_type decla_identifier COMMA parameter','parameter',4,'p_parameter','tokensAndGrammars.py',322),
  ('parameter -> data_type decla_identifier','parameter',2,'p_parameter','tokensAndGrammars.py',323),
  ('neupoint_add_function -> <empty>','neupoint_add_function',0,'p_neupoint_add_function','tokensAndGrammars.py',348),
  ('neupoint_add_parameters -> <empty>','neupoint_add_parameters',0,'p_neupoint_add_parameters','tokensAndGrammars.py',357),
  ('neupoint_start_function -> <empty>','neupoint_start_function',0,'p_neupoint_start_function','tokensAndGrammars.py',364),
  ('neupoint_check_for_return -> <empty>','neupoint_check_for_return',0,'p_neupoint_check_for_return','tokensAndGrammars.py',373),
  ('neupoint_end_function -> <empty>','neupoint_end_function',0,'p_neupoint_end_function','tokensAndGrammars.py',395),
  ('comparators -> COMPARISON','comparators',1,'p_comparators','tokensAndGrammars.py',408),
  ('comparators -> GREATERHANOREQUAL','comparators',1,'p_comparators','tokensAndGrammars.py',409),
  ('comparators -> LESSTHANOREQUAL','comparators',1,'p_comparators','tokensAndGrammars.py',410),
  ('comparators -> GREATERTHAN','comparators',1,'p_comparators','tokensAndGrammars.py',411),
  ('comparators -> LESSTHAN','comparators',1,'p_comparators','tokensAndGrammars.py',412),
  ('comparators -> DIFFERENT','comparators',1,'p_comparators','tokensAndGrammars.py',413),
  ('exp_operator -> PLUS','exp_operator',1,'p_exp_operator','tokensAndGrammars.py',420),
  ('exp_operator -> MINUS','exp_operator',1,'p_exp_operator','tokensAndGrammars.py',421),
  ('term_operator -> MULTIPLY','term_operator',1,'p_term_operator','tokensAndGrammars.py',428),
  ('term_operator -> DIVIDE','term_operator',1,'p_term_operator','tokensAndGrammars.py',429),
  ('term_operator -> MOD','term_operator',1,'p_term_operator','tokensAndGrammars.py',430),
  ('block -> LEFTBRACKET statutes_list RIGHTBRACKET','block',3,'p_block','tokensAndGrammars.py',438),
  ('block -> LEFTBRACKET RIGHTBRACKET','block',2,'p_block','tokensAndGrammars.py',439),
  ('statutes_list -> statute statutes_list','statutes_list',2,'p_statutes_list','tokensAndGrammars.py',446),
  ('statutes_list -> statute','statutes_list',1,'p_statutes_list','tokensAndGrammars.py',447),
  ('statute -> assignment','statute',1,'p_statute','tokensAndGrammars.py',454),
  ('statute -> function_return','statute',1,'p_statute','tokensAndGrammars.py',455),
  ('statute -> reading','statute',1,'p_statute','tokensAndGrammars.py',456),
  ('statute -> writing','statute',1,'p_statute','tokensAndGrammars.py',457),
  ('statute -> decision','statute',1,'p_statute','tokensAndGrammars.py',458),
  ('statute -> loop','statute',1,'p_statute','tokensAndGrammars.py',459),
  ('statute -> function_call_void','statute',1,'p_statute','tokensAndGrammars.py',460),
  ('assignment -> identifier neupoint_add_operand EQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON','assignment',7,'p_assignment','tokensAndGrammars.py',467),
  ('assignment -> identifier neupoint_add_operand PLUSEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON','assignment',7,'p_assignment','tokensAndGrammars.py',468),
  ('assignment -> identifier neupoint_add_operand SUBSTRACTEQUALS neupoint_add_operator expresion neupoint_assignment_quad SEMICOLON','assignment',7,'p_assignment','tokensAndGrammars.py',469),
  ('assignment -> identifier neupoint_add_operand INCREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON','assignment',6,'p_assignment','tokensAndGrammars.py',470),
  ('assignment -> identifier neupoint_add_operand DECREMENT neupoint_add_operator neupoint_assignment_single_quad SEMICOLON','assignment',6,'p_assignment','tokensAndGrammars.py',471),
  ('reading -> READ LEFTPARENTHESIS reading_list RIGHTPARENTHESIS SEMICOLON','reading',5,'p_reading','tokensAndGrammars.py',478),
  ('reading_list -> identifier neupoint_add_operand COMMA reading_list','reading_list',4,'p_reading_list','tokensAndGrammars.py',485),
  ('reading_list -> identifier neupoint_add_operand','reading_list',2,'p_reading_list','tokensAndGrammars.py',486),
  ('writing -> WRITE LEFTPARENTHESIS writing_list RIGHTPARENTHESIS SEMICOLON','writing',5,'p_writing','tokensAndGrammars.py',494),
  ('writing_list -> CTESTRING neupoint_add_cte_operand neupoint_write_quad COMMA writing_list','writing_list',5,'p_writing_list','tokensAndGrammars.py',501),
  ('writing_list -> expresion neupoint_write_quad COMMA writing_list','writing_list',4,'p_writing_list','tokensAndGrammars.py',502),
  ('writing_list -> CTESTRING neupoint_add_cte_operand neupoint_write_quad','writing_list',3,'p_writing_list','tokensAndGrammars.py',503),
  ('writing_list -> expresion neupoint_write_quad','writing_list',2,'p_writing_list','tokensAndGrammars.py',504),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad THEN block ELSE neupoint_else_conditional_quad block neupoint_end_conditional_quad','decision',11,'p_decision','tokensAndGrammars.py',511),
  ('decision -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad THEN block neupoint_end_conditional_quad','decision',8,'p_decision','tokensAndGrammars.py',512),
  ('loop -> conditional','loop',1,'p_loop','tokensAndGrammars.py',519),
  ('loop -> non_conditional','loop',1,'p_loop','tokensAndGrammars.py',520),
  ('conditional -> WHILE neupoint_while_start LEFTPARENTHESIS expresion RIGHTPARENTHESIS neupoint_conditional_quad DO block neupoint_while_end','conditional',9,'p_conditional','tokensAndGrammars.py',527),
  ('non_conditional -> FOR ID neupoint_add_operand_integer EQUALS neupoint_add_operator exp neupoint_assignment_quad neupoint_add_operand_for TO exp neupoint_comparison_quad DO block neupoint_for_end','non_conditional',14,'p_non_conditional','tokensAndGrammars.py',534),
  ('function_return -> RETURN LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON','function_return',5,'p_function_return','tokensAndGrammars.py',541),
  ('function_call_void -> function_call SEMICOLON','function_call_void',2,'p_function_call_void','tokensAndGrammars.py',556),
  ('function_call -> ID neupoint_validate_function LEFTPARENTHESIS neupoint_era_quad neupoint_add_wall ags_list neupoint_validate_num_args RIGHTPARENTHESIS neupoint_gosub_quad','function_call',9,'p_function_call','tokensAndGrammars.py',563),
  ('function_call -> ID neupoint_validate_function LEFTPARENTHESIS neupoint_era_quad neupoint_add_wall neupoint_validate_num_args RIGHTPARENTHESIS neupoint_gosub_quad','function_call',8,'p_function_call','tokensAndGrammars.py',564),
  ('ags_list -> expresion neupoint_validate_args COMMA ags_list','ags_list',4,'p_ags_list','tokensAndGrammars.py',571),
  ('ags_list -> expresion neupoint_validate_args','ags_list',2,'p_ags_list','tokensAndGrammars.py',572),
  ('expresion -> exp_relational AND neupoint_add_operator expresion neupoint_logical_relational_opt','expresion',5,'p_expresion','tokensAndGrammars.py',579),
  ('expresion -> exp_relational OR neupoint_add_operator expresion neupoint_logical_relational_opt','expresion',5,'p_expresion','tokensAndGrammars.py',580),
  ('expresion -> exp_relational','expresion',1,'p_expresion','tokensAndGrammars.py',581),
  ('exp_relational -> exp comparators neupoint_add_operator exp neupoint_logical_relational_opt','exp_relational',5,'p_exp_relational','tokensAndGrammars.py',588),
  ('exp_relational -> exp','exp_relational',1,'p_exp_relational','tokensAndGrammars.py',589),
  ('exp -> term neupoint_arithmetic_exp_quad exp_operator neupoint_add_operator exp','exp',5,'p_exp','tokensAndGrammars.py',596),
  ('exp -> term neupoint_arithmetic_exp_quad','exp',2,'p_exp','tokensAndGrammars.py',597),
  ('term -> factor neupoint_arithmetic_term_quad term_operator neupoint_add_operator term','term',5,'p_term','tokensAndGrammars.py',604),
  ('term -> factor neupoint_arithmetic_term_quad','term',2,'p_term','tokensAndGrammars.py',605),
  ('factor -> LEFTPARENTHESIS neupoint_add_wall expresion neupoint_remove_wall RIGHTPARENTHESIS','factor',5,'p_factor','tokensAndGrammars.py',612),
  ('factor -> CTEINT neupoint_add_cte_operand','factor',2,'p_factor','tokensAndGrammars.py',613),
  ('factor -> CTEFLOAT neupoint_add_cte_operand','factor',2,'p_factor','tokensAndGrammars.py',614),
  ('factor -> CTECHAR neupoint_add_cte_operand','factor',2,'p_factor','tokensAndGrammars.py',615),
  ('factor -> function_call','factor',1,'p_factor','tokensAndGrammars.py',616),
  ('factor -> identifier neupoint_add_operand','factor',2,'p_factor','tokensAndGrammars.py',617),
  ('neupoint_add_operator -> <empty>','neupoint_add_operator',0,'p_neupoint_add_operator','tokensAndGrammars.py',624),
  ('neupoint_add_operand -> <empty>','neupoint_add_operand',0,'p_neupoint_add_operand','tokensAndGrammars.py',631),
  ('neupoint_add_cte_operand -> <empty>','neupoint_add_cte_operand',0,'p_neupoint_add_cte_operand','tokensAndGrammars.py',644),
  ('neupoint_arithmetic_exp_quad -> <empty>','neupoint_arithmetic_exp_quad',0,'p_neupoint_arithmetic_exp_quad','tokensAndGrammars.py',658),
  ('neupoint_arithmetic_term_quad -> <empty>','neupoint_arithmetic_term_quad',0,'p_neupoint_arithmetic_term_quad','tokensAndGrammars.py',667),
  ('neupoint_add_wall -> <empty>','neupoint_add_wall',0,'p_neupoint_add_wall','tokensAndGrammars.py',676),
  ('neupoint_remove_wall -> <empty>','neupoint_remove_wall',0,'p_neupoint_remove_wall','tokensAndGrammars.py',683),
  ('neupoint_assignment_quad -> <empty>','neupoint_assignment_quad',0,'p_neupoint_assignment_quad','tokensAndGrammars.py',692),
  ('neupoint_assignment_single_quad -> <empty>','neupoint_assignment_single_quad',0,'p_neupoint_assignment_single_quad','tokensAndGrammars.py',699),
  ('neupoint_logical_relational_opt -> <empty>','neupoint_logical_relational_opt',0,'p_neupoint_logical_relational_opt','tokensAndGrammars.py',706),
  ('neupoint_conditional_quad -> <empty>','neupoint_conditional_quad',0,'p_neupoint_conditional_quad','tokensAndGrammars.py',713),
  ('neupoint_else_conditional_quad -> <empty>','neupoint_else_conditional_quad',0,'p_neupoint_else_conditional_quad','tokensAndGrammars.py',720),
  ('neupoint_end_conditional_quad -> <empty>','neupoint_end_conditional_quad',0,'p_neupoint_end_conditional_quad','tokensAndGrammars.py',727),
  ('neupoint_while_start -> <empty>','neupoint_while_start',0,'p_neupoint_while_start','tokensAndGrammars.py',734),
  ('neupoint_while_end -> <empty>','neupoint_while_end',0,'p_neupoint_while_end','tokensAndGrammars.py',742),
  ('neupoint_validate_function -> <empty>','neupoint_validate_function',0,'p_neupoint_validate_function','tokensAndGrammars.py',750),
  ('neupoint_era_quad -> <empty>','neupoint_era_quad',0,'p_neupoint_era_quad','tokensAndGrammars.py',761),
  ('neupoint_validate_args -> <empty>','neupoint_validate_args',0,'p_neupoint_validate_args','tokensAndGrammars.py',777),
  ('neupoint_validate_num_args -> <empty>','neupoint_validate_num_args',0,'p_neupoint_validate_num_args','tokensAndGrammars.py',799),
  ('neupoint_gosub_quad -> <empty>','neupoint_gosub_quad',0,'p_neupoint_gosub_quad','tokensAndGrammars.py',815),
  ('neupoint_write_quad -> <empty>','neupoint_write_quad',0,'p_neupoint_write_quad','tokensAndGrammars.py',829),
  ('neupoint_add_operand_integer -> <empty>','neupoint_add_operand_integer',0,'p_neupoint_add_operand_integer','tokensAndGrammars.py',836),
  ('neupoint_add_operand_for -> <empty>','neupoint_add_operand_for',0,'p_neupoint_add_operand_for','tokensAndGrammars.py',854),
  ('neupoint_comparison_quad -> <empty>','neupoint_comparison_quad',0,'p_neupoint_comparison_quad','tokensAndGrammars.py',862),
  ('neupoint_for_end -> <empty>','neupoint_for_end',0,'p_neupoint_for_end','tokensAndGrammars.py',870),
]
