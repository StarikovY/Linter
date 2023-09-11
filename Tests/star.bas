10 REM INKEY$ test - starship control 
20 REM prog shows how to check pressing regular keys 
30 REM and how to recognize and handle special keys 
40 X = 39 
50 Y = 13 
60 PREVX = X : PREVY = Y 
70 SCREEN 0 
75 COLOR 7, 0
80 CLS 
90 LOCATE PREVX , PREVY : PRINT " " 
100 LOCATE X , Y : PRINT "W" 
110 PREVX = X : PREVY = Y 
120 A$ = INKEY$ : IF A$ = "" THEN GOTO 120 
130 IF A$ = "q" THEN GOTO 190 
140 IF A$ = CHR$ ( 0 ) + "H" THEN Y = Y - 1 : IF Y <= 1 THEN Y = 1 : REM  "This is the up arrow key!" 
150 IF A$ = CHR$ ( 0 ) + "P" THEN Y = Y + 1 : IF Y > 24 THEN Y = 24 : REM This is the down arrow key! 
160 IF A$ = CHR$ ( 0 ) + "K" THEN X = X - 1 : IF X <= 1 THEN X = 1 : REM This is the left arrow key! 
170 IF A$ = CHR$ ( 0 ) + "M" THEN X = X + 1 : IF X > 80 THEN X = 80 : REM This is the right arrow key! 
180 GOTO 90 
190 print " " : PRINT "Finish!" 
