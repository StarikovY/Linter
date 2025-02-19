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

"""This class implements a BASIC interpreter that
presents a prompt to the user. The user may input
program statements, list them and run the program.
The program may also be saved to disk and loaded
again.

"""

from basictoken import BASICToken as Token
from lexer import Lexer
from program import Program
from sys import stderr
import sys
import os
import msx
import datetime

def main():

    banner = (
        """
        *
        *       °
        *           ***   *     **    *  * 
        *       *  *  *  ***   ****   **  *
        *       *  *  *   *    *      *
        ******  *  *  *   * *  ****   *
        The interpreter of BASIC Programming language
                     Yuri Starikov - 1986-2025. 
            This version based on sources of PYBasic
                    Version 1.5.0.72
        """)
    # tz = datetime.timezone.utc
    # ft = "%Y-%m-%dT%H:%M:%S%z"
    # t = datetime.datetime.now(tz=tz).strftime(ft)
    argc = len(sys.argv)
    if argc > 2:
        print("Usage: python3 " + sys.argv[0] + " [basic_program]")
        return
    elif argc == 2:
        BasProg = sys.argv[1]
    else:
        BasProg = ''
        
    # cmd = 'mode con: cols=80 lines=25'
    # os.system(cmd) 
    
    # print('\x1b[' + str(40) + 'm', end='')
    # print('\x1b[' + str(32) + 'm', end='')
    # msx.cls_terminal()   

    
    print(banner)
    # print(f"           Version: 1.5.{t}")

    lexer = Lexer()
    program = Program()

    # Run program from argument
    if argc > 1:
        program.load(BasProg)
        try:
            program.execute()

        except KeyboardInterrupt:
            print("Program terminated")
        
        return 
        
    # Continuously accept user input and act on it untilloa
    # the user enters 'EXIT'
    while True:

        stmt = input('> ')

        try:
            tokenlist = lexer.tokenize(stmt)

            # Execute commands directly, otherwise
            # add program statements to the stored
            # BASIC program

            if len(tokenlist) > 0:

                # Exit the interpreter
                if tokenlist[0].category == Token.EXIT:
                    break

                # Add a new program statement, beginning
                # a line number
                elif tokenlist[0].category == Token.UNSIGNEDINT\
                     and len(tokenlist) > 1:
                    program.add_stmt(tokenlist)

                # Delete a statement from the program
                elif tokenlist[0].category == Token.UNSIGNEDINT \
                        and len(tokenlist) == 1:
                    program.delete_statement(int(tokenlist[0].lexeme))

                # Execute the program
                elif tokenlist[0].category == Token.RUN:
                    try:
                        program.execute()

                    except KeyboardInterrupt:
                        print("Program terminated")

                # List the program
                elif tokenlist[0].category == Token.LIST or tokenlist[0].category == Token.LISTNH:
                     if len(tokenlist) == 2:
                         program.list(int(tokenlist[1].lexeme),int(tokenlist[1].lexeme))
                     elif len(tokenlist) == 3:
                         # if we have 3 tokens, it might be LIST x y for a range
                         # or LIST -y or list x- for a start to y, or x to end
                         if tokenlist[1].lexeme == "-":
                             program.list(None, int(tokenlist[2].lexeme))
                         elif tokenlist[2].lexeme == "-":
                             program.list(int(tokenlist[1].lexeme), None)
                         else:
                             program.list(int(tokenlist[1].lexeme),int(tokenlist[2].lexeme))
                     elif len(tokenlist) == 4:
                         # if we have 4, assume LIST x-y or some other
                         # delimiter for a range
                         program.list(int(tokenlist[1].lexeme),int(tokenlist[3].lexeme))
                     else:
                         program.list()
                
                # List the program
                elif tokenlist[0].category == Token.RENUM:
                     if len(tokenlist) == 6:
                         program.renum(int(tokenlist[3].lexeme),int(tokenlist[3].lexeme),int(tokenlist[5].lexeme))
                     elif len(tokenlist) == 4:
                        program.renum(int(tokenlist[1].lexeme),int(tokenlist[3].lexeme))
                     elif len(tokenlist) == 2:
                         program.renum(int(tokenlist[1].lexeme))
                     else:
                         program.renum()
                
                # TRON/TROFF
                
                elif tokenlist[0].category == Token.TRON:
                    program.tron()
                    
                elif tokenlist[0].category == Token.TROFF:
                    program.troff()
                    
                elif tokenlist[0].category == Token.DEC:
                    program.dec()
  
                elif tokenlist[0].category == Token.MSX:
                    program.msx()                    
      
                # Save the program to disk
                elif tokenlist[0].category == Token.SAVE:
                    program.save(tokenlist[1].lexeme)
                    print("Program written to file")

                # Load the program from disk
                elif tokenlist[0].category == Token.LOAD:
                    program.load(tokenlist[1].lexeme)
                    print("Program read from file")

                # List of files on the disk
                elif tokenlist[0].category == Token.DIR:
                    if len(tokenlist) == 1:
                        path = "."
                    else:
                        path = tokenlist[1].lexeme
                    program.filelist(path)
                
                # SET Breakpoint
                elif tokenlist[0].category == Token.BPON:
                    program.bpon(tokenlist[1].lexeme)

                # Delete Breakpoint
                elif tokenlist[0].category == Token.BPOFF:
                    program.bpoff(tokenlist[1].lexeme)

                # List of Breakpoints
                elif tokenlist[0].category == Token.BPLIST:
                    program.bplist()

                # remove all Breakpoints
                elif tokenlist[0].category == Token.BPCLEAR:
                    program.bpclear()

                # Delete the program from memory
                elif tokenlist[0].category == Token.NEW:
                    program.delete()
                
                #re-enumerate 

                # Unrecognised input
                else:
                    print("Unrecognised input: ", file=stderr)
                    for token in tokenlist:
                        token.print_lexeme()
                    print(flush=True)

        # Trap all exceptions so that interpreter
        # keeps running
        except Exception as e:
            print(e, file=stderr, flush=True)

