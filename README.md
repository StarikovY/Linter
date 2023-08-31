Чем бы дитя не тешилось лишь бы выпить не просило! (English: Whichever fun 
a baby has lest it drinks (or as long as he didn't ask for a drink))

Linter is interpreter for variation of BASIC programming language. It was 
developed by Yuri Starikov in 1987-1988 for Soviet analog of 
UNIX BSD 2.9 – Demos. 
It was part of Yuri’s PhD dissertation. First version was written, using 
LEX/YACC and C. It was widely used in Moscow’s school #167 and users of Demos 
operation system. Yuri also ported this interpreter to Soviet analog of VAX, 
Soviet analog of IBM 360 with Unix OS, Venix/Xenix operation systems for PC 
compatible computers, and IBM RT PC with AIX. It was actively used on 
IBM RT PC for scientific calculations.

After moving to United States and personal computers lost 5½ inches floppy, 
original sources were lost. After retirement Yuri found PyBasic project 
in Github. Using this project as initial, Yuri restored Linter project on 
new basis. Now Linter is written on Python and expect to work on any 
Windows/Linux and Mac OS machine.

Original Linter language was based on BASIC for PDP-11 RT-11 operation system 
(Soviet Analog is ОС РАФОС) with some extensions from GW-BASIC and MSX-BASIC. 
It worked only on text terminals 80x24, but supported screen operations.

1. Running project.

You can run directly 

    linter.exe 

file which is packacge create by PyInstaller. If you unpack it then you should start

    Python(3) linter.py

Linter was tested only with Python 3.10 or later version of Python.
You can add program name as command line parameter:

    linter utka.bas

or

    Python3 linter.py Utka.bas

I recommend to create Linter.CMD (or linter.sh for Unix systems) with the following line:

python YOUR_FULL_PATH_TO_LINTER\linter.py %1

Put this file to folder with executables and you can start your basic app from any placed.

2. Extensions to PyBasic

LINTER added some extensions from GW-BASIC and MSX-Basic. This list of extensions is updating every week.

1). Command line parameter for running BASIC program - see above
2). Command RENUM - allow to re-enumerate lines in BASIC Program
3). SCREEN - SCREEN keyword - set direct positioning of cursor for compatible terminals with ANSIterminal
    only one mode supported yet: SCREEN 0 - which creates terminal with 80x25 size: X coordinate is column number (1-80)
    Y coordinate is line number (1-24)
4). CLS- CLS KEYWORD (STATEMENT) - clear screen. Many dialects of BASIC have different formats. For compatibility
    LINTER supports CLS and CLS() formats.
5). LOCATE - LOCATE keyword - poistion cursior. Example: 20 LOCATE 50,24
6). COLOR -COLOR keyword. Example: 20 COLOR Foreground, Background, where parameters can be following values:
    0 = black
    1 = blue
    2 = green
    3 = cyan
    4 = red
    5 = magenta
    6 = yellow
    7 = white
7). INKEY$ - INKEY$ keyword - allow to press keys and check results without pressin ENTER key. Special keys (like arrow keys)
    return 2 characters: CHR$(0) and character. See GW-BASIC documentation and STAR.BAS example for details
8). BEEP - BEEP keyword (Statement). Produce "default" operation system sound for "beep". This may surprise you, as your 
    OS settings produces "beep"
9). TRON/TROFF - TRON/TROFF commands - trace the execution of program statements. TRON displays BASIC line before execution.
    TROFF - disable this output
10). PAUSE - PAUSE keyword - pause execution of program in seconds (float value). Example: 30 SLEEP(0.3) 
11). EOF - EOF (end offile) function

This list is modified every days and extended by members of project.

3. Test and example files

Folder test containes the following files

bagels.bas - simple game from PyBasic examples
BAS1.bas - simple test for testing c
Beer.bas - sample of loop with 90 bottles of beer (you can increase/decrease your dose)
ColorScreen1.bas - using SCREEN, LOCATE and COLOR 
eliza.bas - "Siri" on BASIC
eoftest.bas - EOF() function test
factorial.bas - simple program for calculation of factorial
regression.bas - PyBASIC regression test
star.bas - INKEY$ sample, shows how to handle arrows keys
utka.bas - old UTKA (Duck) game

You cam modify these programms and add new games and other interesting programs.









