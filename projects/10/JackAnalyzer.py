import sys
import os

keyword =   ["class", "constructor", "function", "method", "field", "static", "var",
            "int", "chat", "boolean", "void", "true", "false", "null", "this", 
            "let", "do", "if", "else", "while", "return"]
symbol = []


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
                list_file_names_to_read.append(file_name_inc_ext)

if __name__ == "__main__":
    list_file_names_to_read = []   
    create_file_list()

    for file_to_read in list_file_names_to_read:
        with open(file_to_read, 'r') as file_read_object:
            for line in file_read_object:
                print(line)
