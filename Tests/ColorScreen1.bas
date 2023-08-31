10 REM Screen routines test
20 rem set text screen mode
60 SCREEN 0 
160 CLS
170 for I = 0 TO 7
180 for J = 0 to 7
185 LOCATE J+10, I+10
190 COLOR J, I
200 REm LOCATE J+10, I+10
210 PRINT "X"
220 NEXT J
230 NEXT I
233 rem pause
235 rem LOCATE 1, 24
240 COLOR 7, 0

