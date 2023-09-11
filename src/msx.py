# YST extension for some GW and MSX BASICs
import os
if os.name == 'nt':  # sys.platform == 'win32': 
    import msvcrt
else:
    from readchar import readchar
    from select import select
    from sys import stdin, stdout

def inkey_impl():
    key = ''
    if os.name == 'nt':  # sys.platform == 'win32':
        if msvcrt.kbhit():
            arr = msvcrt.getch()
            if arr[0] == 0xe0:
                arr = msvcrt.getch()
                key = chr(0) + chr(arr[0])
            else:
                key = chr(arr[0])
            # key = chr(arr[0])
    else:
        # Linux/Mac only!
        if select([stdin,],[],[],0.05)[0]:
            key = readchar()
            
    return key

def cls_terminal():
    ''' Reset the terminal/console screen. (Also aliased to cls.)

        Greater than a fullscreen terminal clear, also clears the scrollback
        buffer.  May expose bugs in dumb terminals.
    '''
    if os.name == 'nt':
        from subprocess import call
        call('cls', shell=True)
    else:
        text = sc.reset
        if _ansi_capable:
            print(text, end='', flush=True)
        return text  # for testing

def location (y, x) :
    curstr = '\x1b[' +str(y+1) + ';' + str(x+1) + 'H'
    print(curstr, end='') 
