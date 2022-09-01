import sys
import os

read_file_full_path = sys.argv[1]
read_file_name = os.path.basename(read_file_full_path)
base_file_name = read_file_name[0:read_file_name.index('.')]

write_file_full_path = read_file_full_path[0:read_file_full_path.index('.')] + ".asm"

jump_count = 0          # Global jump_count for jump labels
function_name = "main"  # Track function names for function labels
local_var_count = 0     # Track number of local variables for active function

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
    "local"    : "LCL",
    "argument" : "ARG",
    "this"     : "THIS",
    "that"     : "THAT",
}

##########################################

def parser(line):
        commands_list = line.split(' ')
        if len(commands_list) == 1:
            return line, "", ""
        if len(commands_list) == 2:
            return commands_list[0], commands_list[1], ""
        else:
            return commands_list[0], commands_list[1], commands_list[2]

def code_writer(command, arg1, arg2):
    if command == "push":
        return generate_push_string(arg1, arg2)

    elif command == "pop":
        return generate_pop_string(arg1, arg2)

    elif command == "label":
            return generate_label_string(arg1)
    
    elif command == "function":
            return generate_function_string(arg1, arg2)

    elif command == "if-goto":
            return generate_ifgoto_string(arg1)

    elif command == "goto":
            return generate_goto_string(arg1)

    elif command == "return":
            return generate_return_string(arg2)

    elif command in comparison_code:
        alc_code = comparison_code[command]
        return generate_comparison_string(alc_code)

    elif command in alc_single_code:
        alc_code = alc_single_code[command]
        return generate_alc_single_string(alc_code)

    elif command in alc_double_code:
        alc_code = alc_double_code[command]
        return generate_alc_double_string(alc_code)
    
def move_sp_forward():
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M+1" + '\n'
    return assembly_string

def move_sp_back():
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M-1" + '\n'
    return assembly_string

def set_m_to_sp():
    # Dereference sp pointer value ie: "M = *sp"
    # Next instruction: "M = x", will store value x at location RAM[M]
    assembly_string = ""
    assembly_string += "@SP" + '\n'
    assembly_string += "A=M" + '\n'
    return assembly_string

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

def calculate_memory_location(arg1, arg2):
    # Sets D-register to location specified by arg1, arg2
    # Eg "temp 2" will set: D = value of temp 2 location in RAM
    assembly_string = ""
    if arg1 =="temp":
        assembly_string += "@5" + '\n' # Base memory for temp
        assembly_string += "D=A" + '\n'
        assembly_string += "@" + arg2 + '\n'
        assembly_string += "D=D+A" + '\n'

    elif arg1 =="pointer":
        if arg2 == '0':
            assembly_string += "@THIS" + '\n' # Base memory for this
        else:
            assembly_string += "@THAT" + '\n' # Base memory for that
        assembly_string += "D=A" + '\n'

    elif arg1 =="static":
        assembly_string += "@" + base_file_name + arg2 + '\n'
        assembly_string += "D=A" + '\n'

    else:
        arg1_string =  memory_location[arg1]
        assembly_string += "@" + arg1_string + '\n'
        assembly_string += "D=M" + '\n'
        
        assembly_string += "@" + arg2 + '\n'
        assembly_string += "D=D+A" + '\n'
    
    return assembly_string

def restore_values(memory_name):
    assembly_string = ""
    if memory_name == "THAT":   offest = '1' 
    if memory_name == "THIS":   offest = '2'
    if memory_name == "ARG":    offest = '3'
    if memory_name == "LCL":    offest = '4'
    
    # Store value of offset in D
    assembly_string += "@" + offest + '\n'
    assembly_string += "D=A" + '\n'

    # Get value of LCL and deduct offset
    assembly_string += "@R13" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=A-D" + '\n'

    # Store value at memory location D into D
    assembly_string += "A=D" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=A" + '\n'

    # Store value of D into base memory
    assembly_string += "@" + memory_name + '\n'
    assembly_string += "M=D" + '\n'

    return assembly_string


def generate_push_string(arg1, arg2):
    assembly_string = ""
    if arg1 == "constant":
        assembly_string += "@" + arg2 + '\n'
        assembly_string += "D=A" + '\n'
        assembly_string += set_m_to_sp()
        assembly_string += "M=D" + '\n'
    else:
        assembly_string += calculate_memory_location(arg1, arg2)
        assembly_string += "A=D" + '\n'
        assembly_string += "D=M" + '\n'
        assembly_string += set_m_to_sp()
        assembly_string += "M=D" + '\n' # Stores value at SP location
    assembly_string += move_sp_forward()
    return assembly_string

def generate_pop_string(arg1, arg2):
    assembly_string = ""
    #1. Calculate memory location
    assembly_string += calculate_memory_location(arg1, arg2)
    assembly_string += "@R13" + '\n'
    assembly_string += "M=D" + '\n' # Location to put value saved in R13
    #2. Get value from stack
    assembly_string += move_sp_back()
    assembly_string += "@SP" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=M" + '\n'
    #3. Place value at location
    assembly_string += "@R13" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "M=D" + '\n'
    return assembly_string

def generate_label_string(arg1):
    assembly_string = ""
    assembly_string += '(' + convert_label_name(arg1) + ')' + '\n'
    return assembly_string

def generate_function_string(arg1, arg2):
    # When a function line is executed eg "function SimpleFunction.test 2"
    # Labels function line and sets n local variables to zero
    assembly_string = ""
    assembly_string += '(' + arg1 + ')' + '\n'
    local_var_count = int(arg2)
    for i in range(local_var_count):
        assembly_string += generate_push_string("constant", "0")
        assembly_string += generate_pop_string("local", str(i))
        assembly_string += move_sp_forward()
    return assembly_string

def generate_return_string(num_args):
    assembly_string = ""
    # 1. Save LCL into R13
    assembly_string += "@LCL" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=A" + '\n'
    assembly_string += "@R13" + '\n'
    assembly_string += "M=D" + '\n'
    # 2. Save return address (LCL - 5) to R14 
    assembly_string += "@5" + '\n'     # Calc where in memory the ret address is
    assembly_string += "D=A" + '\n'
    assembly_string += "@LCL" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=A-D" + '\n'  # D = memory location of ret address 
    
    assembly_string += "A=D" + '\n'     # Goto return address location and save value
    assembly_string += "A=M" + '\n'
    assembly_string += "D=A" + '\n'    # D = value of return address

    assembly_string += "@R14" + '\n'    # Save value of return address in R14
    assembly_string += "M=D" + '\n'

    # 3. Place return value back to return address
    assembly_string += move_sp_back() # Save return value into D
    assembly_string += set_m_to_sp()
    assembly_string += "D=M" + '\n'

    assembly_string += "@ARG" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "M=D" + '\n'

    # 4. Reset stack pointer
    assembly_string += "@ARG" + '\n'
    assembly_string += "A=M" + '\n'
    assembly_string += "D=A" + '\n'
    assembly_string += "@SP" + '\n'
    assembly_string += "M=D" + '\n'
    assembly_string += move_sp_forward()

    # Restore THAT, THIS, LOCAL
    assembly_string += restore_values("THAT")
    assembly_string += restore_values("THIS")
    assembly_string += restore_values("ARG")
    assembly_string += restore_values("LCL")
    
    return assembly_string

def generate_ifgoto_string(arg1):
    assembly_string = ""
    label_name = convert_label_name(arg1)
    assembly_string += move_sp_back()
    assembly_string += "@" + label_name + '\n'
    assembly_string += "D; JNE" + '\n'
    return assembly_string

def generate_goto_string(arg1):
    assembly_string = ""
    label_name = convert_label_name(arg1)
    assembly_string += "@" + label_name + '\n'
    assembly_string += "0; JMP" + '\n'
    return assembly_string

'''
def create_function_name(function_name):
    # Converts a function name for labelling
    # Function name eg "myFunc" in file "fileName" -> fileName.myFunc
    label_string = ""
    label_string += base_file_name + '.' + function_name
    return label_string
'''

def convert_label_name(label_name):
    label_string = ""
    label_string += base_file_name + '.' + function_name + '$' + label_name
    return label_string

with open(read_file_full_path) as read_file:
    write_file = open(write_file_full_path, "w")
    for line in read_file:
        if line != '\n' and line[0] != '/':
            assembly_string = ""
            line_no_returnchar = line.strip('\n')
            command, arg1, arg2 = parser(line_no_returnchar)
            assembly_string += code_writer(command, arg1, arg2)
            write_file.write(assembly_string)

write_file.close()