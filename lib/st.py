"""This module is designed to test the connection of the machine to ensure
there are not any connectivity issues. Also checks for the platform type,
as well as retrieve the source card data."""

import os
import csv
import chardet
import requests
import platform
import subprocess

class smartjack():
    def __init__(self):
        self.dest_dict = {'1':'google.com',
                    '2':'4.2.2.2',
                    '3':'8.8.4.4',
                    '4':'4.2.2.2',
                    '5':'8.8.8.8',
                    '6':'4.2.2.1'}
        #gets the current working directory for file handling
        self.cwd = os.getcwd()
        self.dest_file_path = []
        #defines the mtgjson URL to query for All Printings
        self.cardp = 'https://mtgjson.com/api/v5/csv/'
        self.cardf = 'https://mtgjson.com/api/v5/csv/cards.csv'

        #defines the file name for the saved file
        self.ccsv = 'cards.csv'
        self.fp = str(cwd) + '/bin/' + str(ccsv)
        #file path for cards.csv
        self.cfp = str(cwd) + '/bin/' + str(ccsv)


    def get_dest_filepath(self):
        #code to get user input about file name and filepath for each destination in dest_list


    def _file_upd(self):
        """Access the mtgjson host and get the most up to date card list from
        the Oracle db"""
        self.get_dest_filepath()
        print('Retrieving data from source destination; this may take a minute.')
        for path in self.dest_file_path:
            with requests.get(self.dest_file_path[path], stream=True) as request:
                request.raise_for_status()
                with open(file_write_path, 'wb') as file:
                    file.write(request.content)
                    #pulls raw data to manually decode
                    request_content = request.content
                    detenc = chardet.detect(request_content)
                    if debug:
                        print('encoding: ', request.encoding)
                        print('header: ', request.headers)
                        print('size: ', len(request.content))
                        print('status: ', request.status_code)
                        print('chardet: ', detenc)

    def _dest_test(self):
        """Returns TRUE if dest responds to ICMP; may timeout due to dest config"""
        #checks for OS compatibility and sets proper parameter definition. 
        param = '-n' if platform.system().lower()=='windows' else '-c'
        if debug:
            print('param: ' + param)
        #defines exact command syntax using var formatting 
        command = ['ping', param, attempts, dest]
        if debug:
            print('command: ', command)
            print('command call: ', subprocess.call(command))
        #gives TRUE/FALSE return based on the output of the subprocess.call() func
        return True if subprocess.call(command)== 0 else False

    def _path_iter(self, destdict):
        '''Iterate over the K:V pairs in the provided dict, added the keys as destinations and the values as ping amounts to self.dest_dict'''
        icmp = False
        #iterates through the dd dict to verify connectivity
        for k, v in dd.items():
            while not icmp:
                if debug:
                    print(f'Attempting to send ' + str(k) + ' packet(s) to ' + str(v))
                #Pings each iterate and checks for response
                if _ptst(k, v):
                    icmp = True
                    if debug:
                     print('ICMP: ', icmp)
                else:
                    icmp = False
                    if debug:
                        print(icmp)
        return icmp

#if debug:
#    print('Target IPs {#/pings:add}: ', dd)

##calls the ping infrastructure to greenlight the rest of the functions test.
#pexe = _pit(dd)
#if debug:
#    print('Ping test successful: ', pexe)

##tests connection to mtgjson
#if pexe:
#    tget = requests.get(cardf, stream=True)
#    oracletst = True if tget.status_code == 200 else False
#    oracletst
#    if debug:
#        print('Ping response from mtgjson: ', oracletst)
##activates the user prompt to update their data file
#if oracletst:
#    updprompt = True
#    if debug:
#        print('System awaiting input from user: ', updprompt)

##checks for existing data file
#if not os.path.exists(str(cwd) + '/bin/' + str(ccsv)):
#    updprompt = False
#    _cupd()   
##checks to see if the user wants to update the data file before continuing
#else:
#    while updprompt:
#        oracleupd = input('Card data accessible, would you like to update? Y or N')
#        if oracleupd == 'y':
#            updprompt = False
#            _cupd()
#        elif oracleupd == 'n':
#            updprompt = False
#            pass
#        else:
#            print('Invalid entry, please try again.')
#            updprompt = True
