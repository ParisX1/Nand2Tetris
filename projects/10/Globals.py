keyword =   ["class", "constructor", "function", "method", "field", "static", "var",
            "int", "char", "boolean", "void", "true", "false", "null", "this", 
            "let", "do", "if", "else", "while", "return"]
symbol =    ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', 
            '|', '<', '>', '=', '~']
symbol_replacement = {'<':"&lt;", 
                      '>':"&gt;",
                      '"':"&quot;",
                      '&':"&amp;"
                     }
token_list = []
multiline_comment = False
is_debug_mode = True
