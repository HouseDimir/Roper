Author: Jessie Kovacs
CC-BY-NC-ND
jkcreations.carrd.co/Roper

This is a Python based data sorting system designed to separate variable length card lists into Draft Booster packs. To initiate setup, open a command prompt and type "py roper -setup". When running the -cube command use the Cube commands below to define what cards will be searched for. When running the -draft command use the Pack commands below to define how the pack will be generated. 

Documentation:
Each of the available commands are listed below, as well as a short example of how to use them. For the full list of available keywords or arguments passable to one of the selection commands, see the Documentation.txt

-System Commands-
Debug Mode: roper debug
Firstime Setup: roper -setup
Manually Update: roper update forced

-Cube Commands-
Keyword Selection: -kw Banding, Flying, Indestructible, Mill  *Or based selection, may return only creatures






Pulled from code to clean up and store here for further clarification, correction, reference, and expansion as necessary:
Required Arguments
        -draft    True or False; Declare True when you want the card pool separated into Draft packs; If True requires Cube path
        -excl    True or False; Declare True when you want the listed arguments to apply exclusively, returning only cards that match all arguments given
        -mode    add/clr/rmv/shw/upd; set mode to Add, Clear, Remove, Show, or Update respectively; Defines how the commands manipulate the current 

        Optional arguments
        -kw    Space deliniated keywords; Declare the keywords you wish to search for; Likely to return only creatures; Default None
        -cr    True or False; Declare whether cubes will balance the number of commons/uncomons/rares/mythics; Default True
        -mc    Max number of cards you want in the cube; Changes max_pack; Default 360
        -mp    Number of packs you want generated; Only works if -draft is True; Default 24
        -mv    Requires =,<,>,=<, or >= preceed numerical arguments; Accepts any whole number from 0-99; See Documentation for more details
        -gc    True or False; Declare True to allow GameChangers
        -pr    True or False; Declare whether packs will balance rarity among the cards; Default True
        -ps    number of cards per pack; Only works if -draft is True; Default 15
        -s    Three-four letter Set Code; Declare each set you want to sort through
        -sbt    Space deliniated Keywords; Declare subtypes you wish to search for
        -spt    Space deliniated Keywords; Niche; Declare supertypes you wish to search for
        -t    Space deliniated keywords; Declare the card types you wish to search for; May not be compatible with --kw in some instances

