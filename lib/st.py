"""This module is designed to test the connection of the machine to ensure
there are not any connectivity issues. Also checks for the platform type,
as well as retrieve the source card data."""

import os
import csv
import chardet
import requests
import platform
import subprocess

#Defines the mtgjson URL to query for All Printings
cardp = 'https://mtgjson.com/api/v5/csv/'
cardf = 'https://mtgjson.com/api/v5/csv/cards.csv'

#Defines the file name for the saved file
ccsv = 'cards.csv'

#Gets the current working directory for file handling
cwd = os.getcwd()
#File path for cards.csv
cfp = str(cwd) + '/bin/' + str(ccsv)
#Defines the number of tests and where the packets are sent.
#Iterate through for most consistent results.
dd = {
    '1':'google.com',
    '2':'4.2.2.2',
    '3':'8.8.4.4',
    '4':'4.2.2.2',
    '5':'8.8.8.8',
    '6':'4.2.2.1'
    }
debug = True
fp = str(cwd) + '/bin/' + str(ccsv)
updprompt = False

#Defines the lists to organize the data by Color Identity
bl = []
gl = []
ll = []
ml = []
rl = []
ul = []
wl = []
xl = []
lc = [bl, gl, ll, ml, rl, ul, wl, xl]

#Defines the various CSV values for multicolor cards
mc = [
    "B, G, R, U, W",
    "B, G, R, U",
    "G, R, U, W",
    "B, R, U, W",
    "B, G, U, W",
    "B, G, R, W",
    "B, G, R",
    "B, G, U",
    "B, G, W",
    "B, R, U",
    "B, R, W",
    "B, U, W",
    "G, R, U",
    "G, R, W",
    "G, U, W",
    "G, U, B",
    "R, U, W",
    "R, U, G",
    "R, U, B",
    "R, G, B",
    "U, R, G",
    "U, B, G",
    "U, G, W",
    "U, R, W",
    "B, G",
    "B, R",
    "B, U",
    "B, W",
    "G, R",
    "G, U",
    "G, W",
    "G, B",
    "R, U",
    "R, W",
    "R, B",
    "R, G",
    "U, W",
    "U, B",
    "U, G",
    "U, R",
    "W, B",
    "W, G",
    "W, R",
    "W, U"
    ]

#Define the file paths for the sorted card files
bfp = str(cwd) + '/bin/cards_black.csv' 
gfp = str(cwd) + '/bin/cards_green.csv'
lfp = str(cwd) + '/bin/cards_nbl.csv'
mfp = str(cwd) + '/bin/cards_multi.csv'
rfp = str(cwd) + '/bin/cards_red.csv'
ufp = str(cwd) + '/bin/cards_blue.csv'
wfp = str(cwd) + '/bin/cards_white.csv'
xfp = str(cwd) + '/bin/cards_colorless.csv'
sl = [bfp, gfp, lfp, mfp, rfp, ufp, wfp, xfp]

#Counts each iteration when sorting the cards into the respective files
rc = 0

def _cupd():
    """Access the mtgjson host and get the most up to date card list from
    the Oracle db"""
    print('Getting the card data from mtgjson.com; this may take a minute.')
    with requests.get(cardf, stream=True) as r:
        r.raise_for_status()
        with open(fp, 'wb') as f:
            f.write(r.content)
            #Pulls raw data to manually decode
            rc = r.content
            detenc = chardet.detect(rc)
            if debug:
                print('encoding: ', r.encoding)
                print('header: ', r.headers)
                print('size: ', len(r.content))
                print('status: ', r.status_code)
                print('chardet: ', detenc)

def _ptst(attempts, dest):
    """Returns TRUE if dest responds to ICMP; may timeout due to dest config"""
    #Checks for OS compatibility and sets proper parameter definition. 
    param = '-n' if platform.system().lower()=='windows' else '-c'
    if debug:
        print('param: ' + param)
    #Defines exact command syntax using var formatting 
    command = ['ping', param, attempts, dest]
    if debug:
        print('command: ', command)
        print('command call: ', subprocess.call(command))
    #Gives TRUE/FALSE return based on the output of the subprocess.call() func
    return True if subprocess.call(command)== 0 else False

def _pit(destdict):
    """Iterate over the K:V pairs in the provided dict, stopping when a
    return is TRUE"""
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

def _toggledebug():
    '''Checks to see if debug var is True, or false, then switches the value'''
    if not debug:
        debug = True
    else:
        debug = False
    return debug

if debug:
    print('Target IPs {#/pings:add}: ', dd)

#Calls the ping infrastructure to greenlight the rest of the functions test.
pexe = _pit(dd)
if debug:
    print('Ping test successful: ', pexe)

#Tests connection to mtgjson
if pexe:
    tget = requests.get(cardf, stream=True)
    oracletst = True if tget.status_code == 200 else False
    oracletst
    if debug:
        print('Ping response from mtgjson: ', oracletst)
#Activates the user prompt to update their data file
if oracletst:
    updprompt = True
    if debug:
        print('System awaiting input from user: ', updprompt)

#Checks for existing data file
if not os.path.exists(str(cwd) + '/bin/' + str(ccsv)):
    updprompt = False
    _cupd()   
#Checks to see if the user wants to update the data file before continuing
else:
    while updprompt:
        oracleupd = input('Card data accessible, would you like to update? Y or N')
        if oracleupd == 'y':
            updprompt = False
            _cupd()
        elif oracleupd == 'n':
            updprompt = False
            pass
        else:
            print('Invalid entry, please try again.')
            updprompt = True

#Opens and loads the csv into a nested set of lists to process
try:
    with open(cfp, 'r', newline='', encoding='utf-8') as cards:
        r = csv.reader(cards)
        for l in r:
            if 'Basic Land' in l[77]:
                pass
            else:
                if not l[77] == 'Land':
                    if l[10] == 'B':
                        bl.append(l)
                    elif l[10] == 'G':
                        gl.append(l)
                    elif l[10] == 'R':
                        rl.append(l)
                    elif l[10] == 'U':
                        ul.append(l)
                    elif l[10] == 'W':
                        wl.append(l)
                    elif l[10] == '':
                        xl.append(l)
                    elif l[10] in mc: 
                        ml.append(l)
                    elif l[10] == 'colors':
                        pass
                    else:
                        if debug:
                            print(l[10])
                            print(l[52])
                        print("Found unexpected value in card type field. Please refresh source data as it may be corrupted.")
                        raise ValueError()
                else:
                    ll.append(l)
#Exception Handling to ensure there is a file for the cards to go to                    
except FileNotFoundError:
    st._cupd()
    with open(cfp, 'r', newline='', encoding='utf-8') as cards:
        r = csv.reader(cards)
        for l in r:
            if 'Basic Land' in l[77]:
                pass
            else:
                if not l[77] == 'Land':
                    if l[10] == 'B':
                        bl.append(l)
                    elif l[10] == 'G':
                        gl.append(l)
                    elif l[10] == 'R':
                        rl.append(l)
                    elif l[10] == 'U':
                        ul.append(l)
                    elif l[10] == 'W':
                        wl.append(l)
                    elif l[10] == '':
                        xl.append(l)
                    elif l[10] in mc:
                        ml.append(l)
                    else:
                        if debug:
                            print(l[10])
                            print(l[52])
                        print("Found unexpected value in card type field. Please refresh source data, as it may be corrupted.")
                        raise ValueError()
                else:
                    ll.append(l)
        
#Check to see if the named files exist and deletes them before proceeding
for n in range(len(sl)):
    p = sl[n]
    l = lc[n]
    if os.path.exists(p):
        os.remove(p)
        with open(p, 'w', newline='', encoding='utf-8') as sort:
            w = csv.writer(sort)
            for c in l:
                w.writerow(c)
                print('Finished sorting row ' +str(rc))
                rc += 1
    else:
       with open(p, 'w', newline='', encoding='utf-8') as sort:
        w = csv.writer(sort)
        for c in l:
            w.writerow(c)
            print('finished sorting row ' + str(rc))
            rc += 1
