'''
from curses.ascii import SP
import sys
read_file_name = sys.argv[1]
write_file_name = read_file_name[0:read_file_name.index('.')] + ".asm"
'''
read_file_name = "SimpleAdd.vm"
write_file_name = "SimpleAdd.asm"

# Arithmetic Logical Commands With 2 Variables
alu_double_code = {
    "add" : "D+M", 
    "sub" : "D-M", 
    
    "eq"  : "D-M",
    "gt"  : "D-M",
    "lt"  : "D-M",
    
    "and" : "D&M",
    "or"  : "D|M",
}

alu_single_code = {
    "neg" : "-M", 
    "not" : "!M"
}

alu_comparison_code = {
    "eq"  : "JNE",
    "gt"  : "JLT",
    "lt"  : "JGT",
}

memory_location = {
    "pointer"  : "SP",
    "local"    : "LCL",
    "argument" : "ARG",
    "this"     : "THIS",
    "that"     : "THAT",
    "temp"     : "TEMP"
}


# Arithmetic Logical Commands With 2 Variables

def parser(line):
        commands_list = line.split(' ')
        if len(commands_list) == 1:
            return line, "", ""
        else:
            return commands_list[0], commands_list[1], commands_list[2]

def code_writer(command, arg1, arg2):
    # Process Arithmetic Logical Commands
    
    if command in alu_double_code:
        alc_code = alu_double_code[command]
        return generate_alc_string(alc_code)

    '''
    if arg1 == "":
        if command == "add":
            return generate_add_string()
    '''

    if command == "push":
        return generate_push_string(arg1, arg2)

    #return assembly_string


##########################################
##########################################
##########################################
def move_sp_forward_string():
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M+1" + '\n'
    return assembly_string
##########################################

##########################################
def move_sp_back_string():
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M-1" + '\n'
    return assembly_string
##########################################

##########################################
def set_m_to_sp():
    # Dereference sp pointer value ie: "M = *sp"
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "A=M" + '\n'
    return assembly_string
##########################################


def generate_alc_string(alc_code):
    assembly_string = ""
    assembly_string += move_sp_back_string()
    assembly_string += set_m_to_sp()
    assembly_string += "D=M" + '\n'
    assembly_string += move_sp_back_string()
    assembly_string += set_m_to_sp()
    assembly_string += "M=" + alc_code + '\n'
    assembly_string += move_sp_forward_string()
    return assembly_string


def generate_push_string(arg1, arg2):
    assembly_string = ""
    if arg1 == "constant":
        assembly_string += "@" + arg2 + '\n'
        assembly_string += "D=A" + '\n'
        assembly_string += set_m_to_sp()
        assembly_string += "M=D" + '\n'
        
    else:

        # Put all this into a function...

        # Base address
        arg1_string =  memory_location[arg1]
        assembly_string += "@" + arg1_string + arg2 + '\n'
        assembly_string += "D=A" + '\n'

        # Specified address
        assembly_string += "@" + "arg2" + '\n'
        assembly_string += "A=D+A" + '\n'   # Sets M to location of specified address

        # Store Value
        assembly_string += "D=M" + '\n'

        # Push value to SP
        assembly_string += "@SP" + '\n'
        assembly_string += "A=D" + '\n'

    
    assembly_string += move_sp_forward_string()
    return assembly_string



with open(read_file_name) as read_file:
    write_file = open(write_file_name, "w")
    for line in read_file:
        if line != '\n' and line[0] != '/':
            assembly_string = ""
            line_no_returnchar = line.strip('\n')
            command, arg1, arg2 = parser(line_no_returnchar)
            assembly_string += code_writer(command, arg1, arg2)
            write_file.write(assembly_string)

write_file.close()