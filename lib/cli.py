import os
import re
import datetime

###store all valid commands for reference later.
##params_dict = {
##    '-excl':[exclCLI(), '*', False, bool, None, False, 'exclude cards that do not match all selected criteria, default inclusive'],
##    '-txt':[txtCLI(), '+', '', str, None, False, 'list of words or phrases you wish to select from all text on a card for the cube'],
##    '-kw':[kwCLI(), '+', '', str, None, False, 'list of Keywords you wish to select for the cube; may return only creatures; may not be compatible with --t'], 
##    '-s':[scCLI(), '+', '', str, None, False, 'list of Set Codes you wish to select for the cube'],
##    '-mv':[mvCLI(), '?', '', str, None, False, '=/</>/<=/>= mana value; see documentation'],
##    '-gc':[gcCLI(), '*', False, bool, None, False, 'are Gamechangers allowed or disallowed in the cube'],
##    '-subt':[subtCLI(), '+', '', str, None, False, 'list of subtypes you wish to select for the cube'],
##    '-supt':[suptCLI(), '+', '', str, None, False, 'list of supertypes you wish to select for the cube'],
##    '-t':[typeCLI(), '+', '', str, None, False, 'list of Types you wish to select for the cube; may not be compatible with --kw']
##    }

#listener object to accept user input
class listener():
    def __init__(self, logging):
        self.logging = logging
        self.log_path = os.getcwd()+f'/logs/{dt}.txt'
        self.output: str = ''
        self.exit = False
        self.helpmode = False
        #variables to define regex patterns
        self.alph = r'[a-zA-Z]'
        self.num = r'[0-9]'
        self.alphnum = r'[a-zA-Z0-9]'
        self.sym = r'[><=]'
        #date time management
        self.dt = datetime.datetime(2026, 3, 11)
        self.dt = dt.today()

    #close Listener             
    def exit(self):
        self.exit = True
        return
    
    #begin listening through input object
    def listen(self):
        if not self.helpmode:
            self.output = input()
            return self.output
        #help Mode Dialogue
        else:
            self.output = input("Help Mode; Enter a command to receive a brief description and usage example:") and self.listening
            return self.output
        
#parsing object to handle live user input
class nParse():
    def __init__(self, listener):
        self.listener=listener
        self.debug = False

    def enum(nput):
        #get the length of the string
        return len(nput.items())

    def enable_debug():
        #turn on debug mode
        self.debug = True
        return
        
    #beak the input into the command and its associated arguments in a {k1:[v1.1,v1.2,v1.3], k2:[v2.1,v2.2,v2.3]} k=command v=arguments 
    def parse_input(self):
        nput = self.listener.listen()
        lenput = len(nput)
        #storage variables for str op
        assembler = []
        last_key: str = ''
        stored_vars = []
        output = {}
        #iterate over the length of the nput to perform input phrase separation by space
        for n in range(0, lenput):
            if self.debug:
                print(f'Character: {nput[n]} \n Char Num: {n}')
            #check the value of the next character in the input stream
            try:
                char_match = re.match(alphnum, nput[n+1])
                sym_match = re.match(sym, nput[n+1])
            #pass through errors from reaching the end of the list
            except IndexError:
                pass
            #break out for helpmode
            if nput[n] == '?':
                helpmode = True
                break
            #ensure the 0th item is recorder
            elif n == 0:
                assembler.append(nput[n])
                if self.debug:
                    print(f'Assembler: {assembler}')
            #pass on the second half of command terminator
            elif nput[n] == '-' and nput[n-1] == '-':
                pass
            #pass on the receding space of command terminator
            elif nput[n] == ' ' and nput[n-1] == '-' and nput[n-2] == '-':
                pass
            #check if the current character fits alphanum/symbols
            elif re.match(alphnum, nput[n]) or re.match(sym, nput[n]):
                assembler.append(nput[n])
                if self.debug:
                    print(f'Assembler: {assembler}')
            elif nput[n] == '-' and nput[n+1] == '-':
                #store the last key and its accumulated variables in the output dict
                output[last_key] = []
                for i in stored_vars:
                    output[last_key].append(i)
                if self.debug:
                    print(f'Output: {output}')
                #clear out any to be used variables before the saving the current progress
                last_key: str = ''
                stored_vars.clear()
            elif nput[n] == ' ':
                #turn the list of character strings into a single string before saving the string as a key variable
                tier_2: str=''
                if self.debug:
                    print(f'Assembler: {assembler}')
                for s in assembler:
                    tier_2+=s
                if self.debug:
                    print(f'Tier_2: {tier_2}')
                key_search = re.search(r'\-', tier_2)
                assembler.clear()
                #stores the finished word as a key or variable
                if key_search:            
                    last_key+=tier_2
                    if self.debug:
                        print(f'Last Key: {last_key}')
                    tier_2: str = ''
                else:
                    stored_vars.append(tier_2)
                    if self.debug:
                        print(f'Stored Vars: {stored_vars}')
                    tier_2: str=''
            #break out if incorrect command
            elif nput[n] == '-' and not char_match and not sym_match:
                raise ValueError("An incorrect command was supplied!")
            #store the character if it fits alphanum/symbol pattern
            elif nput[n] == '-' and char_match or sym_match:
                assembler.append(nput[n])
                if self.debug:
                    print(f'Assembler: {assembler}')
            #break out for unrecognized characters
            else:
                raise AttributeError(f"Unrecognized character input: {nput[n]}")
        return output

##handle command input storage and engine switching
#def cube_gen():
#    #enables cube generation loops to the suplied arguments
#    pass

##Define argument parsing framework and command handling
#listener = listener(False)
#parse = nParse(listener)
#while not listener.exit:
#    args = parse.parse_input()
#    print(args)
