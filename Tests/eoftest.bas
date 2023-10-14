1 REM Windows 11 Python 3.11 verified 
5  REM EOF Test
10 OPEN "D:\test\sign.log" FOR INPUT AS # 1
20 IF EOF ( 1 ) THEN goto 300
30 INPUT #1, A$
40 PRINT A$
45 PRINT "NEXT Section"
50 GOTO 20  
300 CLOSE #1
310 PRINT "Finish"