"""nPut serves as a custom command-line argument parsing module
with a focus on taking classic Unix style command window entries
and handling them in a pythonic way. nPut aims to be a learning
tool as much as a foundational tool in further development of
larger projects."""

import os
import re
import datetime

class Listener():
    """Listener object to accept user input"""
    def __init__(self, logging):
        self.logging = logging
        self.output: str = ''
        self.exit = False
        self.helpmode = False
        # Variables to define regex patterns
        self.alph = r'[a-zA-Z]'
        self.num = r'[0-9]'
        self.alphnum = r'[a-zA-Z0-9]'
        self.sym = r'[><=]'
        # Date time management
        self.datetime = datetime.datetime(2026, 3, 11)
        self.today = datetime.today()
        self.log_path = os.getcwd() + f'/logs/{today}.txt'
            
    def exit(self):
        """Close Listener"""
        self.exit = True
        return
    
    def listen(self):
        """Begin listening through input object"""
        if not self.helpmode:
            self.output = input()
            return self.output
        # Help Mode Dialogue
        else:
            self.output = input('Help Mode; Enter a command to '
                                'receive a brief description and '
                                'usage example:')
            return self.output
        
class nParse():
    """Parsing object to handle live user input"""
    def __init__(self, listener):
        self.listener=listener
        self.debug = False
        self.commands = {}
        self.output = {}

    def add_command(self, command):
        """Dynamically add commands, where command is a dict with
        the various parameter names as the key and the values
        themselves as the values assigned to each argument name.

        Ex: 
        command = {
                'str_':'-excl',
                'func':function(),
                'arg_count':'0',
                'default':False
                'help_':'this is a help string',
                'required':False,
                'type_':bool
                'mod':None
                }"""
        str_ = command['str_']
        func = command['func']
        arg_count = command['arg_count']
        help_ = command['help_']
        required = command['required']
        type_ = command['type_']
        mod = command['mod']
        self.commands[str_] = [str_, func, arg_count, help_, required, type_, mod]
        return self.commands[str_]

    def commands_action(self):
        """Call the functions passed as command variables to 
        add_argument() before clearing the self.output attribute."""
        # attr = commands.values()
        # for value in attr:
        #     for arg_ in value:
        #         if type(arg) == 'function':
        #             ()
        pass

    def enum(self):
        """Get the length of passed output."""
        return len(self.listener.output)

    def enable_debug(self):
        """Enable debug strings."""
        self.debug = True
        return
        
    def parse_input(self):
        """Break the input into the command and its associated
        arguments in a {k1:[v1.1,v1.2,v1.3], k2:[v2.1,v2.2,v2.3]}
        k=command v=arguments."""

        ## To be reworked to better match Unix convention
        nput = self.listener.listen()
        lenput = len(nput)
        # Storage variables for str op
        assembler = []
        last_key: str = ''
        stored_vars = []
        # Iterate over the length of the nput to perform input phrase separation by space
        for num in range(0, lenput):
            if self.debug:
                print(f'Character: {nput[num]} \n Char Num: {n}')
            # Check the value of the next character in the input stream
            try:
                char_match = re.match(alphnum, nput[num + 1])
                sym_match = re.match(sym, nput[num + 1])
            # Pass through errors from reaching the end of the list
            except IndexError:
                pass
            # Break out for helpmode
            if nput[num] == '?':
                helpmode = True
                break
            # Ensure the 0th item is recorder
            elif num == 0:
                assembler.append(nput[num])
                if self.debug:
                    print(f'Assembler: {assembler}')
            # Pass on the second half of command terminator
            elif nput[num] == '-' and nput[num - 1] == '-':
                pass
            # Pass on the receding space of command terminator
            elif nput[num] == ' ' and nput[num - 1] == '-' and nput[n-2] == '-':
                pass
            # Check if the current character fits alphanum/symbols
            elif re.match(alphnum, nput[num]) or re.match(sym, nput[num]):
                assembler.append(nput[num])
                if self.debug:
                    print(f'Assembler: {assembler}')
            elif nput[num] == '-' and nput[num + 1] == '-':
                # Store the last key and its accumulated variables in the output dict
                self.output[last_key] = []
                for item in stored_vars:
                    self.output[last_key].append(item)
                if self.debug:
                    print(f'Output: {self.output}')
                # Clear out any to be used variables before the saving the current progress
                last_key: str = ''
                stored_vars.clear()
            elif nput[num] == ' ':
                # Turn the list of character strings into a single string before saving the string as a key variable
                tier_2: str = ''
                if self.debug:
                    print(f'Assembler: {assembler}')
                for str_ in assembler:
                    tier_2 += str_
                if self.debug:
                    print(f'Tier_2: {tier_2}')
                key_search = re.search(r'\-', tier_2)
                assembler.clear()
                # Stores the finished word as a key or variable
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
            # Break out if incorrect command
            elif nput[num] == '-' and not char_match and not sym_match:
                raise ValueError("An incorrect command was supplied!")
            # Store the character if it fits alphanum/symbol pattern
            elif nput[num] == '-' and char_match or sym_match:
                assembler.append(nput[num])
                if self.debug:
                    print(f'Assembler: {assembler}')
            # Break out for unrecognized characters
            else:
                raise AttributeError(f"Unrecognized character input: {nput[num]}")
        return self.commands