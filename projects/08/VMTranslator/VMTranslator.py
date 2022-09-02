import sys
import os

jump_count = 0              # Global jump_count for jump labels
function_name = "main"      # Track function names for function labels
local_var_count = 0         # Track number of local variables for active function
call_count = 0              # Track calls for labelling return address in saved frame
current_function_name = ""  # Track name of active function ti  label return address in saved frame

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

def create_bootstrap_string():
    assembly_string = ""
    assembly_string += "// create_bootstrap_string\n"
    assembly_string += "@256" + '\n'
    assembly_string += "D=A" + '\n'
    assembly_string += "@SP" + '\n'
    assembly_string += "M=D" + '\n'
    return assembly_string

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

    elif command == "call":
            return generate_call_string(arg1, arg2)
    
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
    assembly_string += "// move_sp_forward\n"
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M+1" + '\n'
    return assembly_string

def move_sp_back():
    assembly_string = ""
    assembly_string += "// move_sp_back\n"
    assembly_string += "@SP" + '\n'
    assembly_string += "M=M-1" + '\n'
    return assembly_string

def set_m_to_sp():
    # Dereference sp pointer value ie: "M = *sp"
    # Next instruction: "M = x", will store value x at location RAM[M]
    assembly_string = ""
    assembly_string += "// set_m_to_sp\n"
    assembly_string += "@SP" + '\n'
    assembly_string += "A=M" + '\n'
    return assembly_string

def generate_alc_double_string(alc_code):
    assembly_string = ""
    assembly_string += "// generate_alc_double_string\n"
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
    assembly_string += "// generate_alc_single_string\n"
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
    assembly_string += "// generate_comparison_string\n"
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
    assembly_string += "// calculate_memory_location\n"
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
        assembly_string += "@" + file_name_no_ext + arg2 + '\n'
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
    assembly_string += "// restore_values\n"
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
    assembly_string += "// generate_push_string\n"
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
    assembly_string += "// generate_pop_string\n"
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
    assembly_string += "// generate_label_string\n"
    assembly_string += '(' + convert_label_name(arg1) + ')' + '\n'
    return assembly_string

def generate_function_string(arg1, arg2):
    # When a function line is executed eg "function SimpleFunction.test 2"
    # Labels function line and sets n local variables to zero
    current_function_name = arg1
    assembly_string = ""
    assembly_string += "// generate_function_string\n"
    assembly_string += '(' + arg1 + ')' + '\n'
    local_var_count = int(arg2)
    for i in range(local_var_count):
        assembly_string += generate_push_string("constant", "0")
        assembly_string += generate_pop_string("local", str(i))
        assembly_string += move_sp_forward()
    return assembly_string

def generate_return_address_string():
    global call_count
    call_count += 1
    assembly_string = ""
    assembly_string += "// generate_return_address_string\n"
    assembly_string += '(' + current_function_name + "$ret." + str(call_count) + ')' + '\n'
    return assembly_string

def generate_call_string(arg1, arg2):
    assembly_string = ""
    assembly_string += "// generate_call_string\n"
    # Create return label
    assembly_string += generate_return_address_string()
    assembly_string += move_sp_forward()

    # Save LCL
    assembly_string += move_sp_forward()
    assembly_string += "@LCL" + '\n'
    assembly_string += "D=M" + '\n'
    assembly_string += set_m_to_sp()
    assembly_string += "M=D" + '\n'

    # Save ARG
    assembly_string += move_sp_forward()
    assembly_string += "@ARGLCL" + '\n'
    assembly_string += "D=M" + '\n'
    assembly_string += set_m_to_sp()
    assembly_string += "M=D" + '\n'

    # Save THIS
    assembly_string += move_sp_forward()
    assembly_string += "@THIS" + '\n'
    assembly_string += "D=M" + '\n'
    assembly_string += set_m_to_sp()
    assembly_string += "M=D" + '\n'

    # Save THAT
    assembly_string += move_sp_forward()
    assembly_string += "@THAT" + '\n'
    assembly_string += "D=M" + '\n'
    assembly_string += set_m_to_sp()
    assembly_string += "M=D" + '\n'
        
    # Jump to execute called function
    assembly_string += move_sp_forward()
    assembly_string += "@" + arg1 + '\n'
    assembly_string += "0,JMP" + '\n'

    return assembly_string

def generate_return_string(num_args):
    assembly_string = ""
    assembly_string += "// generate_return_string\n"
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
    assembly_string += "// generate_ifgoto_string\n"
    label_name = convert_label_name(arg1)
    assembly_string += move_sp_back()
    assembly_string += "@" + label_name + '\n'
    assembly_string += "D; JNE" + '\n'
    return assembly_string

def generate_goto_string(arg1):
    assembly_string = ""
    assembly_string += "// generate_goto_string\n"
    label_name = convert_label_name(arg1)
    assembly_string += "@" + label_name + '\n'
    assembly_string += "0; JMP" + '\n'
    return assembly_string

def convert_label_name(label_name):
    label_string = ""
    label_string += file_name_no_ext + '.' + function_name + '$' + label_name
    return label_string

def add_bootstrap_code():
    assembly_string = ""
    assembly_string += create_bootstrap_string()
    write_file_name_inc_ext.write(assembly_string)

def get_folder_name():
    i = -1
    curr_char = application_argument_supplied[i]
    while curr_char != '/':
        i-=1
        curr_char = application_argument_supplied[i]
    return application_argument_supplied[i+1:]

def get_directory_path():
    i = -1
    curr_char = application_argument_supplied[i]
    while curr_char != '/':
        i-=1
        curr_char = application_argument_supplied[i]
    return application_argument_supplied[0:i:]

if __name__ == "__main__":
    list_file_names_to_read = []   # .vm files to process.  Name only, no folder path
    application_argument_supplied = sys.argv[1]
    is_file_to_read = ".vm" in application_argument_supplied
    
    if is_file_to_read: # Reading single file
        directory_path = get_directory_path()    
        write_file_full_path = application_argument_supplied[0:application_argument_supplied.index('.')] + ".asm"
        write_file_name_inc_ext = open(write_file_full_path, "w")
        file_name_inc_ext = os.path.basename(application_argument_supplied)
        list_file_names_to_read.append(file_name_inc_ext)
   
    else: # Reading directory
        # Get folder name and create write file
        folder_name = get_folder_name()
        directory_path = application_argument_supplied
        write_file_full_path = directory_path + '/' + folder_name + ".asm"
        write_file_name_inc_ext = open(write_file_full_path, "w")
        add_bootstrap_code()
        # Add .vm files to list_files_to_read
        for file_name_inc_ext in os.listdir(application_argument_supplied):
            if file_name_inc_ext[-3:] == ".vm":
                list_file_names_to_read.append(file_name_inc_ext)
        assert "Sys.vm" in list_file_names_to_read # Check that list contains Sys.vm or throw error
        # Ensure Sys.vm is first file in list_files_to_read
        for i in range(len(list_file_names_to_read)):
            if list_file_names_to_read[i] == "Sys.vm":
                list_file_names_to_read[i] = list_file_names_to_read[0]
                list_file_names_to_read[0] = "Sys.vm"

    for read_file_name_inc_ext in list_file_names_to_read:
        file_name_no_ext = read_file_name_inc_ext.strip(".vm")
        read_file_name_full_path_inc_ext = directory_path + '/' + read_file_name_inc_ext
        with open(read_file_name_full_path_inc_ext) as read_file:
            for line in read_file:
                if line != '\n' and line[0] != '/':
                    assembly_string = ""
                    line_no_returnchar = line.strip('\n')
                    command, arg1, arg2 = parser(line_no_returnchar)
                    assembly_string += code_writer(command, arg1, arg2)
                    write_file_name_inc_ext.write(assembly_string)
    write_file_name_inc_ext.close()