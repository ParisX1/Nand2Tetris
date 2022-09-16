from Globals import *
token_num = 0
token_list_len = len(token_list) -1 # Ignore last token ("</tokens")

def parser(write_file_object):
    global token_num
    global token_list_len
    token_list_len = len(token_list) -1 #Ignore last token ("</tokens")
    token_full = token_list[token_num]
    while token_num < token_list_len:
        token_full = get_token_full()
        if is_debug_mode: print("Token: " + token_full)
        token_type = get_token_type(token_full)
        if token_type == "keyword": parse_keyword(token_full, write_file_object)
        advance_token()

def advance_token():
    global token_num
    global token_list_len
    if token_num < token_list_len: 
        token_num += 1 

def parse_keyword(token_full, write_file_object):
    token_content = get_token_content(token_full)
    if token_content == 'class': compile_class(token_full, write_file_object)

def write_text_to_file(line_to_write, write_file_object):
    write_file_object.write(line_to_write + '\n')

def get_token_full():
    global token_num
    return token_list[token_num]

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

    # Class of File
    add_tokens_upto_delim(token_full, '{', write_file_object)
    
    # Class Variables
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    if is_var_dec(token_content):
        write_text_to_file("<classVarDec>", write_file_object)
        while is_var_dec(token_content):
            compile_class_var_dec(token_full, write_file_object)
            token_full = get_token_full()
            token_content = get_token_content(token_full)
        write_text_to_file("</classVarDec>", write_file_object)
    
    # Class Functions
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    if is_subroutine_dec(token_content):
        write_text_to_file("<subroutineDec>", write_file_object)
        while is_subroutine_dec(token_content):
            compile_class_var_dec(token_full, write_file_object)
            token_full = get_token_full()
            token_content = get_token_content(token_full)
        write_text_to_file("</subroutineDec>", write_file_object)

def add_tokens_upto_delim(token_full, delimiter, write_file_object):
    token_content = get_token_content(token_full)
    while token_content != delimiter:
        write_text_to_file(token_full, write_file_object)       
        advance_token()
        token_full = get_token_full()
        token_content = get_token_content(token_full)
    write_text_to_file(token_full, write_file_object)       
    advance_token()

def is_var_dec(token_content):
    if (token_content == 'field') or (token_content == 'static'):
        return True
    else:
        return False

def is_subroutine_dec(token_content):
    if (token_content == 'constructor') or (token_content == 'function') \
        or (token_content == 'method'):
        return True
    else:
        return False

def compile_class_var_dec(token_full, write_file_object):
    add_tokens_upto_delim(token_full, ';', write_file_object)

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
    # if token_contents == "if":
    #     compileIf()    

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