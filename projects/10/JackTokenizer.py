from Globals import *

def tokenizer(input_text, write_file_object):
    global is_debug_mode 
    if is_debug_mode: print(input_text)
    input_text_clean = clean_line_text(input_text)
    line_list = create_line_list(input_text_clean)
    if is_debug_mode: print(line_list)
    for item in line_list:
        if item in keyword:
            create_token(item, write_file_object)
        elif item in symbol:
            create_token(item, write_file_object)    
        else:
            i = 0
            while i < len(item):
                token_string = item[0:i+1]
                found = False
                if item[i] in symbol:
                    if i > 0: # Process prior string if not first char
                        create_token(token_string[0:i], write_file_object)
                    create_token(item[i], write_file_object)
                    item = item[i+1:]
                    found = True
                    i = 0
                if found == False:
                    i+=1
                if (i > 0) and (i == len(item)): # If no match for keyword or symbol, use whole string
                    create_token(item, write_file_object)

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
    j = 1
    
    while text[i] == ' ':
        i = i + 1
    j = i + 1
    
    while j < text_len:
        if text[j] == quote: 
            # If you find a quote first, add everything prior to list
            line_list.append(text[i:j])
            i = j
            j = j + 1
        if text[i] == quote:
            # If inside a quote, process the whole quote
            while text[j] != quote:
                j=j+1
            line_list.append(text[i:j+1])
            i = j + 1
            j = i + 1
        elif text[j] == space:
            # If you find a space, add everything into the list
            line_list.append(text[i:j].strip())
            i = j + 1
            j = i + 1
        else:
            j = j + 1
    line_list.append(text[i:j].strip())

    # Check for empty strings
    i = 0
    while i < len(line_list):
        if line_list[i] == '' or line_list[i] == ' ':
            del line_list[i]
            i = 0
        i = i + 1 
    return line_list

def create_token(token_string, write_file_object):
    if token_string in keyword:
        line_to_write = token_string_creator(token_string, "keyword")
    elif token_string in symbol:
        if token_string in symbol_replacement:
            # Check if symbol needs replacement
            token_string = symbol_replacement[token_string]
        line_to_write = token_string_creator(token_string, "symbol")
    elif token_string.isdigit(): 
        line_to_write = token_string_creator(token_string, "integerConstant")
    elif token_string[0] == '"': 
        token_string = token_string.strip('"')
        line_to_write = token_string_creator(token_string, "stringConstant")
    else:
        line_to_write = token_string_creator(token_string, "identifier")
    write_to_file(line_to_write, write_file_object)

def write_to_file(line_to_write, write_file_object):
    write_file_object.write(line_to_write + '\n')

def token_string_creator(token_string, type_string):
    return '<' + type_string + '>' + token_string + "</" + type_string + '>'