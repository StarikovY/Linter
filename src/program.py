#! /usr/bin/python

# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Class representing a BASIC program.
This is a list of statements, ordered by
line number.

"""

from basictoken import BASICToken as Token
from basicparser import BASICParser
from flowsignal import FlowSignal
from lexer import Lexer
import os
# from debug import Debug

class BASICData:

    def __init__(self):
        # array of line numbers to represent data statements
        self.__datastmts = {}

        # Data pointer
        self.__next_data = 0


    def delete(self):
        self.__datastmts.clear()
        self.__next_data = 0

    def delData(self,line_number):
        if self.__datastmts.get(line_number) != None:
            del self.__datastmts[line_number]

    def addData(self,line_number,tokenlist):
        """
        Adds the supplied token list
        to the program's DATA store. If a token list with the
        same line number already exists, this is
        replaced.

        line_number: Basic program line number of DATA statement

        """

        try:
            self.__datastmts[line_number] = tokenlist

        except TypeError as err:
            raise TypeError("Invalid line number: " + str(err))


    def getTokens(self,line_number):
        """
        returns the tokens from the program DATA statement

        line_number: Basic program line number of DATA statement

        """

        return self.__datastmts.get(line_number)

    def readData(self,read_line_number):

        if len(self.__datastmts) == 0:
            raise RuntimeError('No DATA statements available to READ ' +
                               'in line ' + str(read_line_number))

        data_values = []

        line_numbers = list(self.__datastmts.keys())
        line_numbers.sort()

        if self.__next_data == 0:
            self.__next_data = line_numbers[0]
        elif line_numbers.index(self.__next_data) < len(line_numbers)-1:
            self.__next_data = line_numbers[line_numbers.index(self.__next_data)+1]
        else:
            raise RuntimeError('No DATA statements available to READ ' +
                               'in line ' + str(read_line_number))

        tokenlist = self.__datastmts[self.__next_data]

        sign = 1
        for token in tokenlist[1:]:
            if token.category != Token.COMMA:
                #data_values.append(token.lexeme)

                if token.category == Token.STRING:
                    data_values.append(token.lexeme)
                elif token.category == Token.UNSIGNEDINT:
                    data_values.append(sign*int(token.lexeme))
                elif token.category == Token.UNSIGNEDFLOAT:
                    data_values.append(sign*eval(token.lexeme))
                elif token.category == Token.MINUS:
                    sign = -1
                #else:
                    #data_values.append(token.lexeme)
            else:
                sign = 1


        return data_values

    def restore(self,restoreLineNo):
        if restoreLineNo == 0 or restoreLineNo in self.__datastmts:

            if restoreLineNo == 0:
                self.__next_data = restoreLineNo
            else:

                line_numbers = list(self.__datastmts.keys())
                line_numbers.sort()

                indexln = line_numbers.index(restoreLineNo)

                if indexln == 0:
                    self.__next_data = 0
                else:
                    self.__next_data = line_numbers[indexln-1]
        else:
            raise RuntimeError('Attempt to RESTORE but no DATA ' +
                               'statement at line ' + str(restoreLineNo))


class Program:

    def __init__(self):
        # Dictionary to represent program
        # statements, keyed by line number
        self.__program = {}

        # represent debug 
        # self.__debug = Debug()

        # Program counter
        self.__next_stmt = 0

        # Initialise return stack for subroutine returns
        self.__return_stack = []

        # return dictionary for loop returns
        self.__return_loop = {}

        # Setup DATA object
        self.__data = BASICData()
        
        self.__tron = False 
        self.bplines = []

    def __str__(self):

        program_text = ""
        line_numbers = self.line_numbers()

        for line_number in line_numbers:
            program_text += self.str_statement(line_number)

        return program_text

    def str_statement(self, line_number):
        line_text = str(line_number) + " "

        statement = self.__program[line_number]
        if statement[0].category == Token.DATA:
            statement = self.__data.getTokens(line_number)
        for token in statement:
            # Add in quotes for strings
            if token.category == Token.STRING:
                line_text += '"' + token.lexeme + '" '

            else:
                line_text += token.lexeme + " "
        line_text += "\n"
        return line_text

    def list(self, start_line=None, end_line=None):
        """Lists the program"""
        line_numbers = self.line_numbers()
        if not start_line:
            start_line = int(line_numbers[0])

        if not end_line:
            end_line = int(line_numbers[-1])

        for line_number in line_numbers:
            if int(line_number) >= start_line and int(line_number) <= end_line:
                print(self.str_statement(line_number), end="")

    def tron(self):
        self.__tron = True
        print("OK")
        
    def troff(self):
        self.__tron = False
        print("OK")

    def msx (self):
        self.__msx = True
        self.__dec = False
        print("OK")                           

    def dec (self):
        self.__dec = True
        self.__msx = False
        print("OK")                           
        
    def renum(self, new_line=None, current_line=None, increment=None):
        # re-enum program
        line_numbers = self.line_numbers()
        new_line_numbers = self.line_numbers()
        if not new_line:
            new_line = 10
            
        n_line = new_line    
        
        if not current_line:
            current_line = int(line_numbers[0])
            
        if not increment:
            increment = 10
        
        # # check that prev line numbers are less than new line
        # if current_line
        lexer = Lexer()
        PrNew = Program()
        
        for i in range(len(line_numbers)):
            if line_numbers[i] >= current_line:
                if i > 0:
                    if line_numbers[i-1] > n_line:
                        n_line = line_numbers[i-1] + increment
                
                new_line_numbers[i] = n_line
                n_line += increment
        
        for nl in range(len(line_numbers)):
            
        
            if line_numbers[nl] >= current_line:
                if nl > 0:
                    if line_numbers[nl-1] > new_line:
                        new_line = line_numbers[nl-1] + increment
                
                new_line_numbers[nl] = new_line
                
            sttm = self.str_statement(line_numbers[nl])
            oline = len(str(line_numbers[nl])) + 1 #space between number and statement
            line = str(new_line) + ' ' + sttm[oline:]
            line = line.replace("\r", "").replace("\n", "").strip()
            
            tokenlist = lexer.tokenize(line)
                
            PrNew.add_stmt(tokenlist)
            new_line += increment
            
        # self.delete()
        # self = PrNew
        nl = 0
        for nl in range(len(line_numbers)):
            self.delete_statement(line_numbers[nl])
           
        nl = 0 
        for nl in range(len(line_numbers)):
           sttm = PrNew.str_statement(new_line_numbers[nl])
           sttm = sttm.replace("\r", "").replace("\n", "").strip()
           tokenlist = lexer.tokenize(sttm)
           # tokenlist containes list of tokens from line every token has category, tokenlist[i].category == Token.GOTO, THEN GOSUB 
           # next token will be OLD line number, which need to be extracted and replaced by new line number
           tokenlistsize = len(tokenlist)
           for n in range(tokenlistsize):
                tok = tokenlist[n]
                if tok.category == Token.GOTO or tok.category == Token.GOSUB: # or tok.category == Token.THEN:
                    if n + 1 < tokenlistsize:
                        lg = int (tokenlist[n+1].lexeme)
                        ind = line_numbers.index(lg)
                        tokenlist[n+1].lexeme = str(new_line_numbers[ind])
                                                 
           self.add_stmt(tokenlist)
        
        print("Renum is done!")                                      
                          
        
    def save(self, file):
        """Save the program

        :param file: The name and path of the save file, .bas is
                     appended

        """
        if not file.lower().endswith(".bas"):
            file += ".bas"
        try:
            with open(file, "w", encoding='utf-8') as outfile:
                outfile.write(str(self))
        except OSError:
            raise OSError("Could not save to file")

    def bpon(self, line):
        self.bplines.append(int(line))

    def bpoff(self, line):
        self.bplines.remove(int(line))

    def bplist(self):
        for item in self.bplines:
            print(item, ' ', end='')
        print(" ")      

    def bpclear(self):
        self.bplines.clear()

    def filelist(self, path):
        # list of files
        listfiles = os.listdir(path)
        # print("listdir is OK")
        
        print(listfiles)      
        
    def load(self, file):
        """Load the program

        :param file: The name and path of the file to be loaded, .bas is
                     appended

        """

        # New out the program
        self.delete()
        if not file.lower().endswith(".bas"):
            file += ".bas"
        try:
            lexer = Lexer()
            with open(file, "r", encoding='utf-8') as infile:
                for line in infile:
                    line = line.replace("\r", "").replace("\n", "").strip()
                    tokenlist = lexer.tokenize(line)
                    self.add_stmt(tokenlist)

        except OSError:
            raise OSError("Could not read file")

    def add_stmt(self, tokenlist):
        """
        Adds the supplied token list
        to the program. The first token should
        be the line number. If a token list with the
        same line number already exists, this is
        replaced.

        :param tokenlist: List of BTokens representing a
        numbered program statement

        """
        if len(tokenlist) > 0:
            try:
                line_number = int(tokenlist[0].lexeme)
                if tokenlist[1].lexeme == "DATA":
                    self.__data.addData(line_number,tokenlist[1:])
                    self.__program[line_number] = [tokenlist[1],]
                else:
                    self.__program[line_number] = tokenlist[1:]

            except TypeError as err:
                raise TypeError("Invalid line number: " +
                                str(err))

    def line_numbers(self):
        """Returns a list of all the
        line numbers for the program,
        sorted

        :return: A sorted list of
        program line numbers
        """
        line_numbers = list(self.__program.keys())
        line_numbers.sort()

        return line_numbers

    def __execute(self, line_number):
        """Execute the statement with the
        specified line number

        :param line_number: The line number

        :return: The FlowSignal to indicate to the program
        how to branch if necessary, None otherwise

        """
        if line_number not in self.__program.keys():
            raise RuntimeError("Line number " + line_number +
                               " does not exist")

        statement = self.__program[line_number]

        try:
            return self.__parser.parse(statement, line_number)

        except RuntimeError as err:
            raise RuntimeError(str(err))

    def execdbg(self, stmt2, tokenlist2):
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
        # self.__stmt = stmt2
        # self.__tokenlist  =  tokenlist2
        # self.__Program = prog ()

        if len(tokenlist2) == 0:
            return
        
        # if len(tokenlist2) != 2:
        #    print('Wrong debug derective!', end='')
        #    return
        
        # find last line number of program
        line_numbers = self.line_numbers()
        prglen = len(line_numbers)
        lastline = line_numbers[prglen-1] + 1
    
        if tokenlist2[0].category == 105:  # BPON
            self.bplines.append(int(tokenlist2[1].lexeme))
        elif tokenlist2[0].category == 106:  # BPOFF
            self.bplines.remove(int(tokenlist2[1].lexeme))
        elif tokenlist2[0].category == 107:  # BPLIST
            for item in self.bplines:
                print(item, ' ', end='')
            print(" ")    
        elif tokenlist2[0].category == 108:  # BPCLEAR
            self.bplines.clear()  
        elif tokenlist2[0].category == 96:  # TRON
            self.__tron = True
        elif tokenlist2[0].category == 97:  # TROFF
            self.__tron = False
        else:
            self.__parser.parse(tokenlist2, lastline)

        return

    def execute(self):
        """Execute the program"""

        self.__parser = BASICParser(self.__data)
        self.__data.restore(0) # reset data pointer
        lexer = Lexer()
        line_numbers = self.line_numbers()

        if len(line_numbers) > 0:
            # Set up an index into the ordered list
            # of line numbers that can be used for
            # sequential statement execution. The index
            # will be incremented by one, unless modified by
            # a jump
            index = 0
            self.set_next_line_number(line_numbers[index])

            # Run through the program until the
            # has line number has been reached
            while True:
                ln = self.get_next_line_number()
                if self.__tron or ln in self.bplines:
                    self.__tron = True
                    lngt = 1
                    sttm = self.str_statement(line_numbers[index])
                    print(sttm, end='')

                    while lngt > 0:
                        if self.__tron == False:
                            break

                        stmt2 = input('$ ')

                        # try:
                        tokenlist2 = lexer.tokenize(stmt2)
                        lngt = len(tokenlist2)
                        if lngt > 0:
                            # self.__debug.execdbg(prog, stmt2, tokenlist2)
                            self.execdbg(stmt2, tokenlist2)
                            # self.__parser.parse(tokenlist2, 999)
                    
                flowsignal = self.__execute(self.get_next_line_number())
                self.__parser.last_flowsignal = flowsignal

                if flowsignal:
                    if flowsignal.ftype == FlowSignal.SIMPLE_JUMP:
                        # GOTO or conditional branch encountered
                        try:
                            index = line_numbers.index(flowsignal.ftarget)

                        except ValueError:
                            raise RuntimeError("Invalid line number supplied in GOTO or conditional branch: "
                                               + str(flowsignal.ftarget))

                        self.set_next_line_number(flowsignal.ftarget)

                    elif flowsignal.ftype == FlowSignal.GOSUB:
                        # Subroutine call encountered
                        # Add line number of next instruction to
                        # the return stack
                        if index + 1 < len(line_numbers):
                            self.__return_stack.append(line_numbers[index + 1])

                        else:
                            raise RuntimeError("GOSUB at end of program, nowhere to return")

                        # Set the index to be the subroutine start line
                        # number
                        try:
                            index = line_numbers.index(flowsignal.ftarget)

                        except ValueError:
                            raise RuntimeError("Invalid line number supplied in subroutine call: "
                                               + str(flowsignal.ftarget))

                        self.set_next_line_number(flowsignal.ftarget)

                    elif flowsignal.ftype == FlowSignal.RETURN:
                        # Subroutine return encountered
                        # Pop return address from the stack
                        try:
                            index = line_numbers.index(self.__return_stack.pop())

                        except ValueError:
                            raise RuntimeError("Invalid subroutine return in line " +
                                               str(self.get_next_line_number()))

                        except IndexError:
                            raise RuntimeError("RETURN encountered without corresponding " +
                                               "subroutine call in line " + str(self.get_next_line_number()))

                        self.set_next_line_number(line_numbers[index])

                    elif flowsignal.ftype == FlowSignal.STOP:
                        break

                    elif flowsignal.ftype == FlowSignal.LOOP_BEGIN:
                        # Loop start encountered
                        # Put loop line number on the stack so
                        # that it can be returned to when the loop
                        # repeats
                        self.__return_loop[flowsignal.floop_var] = line_numbers[index]

                        # Continue to the next statement in the loop
                        index = index + 1

                        if index < len(line_numbers):
                            self.set_next_line_number(line_numbers[index])

                        else:
                            # Reached end of program
                            raise RuntimeError("Program terminated within a loop")

                    elif flowsignal.ftype == FlowSignal.LOOP_SKIP:
                        # Loop variable has reached end value, so ignore
                        # all statements within loop and move past the corresponding
                        # NEXT statement
                        index = index + 1
                        while index < len(line_numbers):
                            next_line_number = line_numbers[index]
                            temp_tokenlist = self.__program[next_line_number]

                            if temp_tokenlist[0].category == Token.NEXT and \
                               len(temp_tokenlist) > 1:
                                # Check the loop variable to ensure we have not found
                                # the NEXT statement for a nested loop
                                if temp_tokenlist[1].lexeme == flowsignal.ftarget:
                                    # Move the statement after this NEXT, if there
                                    # is one
                                    index = index + 1
                                    if index < len(line_numbers):
                                        next_line_number = line_numbers[index]  # Statement after the NEXT
                                        self.set_next_line_number(next_line_number)
                                        break

                            index = index + 1

                        # Check we have not reached end of program
                        if index >= len(line_numbers):
                            # Terminate the program
                            break

                    elif flowsignal.ftype == FlowSignal.LOOP_REPEAT:
                        # Loop repeat encountered
                        # Pop the loop start address from the stack
                        try:
                            index = line_numbers.index(self.__return_loop.pop(flowsignal.floop_var))

                        except ValueError:
                            raise RuntimeError("Invalid loop exit in line " +
                                               str(self.get_next_line_number()))

                        except KeyError:
                            raise RuntimeError("NEXT encountered without corresponding " +
                                               "FOR loop in line " + str(self.get_next_line_number()))

                        self.set_next_line_number(line_numbers[index])

                else:
                    index = index + 1

                    if index < len(line_numbers):
                        self.set_next_line_number(line_numbers[index])

                    else:
                        # Reached end of program
                        break

        else:
            raise RuntimeError("No statements to execute")

    def delete(self):
        """Deletes the program by emptying the dictionary"""
        self.__program.clear()
        # self.__debug.clear()
        self.__data.delete()

    def delete_statement(self, line_number):
        """Deletes a statement from the program with
        the specified line number, if it exists

        :param line_number: The line number to be deleted

        """
        self.__data.delData(line_number)
        try:
            del self.__program[line_number]

        except KeyError:
            raise KeyError("Line number does not exist")

    def get_next_line_number(self):
        """Returns the line number of the next statement
        to be executed

        :return: The line number

        """

        return self.__next_stmt

    def set_next_line_number(self, line_number):
        """Sets the line number of the next
        statement to be executed

        :param line_number: The new line number

        """
        self.__next_stmt = line_number
