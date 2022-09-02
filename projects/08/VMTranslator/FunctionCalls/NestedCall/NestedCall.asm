// create_bootstrap_string
@256
D=A
@SP
M=D
// generate_function_string
(Sys.init)
// generate_push_string
@4000	//
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
@THIS
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
@5000
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
@THAT
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
// generate_call_string
// generate_return_address_string
($ret.1)
// move_sp_forward
@SP
M=M+1
// move_sp_forward
@SP
M=M+1
@LCL
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@ARGLCL
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@THIS
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@THAT
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@Sys.main
0,JMP
// generate_pop_string
// calculate_memory_location
@5
D=A
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
// generate_label_string
(Sys.main$LOOP)
// generate_goto_string
@Sys.main$LOOP
0; JMP
// generate_function_string
(Sys.main)
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
@2
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
@3
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
@4
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
@4001
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
@THIS
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
@5001
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
@THAT
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
@200
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
// generate_push_string
@40
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
@2
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
@6
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
@3
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
@123
D=A
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
// generate_call_string
// generate_return_address_string
($ret.2)
// move_sp_forward
@SP
M=M+1
// move_sp_forward
@SP
M=M+1
@LCL
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@ARGLCL
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@THIS
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@THAT
D=M
// set_m_to_sp
@SP
A=M
M=D
// move_sp_forward
@SP
M=M+1
@Sys.add12
0,JMP
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
// generate_push_string
// calculate_memory_location
@LCL
D=M
@2
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
@3
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
@4
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
// generate_function_string
(Sys.add12)
// generate_push_string
@4002
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
@THIS
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
@5002
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
@THAT
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
@12
D=A
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
