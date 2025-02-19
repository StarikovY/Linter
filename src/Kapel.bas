10 REM PROGRAM капли 
20 SCREEN 0 : CLS : REM "Количество букв-капель которые мы пока не поймали" 
30 PRINT "Включи русскую раскладку. Будут падать буквы вводи их." 
40 PRINT "Если готов нажми клавишу" 
50 REM Пустой цикл ожидания нажатия любой клавиши 
60 A$ = INKEY$ : IF A$ = "" THEN GOTO 60 
70 REM Цикл общего количества букв, которые нужно будет поймать, нажав клавишу. 
75 N = 10 
80 FOR K = 1 TO 10 
90 CLS : RANDOMIZE : REM Очистка и настройка генератора случайных чисел. 
100 REM RUS: 
110 REM Получение случайного числа, которое будет преобразовано в букву. 
120 A = INT ( 128 * RND ( 1 ) ) 
130 REM Если буква вне диапазона русских заглавных то загадать число еще раз. 
140 IF CHR$ ( A ) > "Z" OR CHR$ ( A ) < "A" THEN GOTO 100 
150 REM Получение символа из числа 
160 C$ = CHR$ ( A ) 
170 REM Выбор вертикали по которой будет падать буква 
180 V = INT ( RND ( 1 ) * 75 ) 
190 REM Цикл падения буквы 
200 FOR I = 1 TO 24 
210 REM поместить ее на верхнюю строчку для I=1 а потом все ниже и ниже 
220 LOCATE V , I : PRINT C$ 
230 FOR J = 1 TO 15000 : REM Цикл отлова нажатой клавиши. 
240 REM ФАКТИЧЕСКИ НАСТРОЙКА СКОРОСТИ ПАДЕНИЯ БУКВЫ 
250 Q$ = INKEY$ : REM Поместить в переменную Q символ нажатой клавиши 
260 REM Если введенный символ совпал, очистить экран 
270 REM Уменьшить кол-во пропущенных букв. Перейти к получению следующей буквы. 
280 IF UPPER$ ( Q$ ) = C$ THEN CLS : N = N - 1 : GOTO 360 
290 REM Цикл отлова вводимых с клавиатуры букв. 
300 NEXT J 
310 REM Стереть букву на этой строке для подготовки ее рисования на следующей. 
320 REM LOCATE V, I: PRINT " " 
330 REM Цикл перемещения буквы вниз 
340 NEXT I 
350 REM Метка, куда переходит программа в случае если буква введена правильно. 
360 REM SLED: 
370 REM Цикл выбора следующей буквы, а всего их 10. 
380 NEXT K 
390 REM Показать сколько капель пропущено. 
400 LOCATE 1 , 24 
405 PRINT "Done! " 
410 PRINT "Пропущено капель: " ; : PRINT N 
420 PRINT "One More (Y/N)? " ; : PRINT 
430 A$ = INKEY$ : IF A$ = "" THEN GOTO 430 
440 IF UPPER$ ( A$ ) = "Y" THEN 70 
450 IF UPPER$ ( A$ ) <> "N" THEN 430 
