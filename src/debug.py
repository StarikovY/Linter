# Debug Basic file
import os
# from program import Program

class Debug:

    def __init__(self):
        self.__stmt = ''   # Statement string being processed
    
    def execdbg(self, prog, stmt2, tokenlist2):
#
# Available debug instructions:
#
# PRINT Args - Print variable
# BPON LINE_NUMBER - set breakpoint
# BPOFF LINE_ NUMBER - disable breakpoint
# BPLIST - list of break points
# GOTO LINE_NUMBER - set next line 
# 
#         
        self.__stmt = stmt2
        self.__tokenlist  =  tokenlist2
        self.__Program = prog ()

        if len(tokenlist2) == 0:
            return
        
        if len(tokenlist2) != 2:
            print('Wrong debug derective!', end='')
            return
        # find last line number of program
        line_numbers = self.__Program.line_numbers()
        prglen = len(line_numbers)
        lastline = line_numbers[prglen-1] + 1
    
        if self.__tokenlist[0].category == 3:  # print
            self.__Program.__parser.parse(tokenlist2, lastline)

