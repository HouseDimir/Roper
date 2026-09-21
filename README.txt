Author: Jessie Kovacs

This is a Python based data sorting system designed to separate variable length card lists into Draft Booster packs. To initiate setup, open a command prompt and type "py roper -setup". When running the -cube command use the Cube commands below to define what cards will be searched for. When running the -draft command use the Pack commands below to define how the pack will be generated. 

----------//To-Do\\----------          
       ===|Legend|===        
| √ | - Completed - | Alt+251/9723 |
| ○ | - In Progress - | Alt+9 |
| x | - Deprecation Removal - | 'x' key |
| ~ | - Admin Task - | Shift+'`' key |
| § | - Functionality Task - | Alt+21 |
        ===|Tasks|===          
| ~ | 1. Commentation pass __main__.py
| ~ | 2. Documentation pass __main__.py
| ~ | 3. Commentation pass frame.py
| ~ | 4. Documentation pass frame.py
| ~ | 5. Commentation pass nput.py
| ~ | 6. Documentation pass nput.py
| ~ | 7. Commentation pass roper.py
| ~ | 8. Documentation pass roper.py
| ~ | 9. Commentation smartjack.py
| ~ | 10. Documentation pass smartjack.py
| ~ | 11. Planning Session - Functionality, Bloat Removal, Priorities, Stretch Goals


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



Timeline:
The following contains basic plans to expand and engineer functionality in the roper modules, as well as plans for the package as a whole.

Package Goal:
A cohesive piece of software that fluidly and efficiently utilizes machine resources and an external connection to draw a series of files from mtgjson.com. It then aims to take the data and sift it into small batches of card data (known as a Cube) to be chosen from at will or used to dynamically generate Draft Packs for users to host home-made draft games with friends.

nPut module:
Take either dynamic user input or file input and process the text string into a series of commands and attributes to guide the behavior of the various functions called by the argument parser.

smartjack module:
Dynamically contact listed destination addresses and then pull the data available from the web page to store as directed by kwargs.

roper module:
Access card database and process command input to output a series of arrays comprised of the card data based on the search terms entered. Should be able to accept Scryfall style search terms, with some exceptions, and should be able to accept lists of cards extracted from a file input by the user. 

frame module:
Should contain a simple and usable UI to allow basic CLI interaction with the system. Minimal functionality to create minimal bugs.

__main__ module:
Accurately commented and directed module which clearly and succinctly calls and iterates through the various modules accompanying the package.

Expected UI ver 0.0.1a - 1 Oct, '26
Expected nPut & smartjack ver 0.0.1a - 1, Jan '27
Expected roper ver 0.0.1a - 16 Apr, '27


Last Update 15 Aug, '26