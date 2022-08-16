// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

(LOOP)
    // Reduce R1 - 1
    @R1
    D=M
    D = D - 1
    @R1
    M = D
    
    // Check loop condition
    @STOP
    D; JLT

    // Multiplication
    @R0
    D = M
    @SUM
    M = M + D

    // Continue loop
    @LOOP
    0; JMP

(STOP)
    @SUM
    D = M
    @R2
    M = D

    // Reset values
    //@R0
    //M = 0
    //@R1
    //M = 0
    @SUM
    M = 0

(END)
    @END
    0; JMP