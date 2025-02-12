10 REM Old game asteroid 
20 REM First draw Stakan 
30 SCREEN 0 
40 CLS 
50 RANDOMIZE 
60 X = 20 : Y = 3 
70 LOCATE X , Y 
80 PRINT "!" 
90 FOR I = 0 TO 32 STEP 1 
100 PRINT "~" ; 
110 NEXT I 
120 PRINT "!" 
130 FOR I = 1 TO 18 STEP 1 
140 LOCATE X , Y + I 
150 PRINT "|                                 |" 
160 NEXT I 
170 REM DRAW wall PRINT " " 
180 WALL = INT ( RND ( 1 ) * 7 ) 
190 IF WALL < 2 THEN 180 
200 CLR = INT ( RND ( 1 ) * 7 ) 
210 IF CLR < 1 THEN CLR = 7 
220 FOR I = 1 TO 31 STEP 3 
230 LOCATE X + I , Y + WALL 
240 COLOR CLR , CLR 
250 PRINT "   " 
260 CLR = INT ( RND ( 1 ) * 7 ) 
270 IF CLR < 1 THEN CLR = 7 
280 NEXT I 
290 X = X + 16 : Y = 17 
300 PREVX = X : PREVY = Y 
310 REM Draw platform XXXXX 
320 COLOR 7 , 0 
330 LOCATE PREVX , PREVY : PRINT "       " 
340 LOCATE X , Y : PRINT "XXXXX" 
350 PREVX = X : PREVY = Y 
360 A$ = INKEY$ : IF A$ = "" THEN GOTO 360 
370 IF A$ = "x" OR A$ = "X" THEN GOTO 430 
380 REM IF A$ = CHR$ ( 0 ) + "H" THEN Y = Y - 1 : IF Y <= 1 THEN Y = 1 : REM  This is the up arrow key! 
390 REM IF A$ = CHR$ ( 0 ) + "P" THEN Y = Y + 1 : IF Y > 24 THEN Y = 24 : REM This is the down arrow key! 
400 IF A$ = CHR$ ( 0 ) + "K" THEN X = X - 1 : IF X <= 1 THEN X = 1 : REM This is the left arrow key! 
410 IF A$ = CHR$ ( 0 ) + "M" THEN X = X + 1 : IF X > 80 THEN X = 80 : REM This is the right arrow key! 
420 GOTO 330 
430 LOCATE 1 , 24 
440 COLOR 7 , 0 
450 PRINT "Done!" 
460 END 
