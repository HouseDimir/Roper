"""nPut serves as a custom command-line argument parsing module
with a focus on taking classic Unix style command window entries
and handling them in a pythonic way. nPut aims to be a learning
tool as much as a foundational tool in further development of
larger projects."""

## To be reworked to handle output of command as str variable
## from user interface software

import os
import re
import datetime
from pathlib import Path

scope = (''
        )

# Absolute pathing variables
_current_file = Path(__file__).resolve()
_module_dir = _current_file.parent
_root_dir = _module_dir.parent

class Listener():
    """Listener object to accept user input."""
    def __init__(self, logging, debug=False):
        self.logging = logging
        self.debug = debug
        self.output: str = ''
        self.exit = False
        self.helpmode = False
        if self.debug:
            print('Finished initializing Listener().')
            
    def destroy(self):
        """Close Listener."""
        if self.debug:
            print('Destroying Listener().')
        self.exit = True
        return
    
    def listen(self):
        """Begin listening through input object."""
        if self.debug:
            print('Enabling command input:')
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
    """Parsing object to handle live user input."""
    def __init__(self,
                listener_mode=False,
                listener=None,
                variable_mode=False,
                variable=None,
                file_mode=False,
                filepath=None,
                debug=False):
    self.debug = debug
        if not listener_mode and not variable_mode and not file_mode:
            raise AttributeError('Mode not defined on initialization.'
                                'Please set <nParse.listener_mode>, '
                                '<nParse.variable_mode>, or <nParse.file_mode> '
                                'and then define <nParse.listener>, '
                                '<nParse.variable>, or <nParse.filepath> '
                                'respectively when calling <nParse>.')
        elif listener_mode:
            self.listener=listener
            self.variable = None
            self.filepath = None
        elif variable_mode:
            self.variable = variable
            self.listener = None
            self.filepath = None
        elif file_mode:
            self.filepath = filepath
            self.listener = None
            self.variable = None
        else:
            pass
        self.commands = {}
        self.output = {}
        # Variables to define regex patterns
        self.alph = r'[a-zA-Z]'
        self.num = r'[0-9]'
        self.alphnum = r'[a-zA-Z0-9]'
        self.sym = r'[><=]'
        # Date time management
        self.now = datetime.datetime.now()
        self.datetime = self.now.year
        self.today = self.now.today()
        self.log_path = os.getcwd() + f'/logs/{self.today}.txt'
        if self.debug:
            print('Finished initialing nParse().')


    def add_command(self, command):
        """Dynamically add commands, where command is a dict with
        the various parameter names as the key and the values
        themselves as the values assigned to each argument name.

        Ex: 
        command = {
                'str_':'-cmd',
                'func':function(),
                'arg_count':'0',
                'default':False
                'help_':'this is a help string',
                'required':False,
                'type_':bool
                'mod':None
                }"""
        if self.debug:
            print(f'Adding {command} to self.commands')
        self.commands[command['str_']] = command

    def commands_action(self):
        """Call the functions passed as command variables to 
        add_argument() before clearing the self.output attribute."""
# Rework to handle dict of dicts
        if self.debug:
            print('Running stored commands.')
        for command in self.commands and call.keys() in self.output:
            if  != command['str_']:
                pass
            else:
                command['func']()

    def enum(self):
        """Get the length of passed output."""
# Rework to handle dynamic entry
        if self.debug:
            print('Getting the length of the output.')
        return len(self.listener.output)

    def toggle_debug(self):
        """Enable debug strings."""
        if self.debug:
            print('Disabling debug.')
            self.debug = False
        else:
            self.debug = True
        return
        
    def parse_input(self):
        """Break the input into the command and its associated
        arguments in a {k1:[v1.1,v1.2,v1.3], k2:[v2.1,v2.2,v2.3]}
        k=command v=arguments."""

## To be reworked to respect listener/variable/file mode
## To be reworked to better match Unix convention
## To be reworked to handle commands as dict instead of list of attr
        if self.listener != None:
            nput = self.listener.listen()
        elif self.variable != None:
            nput = self.variable
        else:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                nput = file.read()
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
                char_match = re.match(self.alphnum, nput[num + 1])
                sym_match = re.match(self.sym, nput[num + 1])
            # Pass through errors from reaching the end of the list
            except IndexError:
                pass
            # Break out for helpmode
            if nput[num] == '?':
                helpmode = True
                break
            # Ensure the 0th item is recorded
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
            elif re.match(self.alphnum, nput[num]) or re.match(self.sym, nput[num]):
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