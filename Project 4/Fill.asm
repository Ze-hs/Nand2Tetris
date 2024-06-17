// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.


// Get input from keyboard and switch colors
(INPUT)
    @SCREEN
    D=A
    @word //current pixel word/location
    M=D

    @KBD
    D=M
    
    @BLACK
    D;JGT
    @WHITE
    0;JMP

    @INPUT
    0;JMP


//Change screen color
(DRAW)
    //Set the color
    @color
    D=M

    @word
    A=M
    M=D
    
    //Advance to the next pixels
    @word
    M=M+1
    D=M

    //KBD - Current Sreen locationn
    @KBD
    D=A-D
    
    @R1
    M=D

    @DRAW
    D;JGT
    @INPUT
    0;JMP

(WHITE)
    @color
    M=0

    @DRAW
    0;JMP

(BLACK)
    @color
    M=-1

    @DRAW
    0;JMP