10 REM Program Kapel 
20 CLS : N = 10 : REM Number of drops 
30 INPUT "Enter line of text (up to 10 chars)" ; LINETXT$ 
40 IF LEN ( LINETXT$ ) > 10 THEN GOTO 30 
50 REM Waiting for key 
60 LNGT = LEN ( LINETXT$ ) : STARTLOC = INT ( ( 80 - LNGT ) / 2 ) 
70 PRINT LNGT 
80 PRINT STARTLOC 
90 REM REM Main Loop 
100 DIM LETTER$ ( 10 ) 
110 DIM COLUMN ( 10 ) 
120 DIM LINES ( 10 ) 
130 REM ------------------------------------------------------------ 
140 FOR I = 1 TO LNGT 
150 LETTER$ ( I ) = LINETXT$ ( I ) 
160 NEXT I 
170 REM Loop 
180 CLS : RANDOMIZE 
190 SCREEN 0 : COLOR 2 , 0 
200 LOCATE STARTLOC , 0 : PRINT LINETXT$ 
210 FOR I = 1 TO 23 
220 FOR K = 1 TO LNGT 
230 REM Generate letter and column 
240 REM Generate rundom number and convert to letter 
250 IF K > 10 THEN GOTO 470 
260 REM IF K >= I THEN GOSUB 580 
270 REM Select letter for drop 
280 V = INT ( ROUND ( RND ( 1 ) * LNGT ) ) 
290 REM CLEAR Prev letter 
300 LOCATE STARTLOC + I , V : PRINT LETTER$ ( K ) 
310 SPEED = 5000 - ( 10 - N ) * 300 
320 FOR J = 1 TO SPEED : REM 
330 REM speed for drop of letter 
340 REM Q$ = UPPER$ ( INKEY$ ) 
350 REM Clear scren when input letter i the same as drop[ letter 
360 REM Decrease number of missed letters, next char 
370 REM IF Q$ = C$ THEN CLS : N = N - 1 : GOTO 430 
380 REM Loop for checking input char 
390 NEXT J 
400 REM Erase letter on line . 
410 LOCATE STARTLOC + I - 1 , V : REM PRINT " " 
420 REM Loop for moving letter to next line 
430 REM 
440 REM SLED: 
450 REM Loop for next letter. 
460 NEXT K 
470 NEXT I 
480 REM Show how many drops missed 
490 LOCATE 10 , 5 
500 PRINT "" 
510 PRINT "Missed letters: " ; N 
520 PRINT "Again? " 
530 REM Waiting 
540 Y$ = INKEY$ 
550 IF Y$ = "" THEN 450 
560 IF UPPER$ ( Y$ ) = "Y" THEN 20 
570 REM GOTO 20 
580 END 
590 A = INT ( 160 * RND ( 1 ) ) 
600 REM If letters are not capital latin letter try again 
610 IF A < 65 OR A > 90 THEN GOTO 230 
620 C$ = UPPER$ ( CHR$ ( A ) ) 
630 LETTER$ ( K ) = C$ 
640 REM Select column for drops 
650 V = INT ( RND ( 1 ) * 75 ) 
660 COLUMN ( K ) = V 
670 REM PRINT "C$ " ; C$ ; " A " ; A ; " V " ; V 
680 REM lOOP OF LETTER DROP 
690 REM Set to upper line for I=1 and down and down 
700 RETURN 
