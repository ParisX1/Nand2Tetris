// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Set initial variables

// 1. Value for 16
@16
D = A
@sixteen
M = D

// 2. Screen position pointer
@SCREEN
D = A
@pointer
M = D

// 3. Position for end of @SCREEN array
@8191
D = A
@SCREEN
D = D + A
@endrow
M = D

// Infinite loop waiting for keyboard input
(INPUTLOOP)
    
    // Check if pointer at end of @SCREEN array
    @CHECKPOINTER
    0; JMP

    (KEYBOARDINPUT)
        // Check keyboard input
        @KBD
        D = M
        @BLACKSCREEN
        D; JNE
        @WHITESCREEN
        D; JEQ
        
        (MOVEPOINTER)
            @pointer
            M = M + 1
            
            @INPUTLOOP
            0; JMP
    

(BLACKSCREEN)
    @pointer
    A = M
    M = -1
    @MOVEPOINTER
    0; JMP

(WHITESCREEN)
    @pointer
    A = M
    M = 0
    @MOVEPOINTER
    0; JMP


(CHECKPOINTER)
    // Checks if pointer is at end of @SCREEN array
    // If at end, resets to @SCREEN location (beginning of array)
    @pointer
    D = M
    @endrow
    D = D - M
    
    // If not at end, go back to INPUTLOOP
    @KEYBOARDINPUT
    D; JLE 
    
    // If at end, resest pointer to @SCREEN
    @SCREEN
    D = A
    @pointer
    M = D

    @KEYBOARDINPUT
    0; JMP