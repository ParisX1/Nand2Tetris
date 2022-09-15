from Globals import *
token_num = 0
token_list_len = len(token_list) -1 # Ignore last token ("</tokens")

def parser(write_file_object):
    global token_num
    global token_list_len
    token_list_len = len(token_list) -1 #Ignore last token ("</tokens")
    token_full = token_list[token_num]
    while token_num < token_list_len:
        if is_debug_mode: print("Token: " + token_full)
        
        token_type = get_token_type(token_full)
        if token_type == "keyword": parse_keyword(token_full, write_file_object)
        
        token_full, token_type, token_content = advance_token()

def advance_token():
    global token_num
    global token_list_len
    if token_num < token_list_len: 
        token_num += 1 
    token_full = token_list[token_num]
    token_type = get_token_type(token_full)
    token_content = get_token_content(token_full)
    return token_full, token_type, token_content

def parse_keyword(token_full, write_file_object):
    token_content = get_token_content(token_full)
    if token_content == 'class': compile_class(token_full, write_file_object)

def write_text_to_file(line_to_write, write_file_object):
    write_file_object.write(line_to_write + '\n')

def get_token_type(token):
    end_index = token.index(">")
    return token[1:end_index]

def get_token_content(token):
    if (">" in token) and ("</" in token):
        begin_index = token.index(">")+1
        end_index = token.index("</") 
        return token[begin_index:end_index]
    else:
        return ""

#########################################################################

# Class declarations

def compile_class(token_full, write_file_object):
    write_text_to_file(token_full, write_file_object)       # Write <class>
    token_full, token_type, token_content = advance_token() # Move forward
    write_text_to_file(token_full, write_file_object)       # Write class name
    token_full, token_type, token_content = advance_token() # Move forward
    write_text_to_file(token_full, write_file_object)       # Write '{'
    token_full, token_type, token_content = advance_token() # Move forward

    # Check for variable decs
    if (token_content == 'field') or (token_content == 'field'):
        # process var dec
        compile_class_var_dec(write_file_object)
        pass

    elif token_type == 'function':
        # process method call
        pass

def compile_class_var_dec(write_file_object):
    write_text_to_file("<classVarDec>", write_file_object)

    # ...

    write_text_to_file("</classVarDec>", write_file_object)

# Functions and Methods

def compile_subroutine():
    pass

def compile_parameter_list():
    pass

def compile_subroutine_body():
    pass

# Declare Variables

def compile_var_dec():
    pass

# Statement Types

def compile_statements():
    pass
    # while there are more statements:
    # recurse into the next 'expression?'

    if token_contents == "if":
        compileIf()    

    # 'eat?' the end things so you come back into the loop and will go again if there's another statement

def compile_let():
    pass

def compile_if():
    pass

def compile_while():
    pass

def compile_do():
    pass

def compile_return():
    pass

# Helper Functions

def compile_expression():
    pass

def compile_term():
    pass

def compile_expression_list():
    pass