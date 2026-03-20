"""This module is designed to test the connection of the machine to ensure
there are not any connectivity issues. Also checks for the platform type,
as well as retrieve the source card data."""

import os
import csv
import chardet
import requests
import platform
import subprocess
from pathlib import Path

scope = (''
        )

# Absolute pathing variables
_current_file = Path(__file__).resolve()
_module_dir = _current_file.parent
_root_dir = _module_dir.parent

class SmartJack():
    def __init__(self):
        """Initiate smartjack web access instance."""
        self.test_dict = {'1':'google.com',
                    '2':'4.2.2.2',
                    '3':'8.8.4.4',
                    '4':'4.2.2.2',
                    '5':'8.8.8.8',
                    '6':'4.2.2.1'}
        # Assigns the key name as the destination and the 
        # value declared as the optional port to access
        self.dest_dict ={}
        # Gets the current working directory for file handling
        self.cwd = os.getcwd()
        # Assigns the key name from dest_dict.keys() to input()
        # value representing local filepath.
        self.dest_file_path = {}

    def add_dest(self, dest, port=None):
        """Populate the destination dict with nodes you wish to
        access. Declare a port number as required."""
        if port != None:
            dest_dict[dest] = port
        else:
            dest_dict[dest] = None
        return

    def get_dest_filepath(self, filepath_list):
        """Access the list of keys in the destination dict and
        prompt the user for input on where to put each item once
        retrieved by self.file_upd()."""
        if len(filepath_list) > len(dest_dict.keys()):
            raise ValueError('Too many items in the supplied list'
                            'of filepaths.')
        elif len(filepath_list) < len(dest_dict.keys()):
            raise ValueError('Too few items in the supplied list'
                            'of filepaths.')
        elif len(filepath_list) != len(dest_dict.keys()):
            raise ValueError('Incorrect number of items in filepath'
                            'list supplied.')
        else:
            for key in dest_dict.keys():
                dest_file_path[key] = filepath
            return


    def file_upd(self):
        """Access the mtgjson host and get the most up to date
        card list from the Oracle db."""
        self.get_dest_filepath()
        print('Retrieving data from source destination; this may'
            'take a minute.')
        for key, value in self.dest_file_path:
            with requests.get(key, stream=True) as request:
                request.raise_for_status()
                with open(value, 'wb') as file:
                    file.write(request.content)
                    # Pulls raw data to manually decode
                    request_content = request.content
                    detenc = chardet.detect(request_content)
                    if debug:
                        print('encoding: ', request.encoding)
                        print('header: ', request.headers)
                        print('size: ', len(request.content))
                        print('status: ', request.status_code)
                        print('chardet: ', detenc)

    def dest_test(self, dest, ping_num):
        """Returns TRUE if dest responds to ICMP; may timeout
        due to dest config."""
        # Checks for OS compatibility and sets proper parameter
        # definition. 
        param = '-n' if platform.system().lower()=='windows' else '-c'
        if debug:
            print('param: ' + param)
        # Defines exact command syntax using var formatting 
        command = ['ping', param, ping_num, dest]
        if debug:
            print('command: ', command)
            print('command call: ', subprocess.call(command))
        # Gives TRUE/FALSE return based on the output of the
        # subprocess.call() func
        return True if subprocess.call(command)== 0 else False

    def path_iter(self):
        """Iterate over the K:V pairs in the provided dict, added
        the keys as destinations and the values as ping amounts
        to self.dest_dict."""
        icmp = False
        # Iterates through the destination dictionary to verify
        # connectivity
        for k, v in self.dest_dict:
            while not icmp:
                if debug:
                    print(f'Attempting to send ' + str(k) 
                            + ' packet(s) to ' + str(v))
                # Pings each iterate and checks for response
                if self.dest_test():
                    icmp = True
                    if debug:
                     print('ICMP: ', icmp)
                else:
                    icmp = False
                    if debug:
                        print(icmp)
        return icmp
