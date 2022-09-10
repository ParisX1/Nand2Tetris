import sys
import os

keyword =   ["class", "constructor", "function", "method", "field", "static", "var",
            "int", "char", "boolean", "void", "true", "false", "null", "this", 
            "let", "do", "if", "else", "while", "return"]
symbol =    ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', 
            '|', '<', '>', '=', '~']
multiline_comment = False

def tokenizer(input_text):
    print(input_text)
    input_text_clean = clean_line_text(input_text)
    line_list = create_line_list(input_text_clean)
    print(line_list)
    for item in line_list:
        if item in keyword:
            create_token(item)
        elif item in symbol:
            create_token(item)    
        else:
            i = 0
            while i < len(item):
                token_string = item[0:i+1]
                #print(token_string)
                found = False
                if item[i] in symbol:
                    if i > 0: # Process prior string if not first char
                        create_token(token_string[0:i])
                    create_token(item[i])
                    item = item[i+1:]
                    found = True
                    i = 0
                if found == False:
                    i+=1
                if (i > 0) and (i == len(item)): # If no match for keyword or symbol, use whole string
                    create_token(item)

def clean_line_text(text):
    # Removes comments and tabs
    text = text.strip('\n')
    text = text.strip('\t')
    if "//" in text:
        text = text[:text.index("//")]
    return text

def create_line_list(text):
    # Breaks up items in line by spaces
    line_list = []
    text_len=len(text)
    space = ' '
    quote = '"'
    i = 0
    while text[i] == ' ':
        i = i + 1
    j = i + 1
    while j < text_len:
        if text[j] == quote: # If you find a quote first, add everything prior to list
            line_list.append(text[i:j])
            i = j
            j = j + 1

        if text[i] == quote:
            while text[j] != quote:
                j=j+1
            line_list.append(text[i:j+1])
            i = j + 1
            j = i + 1

        elif text[j] == space:
            line_list.append(text[i:j])
            i = j + 1
            j = i + 1

        else:
            j = j + 1
    line_list.append(text[i:j])

    # Check for empty strings
    i = 0
    while i < len(line_list):
        if line_list[i] == '' or line_list[i] == ' ':
            del line_list[i]
            i = 0
        i = i + 1 

    return line_list

def create_token(token_string):
    if token_string in keyword:
        line_to_write = token_string_creator(token_string, "keyword")
    elif token_string in symbol:
        line_to_write = token_string_creator(token_string, "symbol")
    elif token_string.isdigit(): 
        line_to_write = token_string_creator(token_string, "integerConstant")
    elif token_string[0] == '"': 
        token_string = token_string.strip('"')
        line_to_write = token_string_creator(token_string, "stringConstant")
    else:
        line_to_write = token_string_creator(token_string, "identifier")
    write_to_file(line_to_write)

def write_to_file(line_to_write):
    write_file_object.write(line_to_write + '\n')

def token_string_creator(token_string, type_string):
    return '<' + type_string + '>' + token_string + "</" + type_string + '>'

def line_has_code(line):
    # Check for multiline comments
    global multiline_comment
    if ("/**" in line) or (multiline_comment == True): 
        if "*/" not in line:
            multiline_comment = True
        elif (multiline_comment == True) and "*\\" in line:
            multiline_comment = False    
        return False

    # Checks if the line is empty or only comments
    i = 0
    if line.strip(' ').strip('\t').strip('\n') == '':
            return False
    while i < len(line):
        if (line[i] == '\n') or (line[i:i+2] == "//"):
            return False
        elif line[i] != ' ':
            return True
        i = i + 1

def create_file_list():
    argument_list = sys.argv
    # Argument is file
    if ".jack" in argument_list[1]:
        list_file_names_to_read.append(argument_list[1])
    # Argument is folder
    else:
        folder_path = argument_list[1]
        for file_name_inc_ext in os.listdir(folder_path):
            if file_name_inc_ext[-5:] == ".jack":
                list_file_names_to_read.append(folder_path + "/" + file_name_inc_ext)

def open_write_file(file_to_read):
    file_name_to_write = str(file_to_read).strip(".jack") + ".xml"
    write_file_object = open(file_name_to_write, 'w')
    return write_file_object

if __name__ == "__main__":
    list_file_names_to_read = []   
    create_file_list()
    for file_to_read in list_file_names_to_read:
        print(file_to_read)
        write_file_object = open_write_file(file_to_read)
        write_file_object.write("<tokens>" + '\n')
        multiline_comment = False
        with open(file_to_read, 'r') as file_read_object:
            for line in file_read_object:
                if line_has_code(line):
                    tokenizer(line)
        write_file_object.write("</tokens>" + '\n')
        write_file_object.close()