10 REM UTKA (DUCK) - old Basic game for LINTER 
20 REM written by Yuri STarikov and 
30 REM students of Moscow school #167 
40 REM First release: 1987 
50 SCREEN 0 
60 CLS 
120 RANDOMIZE 
130 SHUTY = 0 
140 LOCATE 40 , 24 
150 PRINT "I" 
160 Y = INT ( RND ( 23 ) * 22 + 1 ) 
170 X = 75 
180 SPEED = RND ( 1 ) * 0.5 
190 LOCATE X , Y 
200 PRINT "DUCK " 
210 IF SHUTY <> 0 then LOCATE 40 , SHUTY  : PRINT "^"
212 if SHUTY <> Y then goto 220
214 if X < 36 OR X > 40 then goto 220
216 GOSUB 400 
218 goto 60
220 INP$ = INKEY$ 
230 IF INP$ = "x" OR INP$ = "X" THEN GOTO 350 
240 IF INP$ = "i" OR INP$ = "I" THEN GOTO 320 
250 PAUSE ( SPEED ) 
260 X = X - 1 
270 IF SHUTY > 1 THEN SHUTY = SHUTY - 1 
280 IF X >= 1 THEN GOTO 190 
290 REM LOCATE X , Y 
300 REM PRINT "      " 
310 GOTO 60 
320 X = X - 1 
330 IF SHUTY = 0 THEN SHUTY = 23 : GOTO 190 
340 SHUTY = SHUTY - 1 : GOTO 190 
350 LOCATE X , Y : PRINT "      " 
360 LOCATE 40 , 24 
370 PRINT "It's too cold! Go home       " 
380 GOTO 500
400 LOCATE X , Y : print "Kr-y-a"
405 KrX = X
410 for i = Y+1 TO 24
420 inc = int(rnd(1)*4)
425 KrX = KrX - inc
430 locate KrX, i : print "Kr-y-a"
440 PAUSE ( SPEED ) *2
450 next I
460 return 
500 REM End
