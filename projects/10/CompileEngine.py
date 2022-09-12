from Globals import *

def parser(token, write_file_object):
    token_type = get_token_type(token)
    token_contents = get_token_contents(token)
    print(token_type)
    print(token_contents)

def write_to_file(line_to_write, write_file_object):
    write_file_object.write(line_to_write + '\n')

def get_token_type(token):
    end_index = token.index(">")
    return token[1:end_index]

def get_token_contents(token):
    if (">" in token) and ("</" in token):
        begin_index = token.index(">")+1
        end_index = token.index("</") 
        return token[begin_index:end_index]
    else:
        return ""

###############################

def compileClass():
    pass

def compileClassVarDec():
    pass

def compileSubroutine():
    pass

def compileParameterList():
    pass

def compileSubroutineBody():
    pass

def compileVarDec():
    pass

def compileStatements():
    pass

def compileLet():
    pass

def compileIf():
    pass

def compileWhile():
    pass

def compileDo():
    pass

def compileReturn():
    pass

def compileReturn():
    pass

def compileExpression():
    pass

def compileTerm():
    pass

def compileExpressionList():
    pass