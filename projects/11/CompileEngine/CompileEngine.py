'''
Compile Engine
- Uses tokens from token_list (created in JackTokenizer.py)
- Adds "context wrapping" to token in token_list
- Eg "function void main(){" is extended
  so: "<subroutineDec> ... </subroutineDec>" wraps the tokens
- The full token list is outputted to .xml file
'''

from Globals import *
token_num = 0
token_list_len = len(token_list) 
class_name = ""
is_void_type = False

def parser(write_token_file_object, write_vm_file_object):
    global token_num
    global token_list_len
    token_num = 0
    token_list_len = len(token_list) 
    token_full = token_list[token_num]
    compile_class(token_full, write_token_file_object, write_vm_file_object)

############################ ↓ COMPILERS ↓ ############################

def compile_class(token_full, write_token_file_object, write_vm_file_object):
    global class_name
    write_text_to_file("<class>", write_token_file_object)
    
    # Class of File
    add_tokens_upto_delim(token_full, '{', write_token_file_object)
    class_name = get_token_content(token_list[token_num - 2])

    # Class Variables
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    if is_var_dec(token_content):
        while is_var_dec(token_content):
            compile_class_var_dec(token_full, write_token_file_object)
            token_full = get_token_full()
            token_content = get_token_content(token_full)
    
    # Class Functions
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    if is_subroutine_dec(token_content):
        while is_subroutine_dec(token_content):
            write_text_to_file("<subroutineDec>", write_token_file_object)
            compile_subroutine(token_full, write_token_file_object, write_vm_file_object)
            token_full = get_token_full()
            token_content = get_token_content(token_full)
            write_text_to_file("</subroutineDec>", write_token_file_object)

    add_tokens_upto_delim(token_full, '}', write_token_file_object)
    write_text_to_file("</class>", write_token_file_object)

def compile_class_var_dec(token_full, write_token_file_object):
    write_text_to_file("<classVarDec>", write_token_file_object)
    add_tokens_upto_delim(token_full, ';', write_token_file_object)
    write_text_to_file("</classVarDec>", write_token_file_object)

def compile_subroutine(token_full, write_token_file_object, write_vm_file_object):
    global token_num
    global class_name
    global is_void_type
    is_void_type = False
    # Function header
    add_tokens_upto_delim(token_full, '(', write_token_file_object)   # Subroutine definition
    function_name = get_token_content(token_list[token_num - 2])
    token_full = get_token_full()

    # Parameter List
    parameter_count = compile_parameter_list(token_full, write_token_file_object)       # Subroutine parameters
    if parameter_count == 0: is_void_type = True
    token_full = get_token_full()
    
    # Closing
    add_tokens_upto_delim(token_full, ')', write_token_file_object)   # Subroutine definition - end
    token_full = get_token_full()

    # Create Subroutine Header VM Code
    write_text_to_file("function " + class_name + "." + function_name + " " + str(parameter_count), write_vm_file_object) 

    # Compile Subroutine Body 
    compile_subroutine_body(token_full, write_token_file_object, write_vm_file_object)       # Subroutine body

def compile_parameter_list(token_full, write_token_file_object):
    parameter_count = 0
    write_text_to_file("<parameterList>", write_token_file_object)
    token_content = get_token_content(token_full)
    while token_content != ")":
        add_tokens_upto_delim(token_full, token_content, write_token_file_object)
        token_full = get_token_full()
        token_content = get_token_content(token_full)
        parameter_count += 1
    write_text_to_file("</parameterList>", write_token_file_object)
    return parameter_count
    
def compile_subroutine_body(token_full, write_token_file_object, write_vm_file_object):
    write_text_to_file("<subroutineBody>", write_token_file_object)
    add_tokens_upto_delim(token_full, '{', write_token_file_object)
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    
    # Variable Declarations
    while is_var_dec(token_content):
        compile_var_dec(token_full, write_token_file_object)
        token_full = get_token_full()
        token_content = get_token_content(token_full)

    compile_statements(token_full, write_token_file_object, write_vm_file_object)
    token_full = get_token_full()
    add_tokens_upto_delim(token_full, '}', write_token_file_object)
    write_text_to_file("</subroutineBody>", write_token_file_object)

def compile_var_dec(token_full, write_token_file_object):
    write_text_to_file("<varDec>", write_token_file_object) 
    add_tokens_upto_delim(token_full, ';', write_token_file_object)
    write_text_to_file("</varDec>", write_token_file_object)

def compile_statements(token_full, write_token_file_object, write_vm_file_object):
    write_text_to_file("<statements>", write_token_file_object) 
    token_content = get_token_content(token_full)
    while is_statement(token_content):
        if token_content == 'let':
            compile_let(token_full, write_token_file_object)
            token_full = get_token_full()
        elif token_content == 'if': 
                compile_if(token_full, write_token_file_object, write_vm_file_object)    
                token_full = get_token_full()
        elif token_content == 'while':
            compile_while(token_full, write_token_file_object, write_vm_file_object)    
            token_full = get_token_full()
        elif token_content == 'do':
            compile_do(token_full, write_token_file_object, write_vm_file_object)
            token_full = get_token_full()
        elif token_content == 'return':
            compile_return(token_full, write_token_file_object, write_vm_file_object)
            token_full = get_token_full()
        token_content = get_token_content(token_full)
    write_text_to_file("</statements>", write_token_file_object) 

def compile_let(token_full, write_token_file_object):
    write_text_to_file("<letStatement>", write_token_file_object) 
    
    # Add "let"
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    add_tokens_upto_delim(token_full, token_content, write_token_file_object) 
    
    # Add varName
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    add_tokens_upto_delim(token_full, token_content, write_token_file_object) 

    token_full = get_token_full()
    token_content = get_token_content(token_full)
    if token_content == '[':
        add_tokens_upto_delim(token_full, token_content, write_token_file_object) 
        token_full = get_token_full()
        compile_expression(token_full, write_token_file_object)

    token_full = get_token_full()
    add_tokens_upto_delim(token_full, '=', write_token_file_object) 
    token_full = get_token_full()
    compile_expression(token_full, write_token_file_object)
    token_full = get_token_full()
    add_tokens_upto_delim(token_full, ';', write_token_file_object) 
    
    write_text_to_file("</letStatement>", write_token_file_object) 

def compile_if(token_full, write_token_file_object, write_vm_file_object):
    write_text_to_file("<ifStatement>", write_token_file_object) 
    
    add_tokens_upto_delim(token_full, '(', write_token_file_object)
    token_full = get_token_full()
    compile_expression(token_full, write_token_file_object)
    token_full = get_token_full()
    add_tokens_upto_delim(token_full, '{', write_token_file_object)

    token_full = get_token_full()
    compile_statements(token_full, write_token_file_object, write_vm_file_object)
    token_full = get_token_full()
    add_tokens_upto_delim(token_full, '}', write_token_file_object)

    token_full = get_token_full()
    token_content = get_token_content(token_full)
    if (token_content == "else"):
        add_tokens_upto_delim(token_full, '{', write_token_file_object)
        token_full = get_token_full()
        compile_statements(token_full, write_token_file_object, write_vm_file_object)
        token_full = get_token_full()
        add_tokens_upto_delim(token_full, '}', write_token_file_object)
        token_full = get_token_full()

    write_text_to_file("</ifStatement>", write_token_file_object)  

def compile_while(token_full, write_token_file_object, write_vm_file_object):
    write_text_to_file("<whileStatement>", write_token_file_object) 
    add_tokens_upto_delim(token_full, '(', write_token_file_object)
    token_full = get_token_full()
    compile_expression(token_full, write_token_file_object)
    token_full = get_token_full()
    add_tokens_upto_delim(token_full, '{', write_token_file_object)
    token_full = get_token_full()
    compile_statements(token_full, write_token_file_object)
    token_full = get_token_full()
    add_tokens_upto_delim(token_full, '}', write_token_file_object)
    write_text_to_file("</whileStatement>", write_token_file_object) 

def compile_do(token_full, write_token_file_object, write_vm_file_object):
    global token_list
    global token_num
    is_printInt = False
    write_text_to_file("<doStatement>", write_token_file_object) 
    add_tokens_upto_delim(token_full, '(', write_token_file_object)

    if get_token_content(token_list[token_num - 2]) == "printInt": is_printInt = True

    token_full = get_token_full()
    compile_expression_list(token_full, write_token_file_object, write_vm_file_object)

    if is_printInt == True:
         write_text_to_file("call Output.printInt 1", write_vm_file_object)
         write_text_to_file("pop temp 0", write_vm_file_object)

    token_full = get_token_full()
    add_tokens_upto_delim(token_full, ';', write_token_file_object)
    write_text_to_file("</doStatement>", write_token_file_object) 

def compile_return(token_full, write_token_file_object, write_vm_file_object):
    global is_void_type

    if is_void_type == True:
        write_text_to_file("push constant 0", write_vm_file_object)

    write_text_to_file("<returnStatement>", write_token_file_object) 
    token_content = get_token_content(token_full)
    add_tokens_upto_delim(token_full, token_content, write_token_file_object)

    token_full = get_token_full()
    token_content = get_token_content(token_full)
    if token_content == ';':
        add_tokens_upto_delim(token_full, ';', write_token_file_object)
    else:
        compile_expression(token_full, write_token_file_object)   
        token_full = get_token_full()
        add_tokens_upto_delim(token_full, ';', write_token_file_object)
    write_text_to_file("</returnStatement>", write_token_file_object) 

    write_text_to_file("return", write_vm_file_object)

def compile_expression(token_full, write_token_file_object, write_vm_file_object):
    write_text_to_file("<expression>", write_token_file_object) 
    compile_term(token_full, write_token_file_object, write_vm_file_object)
    token_full = get_token_full()

    # Check for op terms
    token_content = get_token_content(token_full)
    while is_op_term(token_content):
        add_tokens_upto_delim(token_full, token_content, write_token_file_object)
        token_full = get_token_full()
        compile_term(token_full, write_token_file_object, write_vm_file_object)

        if token_content == "+": write_text_to_file("add", write_vm_file_object)
        if token_content == "-": write_text_to_file("sub", write_vm_file_object)
        if token_content == "*": write_text_to_file("call Math.multiply 2", write_vm_file_object)
        if token_content == "/": write_text_to_file("call Math.divide 2", write_vm_file_object)        
        
        token_full = get_token_full()
        token_content = get_token_content(token_full)
    
    write_text_to_file("</expression>", write_token_file_object) 

def compile_term(token_full, write_token_file_object, write_vm_file_object):
    unaryOp = ['-', '~']
    token_content = get_token_content(token_full)
    write_text_to_file("<term>", write_token_file_object) 
    
    # Check if variable grouping "()"
    if token_content == '(':
        add_tokens_upto_delim(token_full, token_content, write_token_file_object)
        token_full = get_token_full()
        compile_expression(token_full, write_token_file_object, write_vm_file_object)
        token_full = get_token_full()
        add_tokens_upto_delim(token_full, ')', write_token_file_object)
    
    # Check if unaryOp term
    elif token_content in unaryOp:
        add_tokens_upto_delim(token_full, token_content, write_token_file_object)
        token_full = get_token_full()
        compile_term(token_full, write_token_file_object)

    # Else: Add var name
    else:
        # Add identifier name
        add_tokens_upto_delim(token_full, token_content, write_token_file_object)

        if get_token_type(token_full) == "integerConstant":
            integer_value = get_token_content(token_full)
            write_text_to_file("push constant " + integer_value ,write_vm_file_object)

        # Add Category: field, static, var, arg, class, subroutine

        # Add Index: field, static, var or arg correspond to symbol table

        # Add Usage: declared or used

    token_type = get_token_type(token_full) # Token type of previous token
    token_full = get_token_full()
    token_content = get_token_content(token_full)
    
    # Look at next token for Array or Method
    if token_type == "identifier": # Check type of previous token
        if token_content == '[':
            add_tokens_upto_delim(token_full, '[', write_token_file_object)
            token_full = get_token_full()
            compile_expression(token_full, write_token_file_object)
            token_full = get_token_full()
            add_tokens_upto_delim(token_full, ']', write_token_file_object)
        elif token_content == '.':
            add_tokens_upto_delim(token_full, '(', write_token_file_object)
            token_full = get_token_full()
            compile_expression_list(token_full, write_token_file_object)
            token_full = get_token_full()
            add_tokens_upto_delim(token_full, ')', write_token_file_object)

    write_text_to_file("</term>", write_token_file_object) 

def compile_expression_list(token_full, write_token_file_object, write_vm_file_object):
    write_text_to_file("<expressionList>", write_token_file_object) 
    token_content = get_token_content(token_full)
    while token_content != ')':
        compile_expression(token_full, write_token_file_object, write_vm_file_object)
        token_full = get_token_full()
        token_content = get_token_content(token_full)
        if token_content == ',':
            add_tokens_upto_delim(token_full, token_content, write_token_file_object)
            token_full = get_token_full()
            token_content = get_token_content(token_full)
    write_text_to_file("</expressionList>", write_token_file_object) 

############################    ↓ VM WRITERS ↓    ############################



############################ ↓ HELPER FUNCTIONS ↓ ############################

def add_tokens_upto_delim(token_full, delimiter, write_token_file_object):
    token_content = get_token_content(token_full)
    while (token_content != delimiter) and (token_num < (token_list_len )):
        write_text_to_file(token_full, write_token_file_object)       
        advance_token()
        token_full = get_token_full()
        token_content = get_token_content(token_full)
    write_text_to_file(token_full, write_token_file_object)       
    advance_token()

def advance_token():
    global token_num
    global token_list_len
    if token_num < (token_list_len ): 
        token_num += 1 

def write_text_to_file(line_to_write, write_token_file_object, write_end_line = True):
    write_token_file_object.write(line_to_write)
    if write_end_line == True:
        write_token_file_object.write('\n')

def get_token_full():
    global token_num
    return token_list[token_num]

def get_token_next_full():
    global token_num
    return token_list[token_num + 1]

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

def is_var_dec(token_content):
    if (token_content == 'var') or (token_content == 'field') or (token_content == 'static'):
        return True
    else:
        return False

def is_subroutine_dec(token_content):
    if (token_content == 'constructor') or (token_content == 'function') \
        or (token_content == 'method'):
        return True
    else:
        return False

def is_statement(token_content):
    if (token_content == 'let') or (token_content == 'if') or (token_content == 'while') \
        or (token_content == 'do') or (token_content == 'return'):
        return True
    else:
        return False

def is_op_term(token_content):
    op_list = ['+','-','*','/','&amp;','|','&lt;','&gt;','=']
    if token_content in op_list: return True
    else: return False


'''
############################   ↓ TO DO ↓   ############################

x Fix up all this file naming stuff?

'''
