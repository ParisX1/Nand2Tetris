// create_bootstrap_string
@256
D=A
@SP
M=D
// generate_call_string
@$ret.1
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save LCL
// move_sp_forward
@SP
M=M+1
@LCL
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save ARG
// move_sp_forward
@SP
M=M+1
@ARG
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THIS
// move_sp_forward
@SP
M=M+1
@THIS
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THAT
// move_sp_forward
@SP
M=M+1
@THAT
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// Reposition ARG
@5
D=A
@SP
A=M-D
D=A
@ARG
M=D
// Reposition LCL
@SP
A=M
D=A
@LCL
M=D
// Jmp to function
@Sys.init
0,JMP
($ret.1)
// generate_function_string
(Sys.init)
// generate_push_string
@6
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_push_string
@8
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_call_string
@Sys.init$ret.2
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save LCL
// move_sp_forward
@SP
M=M+1
@LCL
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save ARG
// move_sp_forward
@SP
M=M+1
@ARG
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THIS
// move_sp_forward
@SP
M=M+1
@THIS
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THAT
// move_sp_forward
@SP
M=M+1
@THAT
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// Reposition ARG
@7
D=A
@SP
A=M-D
D=A
@ARG
M=D
// Reposition LCL
@SP
A=M
D=A
@LCL
M=D
// Jmp to function
@Class1.set
0,JMP
(Sys.init$ret.2)
// generate_pop_string
// calculate_memory_location
@5
D=A
@0
D=D+A
@R13
M=D
// move_sp_back
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// generate_push_string
@23
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_push_string
@15
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_call_string
@Sys.init$ret.3
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save LCL
// move_sp_forward
@SP
M=M+1
@LCL
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save ARG
// move_sp_forward
@SP
M=M+1
@ARG
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THIS
// move_sp_forward
@SP
M=M+1
@THIS
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THAT
// move_sp_forward
@SP
M=M+1
@THAT
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// Reposition ARG
@7
D=A
@SP
A=M-D
D=A
@ARG
M=D
// Reposition LCL
@SP
A=M
D=A
@LCL
M=D
// Jmp to function
@Class2.set
0,JMP
(Sys.init$ret.3)
// generate_pop_string
// calculate_memory_location
@5
D=A
@0
D=D+A
@R13
M=D
// move_sp_back
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// generate_call_string
@Sys.init$ret.4
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save LCL
// move_sp_forward
@SP
M=M+1
@LCL
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save ARG
// move_sp_forward
@SP
M=M+1
@ARG
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THIS
// move_sp_forward
@SP
M=M+1
@THIS
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THAT
// move_sp_forward
@SP
M=M+1
@THAT
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// Reposition ARG
@5
D=A
@SP
A=M-D
D=A
@ARG
M=D
// Reposition LCL
@SP
A=M
D=A
@LCL
M=D
// Jmp to function
@Class1.get
0,JMP
(Sys.init$ret.4)
// generate_call_string
@Sys.init$ret.5
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save LCL
// move_sp_forward
@SP
M=M+1
@LCL
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save ARG
// move_sp_forward
@SP
M=M+1
@ARG
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THIS
// move_sp_forward
@SP
M=M+1
@THIS
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// Save THAT
// move_sp_forward
@SP
M=M+1
@THAT
A=M
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// Reposition ARG
@5
D=A
@SP
A=M-D
D=A
@ARG
M=D
// Reposition LCL
@SP
A=M
D=A
@LCL
M=D
// Jmp to function
@Class2.get
0,JMP
(Sys.init$ret.5)
// generate_label_string
(Sys.main$WHILE)
// generate_goto_string
@Sys.main$WHILE
0; JMP
// generate_function_string
(Class2.set)
// generate_push_string
// calculate_memory_location
@ARG
D=M
@0
D=D+A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_pop_string
// calculate_memory_location
@Class20
D=A
@R13
M=D
// move_sp_back
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// generate_push_string
// calculate_memory_location
@ARG
D=M
@1
D=D+A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_pop_string
// calculate_memory_location
@Class21
D=A
@R13
M=D
// move_sp_back
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// generate_push_string
@0
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_return_string
@LCL
A=M
D=A
@R13
M=D
@5
D=A
@LCL
A=M
D=A-D
A=D
A=M
D=A
@R14
M=D
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
A=M
D=A
@SP
M=D
// move_sp_forward
@SP
M=M+1
// restore_values
@1
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THAT
M=D
// restore_values
@2
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THIS
M=D
// restore_values
@3
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@ARG
M=D
// restore_values
@4
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@LCL
M=D
@R14
A=M
0,JMP
// generate_function_string
(Class2.get)
// generate_push_string
// calculate_memory_location
@Class20
D=A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_push_string
// calculate_memory_location
@Class21
D=A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_alc_double_string
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
D=M
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
M=M-D
// move_sp_forward
@SP
M=M+1
// generate_return_string
@LCL
A=M
D=A
@R13
M=D
@5
D=A
@LCL
A=M
D=A-D
A=D
A=M
D=A
@R14
M=D
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
A=M
D=A
@SP
M=D
// move_sp_forward
@SP
M=M+1
// restore_values
@1
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THAT
M=D
// restore_values
@2
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THIS
M=D
// restore_values
@3
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@ARG
M=D
// restore_values
@4
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@LCL
M=D
@R14
A=M
0,JMP
// generate_function_string
(Class1.set)
// generate_push_string
// calculate_memory_location
@ARG
D=M
@0
D=D+A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_pop_string
// calculate_memory_location
@Class10
D=A
@R13
M=D
// move_sp_back
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// generate_push_string
// calculate_memory_location
@ARG
D=M
@1
D=D+A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_pop_string
// calculate_memory_location
@Class11
D=A
@R13
M=D
// move_sp_back
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// generate_push_string
@0
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_return_string
@LCL
A=M
D=A
@R13
M=D
@5
D=A
@LCL
A=M
D=A-D
A=D
A=M
D=A
@R14
M=D
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
A=M
D=A
@SP
M=D
// move_sp_forward
@SP
M=M+1
// restore_values
@1
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THAT
M=D
// restore_values
@2
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THIS
M=D
// restore_values
@3
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@ARG
M=D
// restore_values
@4
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@LCL
M=D
@R14
A=M
0,JMP
// generate_function_string
(Class1.get)
// generate_push_string
// calculate_memory_location
@Class10
D=A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_push_string
// calculate_memory_location
@Class11
D=A
A=D
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_alc_double_string
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
D=M
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
M=M-D
// move_sp_forward
@SP
M=M+1
// generate_return_string
@LCL
A=M
D=A
@R13
M=D
@5
D=A
@LCL
A=M
D=A-D
A=D
A=M
D=A
@R14
M=D
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
A=M
D=A
@SP
M=D
// move_sp_forward
@SP
M=M+1
// restore_values
@1
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THAT
M=D
// restore_values
@2
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@THIS
M=D
// restore_values
@3
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@ARG
M=D
// restore_values
@4
D=A
@R13
A=M
D=A-D
A=D
A=M
D=A
@LCL
M=D
@R14
A=M
0,JMP
