'''
from curses.ascii import SP
import sys
read_file_name = sys.argv[1]
write_file_name = read_file_name[0:read_file_name.index('.')] + ".asm"
'''
read_file_name = "StackArithmetic\StackTest\StackTest.vm"
write_file_name = "StackArithmetic\StackTest\StackTest.asm"
#global jump_count
jump_count = 0

# Arithmetic Logical Commands With 2 Variables
alc_double_code = {
    "add" : "D+M", 
    "sub" : "M-D", 
    
    "eq"  : "D-M",
    "gt"  : "D-M",
    "lt"  : "D-M",
    
    "and" : "D&M",
    "or"  : "D|M",
}

alc_single_code = {
    "neg" : "-M", 
    "not" : "!M"
}

comparison_code = {
    "eq"  : "JNE",
    "gt"  : "JGE",
    "lt"  : "JLE",
}

memory_location = {
    "pointer"  : "SP",
    "local"    : "LCL",
    "argument" : "ARG",
    "this"     : "THIS",
    "that"     : "THAT",
    "temp"     : "TEMP"
}

##########################################

def parser(line):
        commands_list = line.split(' ')
        if len(commands_list) == 1:
            return line, "", ""
        else:
            return commands_list[0], commands_list[1], commands_list[2]

def code_writer(command, arg1, arg2):
    # Process Arithmetic Logical Commands
    
    if command == "push":
        return generate_push_string(arg1, arg2)

    elif command in comparison_code:
        alc_code = comparison_code[command]
        return generate_comparison_string(alc_code)

    elif command in alc_single_code:
        alc_code = alc_single_code[command]
        return generate_alc_single_string(alc_code)

    elif command in alc_double_code:
        alc_code = alc_double_code[command]
        return generate_alc_double_string(alc_code)
    

##########################################
def move_sp_forward():
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M+1" + '\n'
    return assembly_string
##########################################

##########################################
def move_sp_back():
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M-1" + '\n'
    return assembly_string
##########################################

##########################################
def set_m_to_sp():
    # Dereference sp pointer value ie: "M = *sp"
    # Next instruction: "M = x", will store value x at location RAM[M]
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "A=M" + '\n'
    return assembly_string
##########################################

def generate_alc_double_string(alc_code):
    assembly_string = ""
    assembly_string += move_sp_back()
    assembly_string += set_m_to_sp()
    assembly_string += "D=M" + '\n'
    assembly_string += move_sp_back()
    assembly_string += set_m_to_sp()
    assembly_string += "M=" + alc_code + '\n'
    assembly_string += move_sp_forward()
    return assembly_string

def generate_alc_single_string(alc_code):
    assembly_string = ""
    assembly_string += move_sp_back()
    assembly_string += set_m_to_sp()
    assembly_string += "D=" + alc_code + '\n'
    assembly_string += set_m_to_sp()
    assembly_string += "M=D" + '\n'
    assembly_string += move_sp_forward()
    return assembly_string

def generate_comparison_string(alc_code):
    global jump_count
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M-1" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=M" + '\n'
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M-1" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=D-M" + '\n'
    assembly_string += "@NOT_EQUAL" + str(jump_count) + '\n'
    assembly_string += "D," + alc_code + '\n'
    assembly_string += "(EQUAL" + str(jump_count) + ")" + '\n'
    assembly_string += "D=-1" + '\n'
    assembly_string += "@SP" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "M=D" + '\n'
    assembly_string += "@END_COMPARE" + str(jump_count) + '\n'
    assembly_string += "0,JMP" + '\n'
    assembly_string += "(NOT_EQUAL"+ str(jump_count) + ")" + '\n'
    assembly_string += "D=0" + '\n'
    assembly_string += "@SP" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "M=D" + '\n'
    assembly_string += "(END_COMPARE" + str(jump_count) + ")" + '\n'
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M+1" + '\n'
    jump_count += 1
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

    assembly_string += move_sp_forward()
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