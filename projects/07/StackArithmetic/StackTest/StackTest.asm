@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL0
D,JNE
(EQUAL0)
D=-1
@SP
A=M
M=D
@END_COMPARE0
0,JMP
(NOT_EQUAL0)
D=0
@SP
A=M
M=D
(END_COMPARE0)
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL1
D,JNE
(EQUAL1)
D=-1
@SP
A=M
M=D
@END_COMPARE1
0,JMP
(NOT_EQUAL1)
D=0
@SP
A=M
M=D
(END_COMPARE1)
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL2
D,JNE
(EQUAL2)
D=-1
@SP
A=M
M=D
@END_COMPARE2
0,JMP
(NOT_EQUAL2)
D=0
@SP
A=M
M=D
(END_COMPARE2)
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL3
D,JLE
(EQUAL3)
D=-1
@SP
A=M
M=D
@END_COMPARE3
0,JMP
(NOT_EQUAL3)
D=0
@SP
A=M
M=D
(END_COMPARE3)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL4
D,JLE
(EQUAL4)
D=-1
@SP
A=M
M=D
@END_COMPARE4
0,JMP
(NOT_EQUAL4)
D=0
@SP
A=M
M=D
(END_COMPARE4)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL5
D,JLE
(EQUAL5)
D=-1
@SP
A=M
M=D
@END_COMPARE5
0,JMP
(NOT_EQUAL5)
D=0
@SP
A=M
M=D
(END_COMPARE5)
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL6
D,JGE
(EQUAL6)
D=-1
@SP
A=M
M=D
@END_COMPARE6
0,JMP
(NOT_EQUAL6)
D=0
@SP
A=M
M=D
(END_COMPARE6)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL7
D,JGE
(EQUAL7)
D=-1
@SP
A=M
M=D
@END_COMPARE7
0,JMP
(NOT_EQUAL7)
D=0
@SP
A=M
M=D
(END_COMPARE7)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@NOT_EQUAL8
D,JGE
(EQUAL8)
D=-1
@SP
A=M
M=D
@END_COMPARE8
0,JMP
(NOT_EQUAL8)
D=0
@SP
A=M
M=D
(END_COMPARE8)
@SP
M=M+1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D+M
@SP
M=M+1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=-M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D&M
@SP
M=M+1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D|M
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=!M
@SP
A=M
M=D
@SP
M=M+1
