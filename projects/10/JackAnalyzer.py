import sys
import os

keyword =   ["class", "constructor", "function", "method", "field", "static", "var",
            "int", "chat", "boolean", "void", "true", "false", "null", "this", 
            "let", "do", "if", "else", "while", "return" ]
symbol = []



if __name__ == "__main__":
    list_file_names_to_read = []   
    # Process args
    argument_list = sys.argv

    # Argument is file
    if ".jack" in argument_list[1]:
        list_file_names_to_read.append(argument_list[1])
    
    # Argument is folder
    else:
        folder_path = argument_list[1]

        for file_name_inc_ext in os.listdir(folder_path):
            if file_name_inc_ext[-5:] == ".jack":
                list_file_names_to_read.append(file_name_inc_ext)



    # Open folder
    # Read lines

    pass