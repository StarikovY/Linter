10 CLS 
20 RANDOMIZE : SCREEN 0 
30 LOCATE 20 , 10 : PRINT "Guess where the ball is?" 
40 A = 99 * RND ( 1 ) 
50 IF A <= 33 THEN B = 1 ELSE IF A > 66 THEN B = 3 ELSE B = 2 
60 LOCATE 20 , 11 : PRINT " _   _   _" 
70 LOCATE 20 , 12 : PRINT "/ \ / \ / \" 
80 LOCATE 20 , 13 : PRINT " 1   2   3" 
90 PRINT 
100 INPUT "Enter the cup number: " ; C 
110 IF C = B THEN PRINT "YOU GUESSED IT! WELL DONE!" ELSE PRINT "WRONG GUESS! BAD LUCK!" 
120 LOCATE 20 , 11 : PRINT "          " 
130 LOCATE 20 , 12 : PRINT "\_/ \_/ \_/ " 
140 REM print B 
150 LOCATE 20 + 4 * ( B - 1 ) + 1 , 12 : PRINT "O" 
160 LOCATE 1 , 16 : PRINT "Again (0 - No, 1-Yes)? " : INPUT X 
170 IF X > 0 THEN 10 
180 END 
