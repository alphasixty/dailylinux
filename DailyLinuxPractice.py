##################################################
## DailyLinuxPractice
##################################################
## 1.0
##################################################
## Author: alphasixty
## Copyright: None
## Credits: yawpitch
## License: Open Source
## Maintainer: alphasixty
##################################################

print("""\

######     #    ### #       #     #    #       ### #     # #     # #     # 
#     #   # #    #  #        #   #     #        #  ##    # #     #  #   #  
#     #  #   #   #  #         # #      #        #  # #   # #     #   # #   
#     # #     #  #  #          #       #        #  #  #  # #     #    #    
#     # #######  #  #          #       #        #  #   # # #     #   # #   
#     # #     #  #  #          #       #        #  #    ## #     #  #   #  
######  #     # ### #######    #       ####### ### #     #  #####  #     #
                                          _|      _|                      
_|_|_|    _|  _|_|    _|_|_|    _|_|_|  _|_|_|_|        _|_|_|    _|_|    
_|    _|  _|_|      _|    _|  _|          _|      _|  _|        _|_|_|_|  
_|    _|  _|        _|    _|  _|          _|      _|  _|        _|        
_|_|_|    _|          _|_|_|    _|_|_|      _|_|  _|    _|_|_|    _|_|_|  
_|                                                                        
_| 

###########################################################################
Just type in the command to match the description. This is like electronic
flash cards to keep your mind sharp
###########################################################################

""")

import sys
from random import choice

COMMANDS = {
    #List of OS commands to choose at random.
    'cat':
    'concatenate files and print on the standard output',
    'cron':
    'daemon  to  execute  scheduled  commands',
    'df':
    'report file system disk space usage',
    'grep':
    'print lines matching a pattern',
    'ls':
    'list directory contents',
    'lsblk':
    'list block devices',
    'mkdir':
    'make directories',
    'mv':
    'move (rename) files',
    'netstat':
    'Print  network  connections,  routing tables, interface '
    'statistics, masquerade  connections, and multicast '
    'memberships',
    'nohup':
    'run  a  command immune to hangups, with output to a non-tty',
    'nslookup':
    'query Internet name servers interactively',
    'rm':
    'remove files or directories',
    'traceroute':
    'print  the  route packets trace to network host',
    'whoami':
    'print effective userid'
}
#end of commands.

#inits the var for the number of potential wrong answers
wrong_answer = 0

#main loop of the program
#this ends the loop once all commands are removed from the dictionary
while len(COMMANDS) > 1:
    #chooses a command from the dictionary at random
    cmd = choice(list(COMMANDS))

    while True:

        answer = input('\n' + 'Description:\n' + COMMANDS[cmd] + "\n\nType the command that matches this description: ")

       #removes the correct answser from the dictionary and loops back to the next
        if cmd == answer:
            COMMANDS.pop(cmd)
            print('\nGood Job')

            break
        #option to quit
        if answer == 'q':
            print('Thanks for using Daily Linux Practice.')
            sys.exit()
        #iterates wrong_answer by one and goes back to the beginning of the loop with the same cmd 
        else:
            wrong_answer = wrong_answer + 1
            print("\nTry again!")
        #if too many wrong guesses then reset counter and display the correct command and start with a new cmd
        if wrong_answer == 3:
            wrong_answer = 0
            print('\nThe correct answer was' + ' ' + cmd + '\n')

            break

