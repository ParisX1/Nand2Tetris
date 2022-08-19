from curses.ascii import SP
import sys
read_file = sys.argv[1]
write_file = read_file[0:read_file.index('.')] + ".asm"
arithmetic_logical_commands = {
    "add" : "D+A", 
    "sub" : "", 
    "neg" : "", 
    "eq"  : "",
    "gt"  : "",
    "lt"  : "",
    "and" : "",
    "or"  : "",
    "not" : ""
}

def parser(line):
        commands_list = line.split(' ')
        
        if len(commands_list) == 1:
            return line, "", ""
        else:
            return commands_list[0], commands_list[1], commands_list[2]

def code_writer(command, arg1, arg2):
    # Process Arithmetic Logical Commands
    
    if arg1 == "":
        if command == "add":
            return generate_add_string()
        
        if command == "push":
            return generate_push_string(command, arg1, arg2)

    return assembly_string

def generate_add_string():
    assembly_string = ""
    assembly_string += "@SP"
    assembly_string += "D=M"
    assembly_string += "M=M-1"
    assembly_string += "@SP"
    assembly_string += "A=M"
    assembly_string += "M=M-1"
    assembly_string += "A=D-A"
    assembly_string += "@SP"
    assembly_string += "M=A"
    assembly_string += "@SP"
    assembly_string += "M=M+1"
    return assembly_string


def generate_push_string(command, arg1, arg2):
    assembly_string = ""
    if arg1 == "constant":
        assembly_string = "@" + arg2
        assembly_string = "D=A"
        assembly_string = "@SP"
        assembly_string = "A=M"
        assembly_string = "M=D"
        assembly_string = "@SP"
        assembly_string = "M=M+1"
    return assembly_string


with open(read_file):
    for line in read_file:
        if line != '\n' and line[0] != '/':
            line.strip('\n')
            command, arg1, arg2 = parser(line)
            assembly_string = code_writer(command, arg1, arg2)
            write_file.write(assembly_string + '\n')

write_file.close()