10 REM Print ASCII table 
20 FOR I = 0 TO 255 STEP 16 
30 FOR J = 0 TO 15 
33 IF ( I + J ) = 12 THEN GOTO 50 
40 PRINT " " + CHR$ ( J + I ) ; 
50 NEXT J 
60 PRINT " " 
70 NEXT I 
80 END 
