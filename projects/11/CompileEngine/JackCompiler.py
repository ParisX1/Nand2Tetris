'''
Jack Compiler
- Reads .jack files in folder or file passed as arguments
- Opens write file to create tokens (raw list and with context wrapping)
- Loops over files reading jack code, passing data to CompileEngine.py
'''

import sys
import os
from JackTokenizer import *
from CompileEngine import *
from Globals import *

def line_has_code(line):
    # Check for multiline comments
    global multiline_comment
    if ("/**" in line) or (multiline_comment == True): 
        if "*/" not in line:
            multiline_comment = True
        elif (multiline_comment == True) and "*/" in line:
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

def open_write_file(file_to_read, old_ext, new_ext, fileNameAdd=""):
    file_name_to_write = str(file_to_read).replace(old_ext,"") + fileNameAdd + new_ext
    write_file_object = open(file_name_to_write, 'w')
    return write_file_object

if __name__ == "__main__":
    list_file_names_to_read = []   
    list_token_file_names = []
    token_filename_ext = "T"
    compile_filename_ext = ""
    
    '''
    Change this so we create the token array for each file
    Then once we've read the file, created the token file output (and so
    the token array is complete), we can then process the parser.
    So instead of reading all the files, then processing the parser,
    we each one file, parse that file, then clear the token array
    and run the tokeniser on the next file, and so on.
    '''

    create_file_list() # List of Jack files to process

    for file_to_read in list_file_names_to_read:
        if is_debug_mode: print(file_to_read)
        
        # 1. Create tokens -> Create file of tokens (eg MainT.xml)
        write_file_object = open_write_file(file_to_read, ".jack", ".xml", token_filename_ext)
        list_token_file_names.append(write_file_object.name)
        write_file_object.write("<tokens>" + '\n')
        multiline_comment = False
        with open(file_to_read, 'r') as file_read_object:
            for line in file_read_object:
                if line_has_code(line):
                    tokenizer(line, write_file_object)
        write_file_object.write("</tokens>" + '\n')
        write_file_object.close()

        # 2. Parse tokens -> Create file of analysed tokens eg (Main.xml)
        file_to_write = file_to_read
        write_file_object = open_write_file(file_to_write, ".jack", ".xml", compile_filename_ext)
        parser(write_file_object)
        write_file_object.close()
        token_list.clear()
