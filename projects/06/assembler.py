#########################################################################################
###################################### INSTRUCTION DATA #################################
#########################################################################################

c_dict = {
    ""   : "000000",
    "0"  : "101010",
    "1"  : "111111",
    "-1" : "111010",
    "D"  : "001100",
    "A"  : "110000",
    "M"  : "110000",
    "!D" : "001101",
    "!A" : "110001",
    "!M" : "110001",
    "-D" : "001111",
    "-A" : "110011",
    "-M" : "110011",
    "D+1": "011111",
    "A+1": "110111",
    "M+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "M-1": "110010",
    "D+A": "000010",
    "D+M": "000010",
    "M+A": "000010",
    "D-A": "010011",
    "D-M": "010011",
    "A-D": "000111",
    "M-D": "000111",
    "A&M": "000000",
    "D&M": "000000",
    "D|A": "010101",
    "D|M": "010101"
}

d_dict = {
    ""    : "000",
    "M"   : "001",
    "D"   : "010",
    "DM"  : "011",
    "MD"  : "011",
    "A"   : "100",
    "AM"  : "101",
    "MA"  : "101",
    "AD"  : "110",
    "DA"  : "110",
    "ADM" : "111"
}

j_dict = {
    ""    : "000",
    "JGT" : "001",
    "JEQ" : "010",
    "JGE" : "011",
    "JLT" : "100",
    "JNE" : "101",
    "JLE" : "110",
    "JMP" : "111"
}

symbol_dict = {
    "R0"     : "0000000000000000",
    "R1"     : "0000000000000001",
    "R2"     : "0000000000000010",
    "R3"     : "0000000000000011",
    "R4"     : "0000000000000100",
    "R5"     : "0000000000000101",
    "R6"     : "0000000000000110",
    "R7"     : "0000000000000111",
    "R8"     : "0000000000001000",
    "R9"     : "0000000000001001",
    "R10"    : "0000000000001010",
    "R11"    : "0000000000001011",
    "R12"    : "0000000000001100",
    "R13"    : "0000000000001101",
    "R14"    : "0000000000001110",
    "R15"    : "0000000000001111",
    "R15"    : "0000000000001111",
    "SP"     : "0000000000000000",
    "LCL"    : "0000000000000001",
    "ARG"    : "0000000000000010",
    "THIS"   : "0000000000000011",
    "THAT"   : "0000000000000100",
    "SCREEN" : "0100000000000000",
    "KBD"    : "0110000000000000"
}

#########################################################################################
######################################### FUNCTIONS #####################################
#########################################################################################

def convert_num_to_binary(number_string):
    number_decimal = int(number_string)
    number_binary = ""
    number_place = 0
    while number_place < 15:
        power = 14 - number_place
        num_to_check = number_decimal // (2**power)
        if num_to_check > 0:
            number_binary += "1" 
            number_decimal = number_decimal - (num_to_check * (2**power))
        else:
            number_binary += "0"
        number_place += 1
    return number_binary

def line_has_code(line_text):
    if line_text != "\n" and line_text[0] != "/":
        return True
    else:
        return False

def add_to_symbol_table(line_name, line_number):
    symbol_dict[line_name] = str(line_number)

def parser(instruction_string):
    # Check if calculation
    if '=' in instruction_string:
        dest_string = get_dest_string(instruction_string, '=')
        comp_string = get_instruct_string(instruction_string, '=')
        jmp_string = ""

    # Check if jump
    if ';' in instruction_string:
        dest_string = ""
        comp_string = get_dest_string(instruction_string, ';')
        jmp_string = get_instruct_string(instruction_string, ';')
    
    return dest_string, comp_string, jmp_string

def get_dest_string(instruction_string, delim_char):
    i = 0
    return_string = ""
    while instruction_string[i] != delim_char:
        return_string += instruction_string[i]
        i += 1
    return return_string

def get_instruct_string(instruction_string, delim_char):
    i = instruction_string.index(delim_char) + 1
    return instruction_string[i:]

def strings_to_binary(dest_string, comp_string, jump_string):
    instruction_string = "111"
    if 'M' in comp_string:
        a_binary = '1'
    else:
        a_binary = '0'
    comp_binary = c_dict[comp_string]
    dest_binary = d_dict[dest_string]
    jmp_binary = j_dict[jump_string]

    return instruction_string + a_binary + comp_binary + dest_binary + jmp_binary

def clean_line(line):
    # Remove all spaces, comments and return chars from line
    line_no_space = line.strip(' ')
    line_no_comments = ""
    i = 0
    while line_no_space[i] != '/' and line_no_space[i] != '\n':
        line_no_comments += line_no_space[i]
        i+=1
    return line_no_comments

#########################################################################################
########################################### INPUTS ######################################
#########################################################################################

file_to_open   = "pong/PongL.asm"
file_to_create = "Pong.hack"

#########################################################################################
#################################### RUNNING CODE #######################################
#########################################################################################

# Open File to Write
write_file = open(file_to_create, 'w')

# Open File to Read
with open(file_to_open) as read_file:
    # 1. Populate Symbol Table
    '''
    ### TO DO ###
    line_number = 0
    for line in read_file:
        if line_has_code(line):
            if line[0] == '(':
                add_to_symbol_table(line[1:-2], line_number)
            line_number += 1
    '''

    # 2. Translate each line
    line_number = 0
    for line in read_file:
        if line_has_code(line):
            line_clean = clean_line(line)

            # A-instruction
            if line_clean[0] == "@": 
                if line_clean[1] != 'R':
                    write_string = '0' + convert_num_to_binary(line_clean[1:])
                else: 
                    write_string = '0' + symbol_dict[line_clean[1:]]
                write_file.write(write_string + '\n')
            
            # C-instruction
            else:
                dest_string, comp_string, jump_string = parser(line_clean)
                instruction_binary = strings_to_binary(dest_string, comp_string, jump_string)
                write_file.write(instruction_binary + '\n')

write_file.close()
