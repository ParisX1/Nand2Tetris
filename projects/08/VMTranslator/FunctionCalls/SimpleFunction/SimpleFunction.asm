// generate_function_string
(SimpleFunction.test)
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
// generate_pop_string
// calculate_memory_location
@LCL
D=M
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
// move_sp_forward
@SP
M=M+1
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
// generate_pop_string
// calculate_memory_location
@LCL
D=M
@1
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
// move_sp_forward
@SP
M=M+1
// generate_push_string
// calculate_memory_location
@LCL
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
// generate_push_string
// calculate_memory_location
@LCL
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
M=D+M
// move_sp_forward
@SP
M=M+1
// generate_alc_single_string
// move_sp_back
@SP
M=M-1
// set_m_to_sp
@SP
A=M
D=!M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
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
M=D+M
// move_sp_forward
@SP
M=M+1
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
