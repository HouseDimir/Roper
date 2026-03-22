"""This module is designed to take command-line input to configure
how to generate either a Cube() object containing a large number
of card data to be referenced later, or a number of Pack() objects
from a supplied Cube() object, each of which contains a smaller
number of cards which can repeat."""

import os
import re
import nput
import random
import smartjack
from pathlib import Path


#UUIDs card[79]
scope = (''
        )

# Absolute pathing variables
_current_file = Path(__file__).resolve()
_module_dir = _current_file.parent
_root_dir = _module_dir.parent

class Cube():
    """Initialize Cube object to store Pack generation pool."""
    def __init__(self, inst_id, debug):
        # Basic identifying information
        self.inst_id = str('cube_', inst_id)
        self.debug = debug
        self.path: str = path
        self.verfd: bool = False
        self.draft: bool = False
        self.populated: bool = False
        self.purge: bool = False
        self.max_cards: int = 360
        self.max_packs: int = self.max_cards/15
        source_list = ['bin/cards_black.csv',
                        'bin/cards_blue.csv',
                        'bin/cards_colorless.csv',
                        'bin/cards_green.csv',
                        'bin/cards_multicolor.csv',
                        'bin/cards_nbl.csv',
                        'bin/cards_red.csv',
                        'bin/cards_white.csv']
        self.cube_list = []
        self.sorted_list = {}
        # Defines the lists to organize the data by Color Identity
        self.black_list = []
        self.green_list = []
        self.land_list = []
        self.mc_list = []
        self.red_list = []
        self.blue_list = []
        self.white_list = []
        self.x_list = []
        self.list_container = [self.black_list,
                                self.green_list,
                                self.land_list,
                                self.mc_list,
                                self.red_list,
                                self.blue_list,
                                self.white_list, 
                                self.x_list]
        # Defines the various CSV values for multicolor cards
        self.mc = ["B, G, R, U, W",
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
                    "W, U"]
        # Define the file paths for the sorted card files
        self.black_filepath = str(cwd) + '/bin/cards_black.csv' 
        self.green_filepath = str(cwd) + '/bin/cards_green.csv'
        self.land_filepath = str(cwd) + '/bin/cards_nbl.csv'
        self.mc_filepath = str(cwd) + '/bin/cards_multi.csv'
        self.red_filepath = str(cwd) + '/bin/cards_red.csv'
        self.blue_filepath = str(cwd) + '/bin/cards_blue.csv'
        self.white_filepath = str(cwd) + '/bin/cards_white.csv'
        self.x_filepath = str(cwd) + '/bin/cards_colorless.csv'
        self.source_list_container = [black_filepath,
                                    green_filepath,
                                    land_filepath,
                                    mc_filepath,
                                    red_filepath,
                                    blue_filepath,
                                    white_filepath,
                                    x_filepath]
        if self.debug:
            print('Finished initializing Cube().')
    
    def add_card(self, card):
        """Add card to the cube path file and card UUID to cube.cube_list."""
# Rework to update file
        if self.debug:
            print(f'Adding {card} to Cube.filepath.')
        with open(self.path, 'w', encoding='utf-8') as cube:
            cube.write(card)
        self.cube_list.append(card[79])
        return

    # Fix this to actually work /o\ xnx
    def generate(self, output):
        """Iterate through card source files and create a list of all cards
        that match the supplied arguments."""
        exclusive = False
        # Explicit type check all values
        if output.type() != 'dict':
            raise TypeError(f"Improper argument type passed to _sourceIter(): "+output.type)
        elif list_[key].type() in output.keys() != 'str':
            raise TypeError(f"Improper argument type passed from nParse.parse_input(): "+arg.type)
        else:
            # Iterate across sorted card lists
            if self.debug:
                print('Parsing received commands:')
            for item in self.source_list:
                item_path = str(cwd) + item
                with open(item_path, 'r', newline='', encoding='utf-8') as source:
                    # Iterate over each card in each list
                    for card in source:
                        operand = ''
                        if '-excl' in output.keys():
                            excl = True
                        if excl:
                            # Exclusivity handling
                            if self.debug:
                                print('Handling exclusivity.')
                            pass
                        if key == '-gc':
                            # GameChanger card[33]
                            if self.debug:
                                print('Handling Gamechangers.')
                            pass
                        for  key in output.keys():
                            # Compare arguments sorted into dicts; Key = str(kwarg) : Value = list(positional, args, space, deliniated)
                            if key == '-kw':
                                # Keywords card[44]
                                if self.debug:
                                    print('Handling Keywords.')
                                for arg_kw in output['-kw']:
                                    if arg_kw in card[44]:
                                        self.add_card(card)
                            elif key == '-s':
                                # Set codes card[68]
                                if self.debug:
                                    print('Handling Set Codes.')
                                for arg_set in output['-s']:
                                    if arg_set in card[68]:
                                        self.add_card(card)
                            elif key == '-mv':
                                # Mana value card[51]
                                if self.debug:
                                    print('Handling Mana Values.')
                                for value in output['-mv']:
                                    try:
                                        digit = int(v)
                                    except ValueError:
                                        if re.match(nput.sym, v):
                                            operand = v
                                        else:
                                            pass
                                if operand == '>=':
                                    # >=
                                    if card[51] >= digit:
                                        self.add_card(card)
                                elif operand == '>':
                                    # >
                                    if card[51] > digit:
                                        self.add_card(card)
                                elif operand == '=':
                                    # =
                                    if card[51] == digit:
                                        self.add_card(card)
                                elif operand == '<':
                                    # <
                                    if card[51] < digit:
                                        self.add_card(card)
                                elif operand == '<=':
                                    # <=
                                    if card[51] <= digit:
                                        self.add_card(card)
                                else:
                                    # Error message for invalid operand
                                    raise ValueError("Incorrect symbol passed to -mv.")
                            elif key == '-subt':
                                # Subtype card[73]
                                if self.debug:
                                    print('Handling SubTypes.')
                                pass
                            elif key == '-supt':
                                # Supertype card[74]
                                if self.debug:
                                    print('Handling SuperTypes.')
                                pass
                            elif key == '-t':
                                # Type card[77]
                                if self.debug:
                                    print('Handling Types.')
                                for arg_t in output['-t']:
                                    if arg_t in r[77]:
                                        self.add_card(card)
                            else:
                                # Handle unexpected kwargs
                                return ValueError("Cubitrice did not recognize the argument you passed "+str(arg))
        if len(self.cube_list) > self.max_cards:
            self.purge = True
        self.populated = True
        return

    def list_cards(self, sorted=False):
        """List cards in Cube.cube_list by Name, Color, and Type info.
        Pass sorted=True to the method to list the cards by their sorted
        values."""
        if self.debug:
            print('Listing cards in Cube() file:')
        with open(self.path, 'r', encoding='utf-8', newline='') as cube:
            for line in cube:
                line = pack.readline()
                print('name: '+line[52]+', '+'color(s): '+line[10]+', '+'type: '+line[77])

    def list_sort(self):
        """Sort Cube.cube_list by rarity to display."""
        # Create separate lists of cards by rarity then populate
        common = []
        uncommon = []
        rare = []
        mythic =[]
        if self.debug:
            print('Sorting Cube() list.')
        with open(self.path, 'r', encoding='utf-8') as cards:
            for cid in self.cube_list:
                # Check the rarity of each card and append it to the appropriate list
                    for num in range(len(cards)):
                        line = cards.readline()
                        if cid in line and line[64] == 'common':
                            common.append(cid)
                        elif cid in line and line[64] == 'uncommon':
                            uncommon.append(cid)
                        elif cid in line and line[64] == 'rare':
                            rare.append(cid)
                        elif cid in line and line[64] == 'mythic':
                            mythic.append(cid)
                        else:
                            pass
        self.sorted_list['common']: common
        self.sorted_list['uncommon']: uncommon
        self.sorted_list['rare']: rare
        self.sorted_list['mythic']: mythic
        return self.sorted_list

    def remove_card(self, card_id):
        """Remove card from the Cube.cube_list, Cube.sorted_list,
        and the Cube.filepath. card_id should be card UUID."""
        # Init list to track all cards from cube.path file
        cards = []
        if self.debug:
            print('Removing card from Cube().')
        # Remove the UUID from the cube list
        for cid in self.cube_list:
            if card_id == cid:
                self.cube_list.remove(cid)
        # Remove the UUID from the sorted list
        for cid in self.sorted_list:
            if card_id == cid:
                self.sorted_list.remove(cid)
        # Pack the cube.path file into the cards list
        with open(self.path, 'r', encoding='utf-8') as cube:
            for card in cube:
                card = cube.readline()
                cards.append(card)
        # Find the target card and delete it
        for card in cards:
            if card[79] == card_id:
                cards.remove(card)
        # Write the remaining data to the cube.path file
        with open(self.path, 'w', encoding='utf-8') as cube:
            cube.write(cards)
        return

    def replace_card(self, *kwargs):
        """Replace one card with another, using UUIDs to identify
        both the target and the replacement."""
        if self.debug:
            print('Replacing target cards with replacement cards.')
        for num in range(len(self.replaceCard['args'])):
            for cid in self.cube_list:
# Rework this to actually work
                if cid == n[num]:
                    self.remove_card(cid)
                else:
                    self.add_card(cid)
        return self.cube_list

    def source_sort(self, source_path):
        """Sifts through the all_printings csv and sorts the cards
        present by color to be acted on later."""
        # Counts each iteration when sorting the cards into the respective files
        row_count = 0
        # Opens and loads the csv into a nested set of lists to process
        if self.debug:
            print('Sorting through Source data.')
        try:
            with open(source_path, 'r', newline='', encoding='utf-8') as cards:
                reader = csv.reader(cards)
                for line in reader:
                    if 'Basic Land' in line[77]:
                        pass
                    else:
                        if not line[77] == 'Land':
                            if line[10] == 'B':
                                black_list.append(line)
                            elif line[10] == 'G':
                                green_list.append(line)
                            elif line[10] == 'R':
                                red_list.append(line)
                            elif line[10] == 'U':
                                blue_list.append(line)
                            elif line[10] == 'W':
                                white_list.append(line)
                            elif line[10] == '':
                                x_list.append(line)
                            elif line[10] in self.mc: 
                                mc_list.append(line)
                            elif line[10] == 'colors':
                                pass
                            else:
                                if debug:
                                    print(line[10])
                                    print(line[52])
                                print("Found unexpected value in card type field. Please refresh source data as it may be corrupted.")
                                raise ValueError()
                        else:
                            land_list.append(line)
        # Exception handling to ensure there is a file for the cards to go to                    
        except FileNotFoundError:
            # Some code that pulls the necessary card files
            with open(cfp, 'r', newline='', encoding='utf-8') as cards:
                reader = csv.reader(cards)
                for line in reader:
                    if 'Basic Land' in line[77]:
                        pass
                    else:
                        if not line[77] == 'Land':
                            if line[10] == 'B':
                                black_list.append(line)
                            elif line[10] == 'G':
                                green_line.append(line)
                            elif line[10] == 'R':
                                red_list.append(line)
                            elif line[10] == 'U':
                                blue_list.append(line)
                            elif line[10] == 'W':
                                white_list.append(line)
                            elif line[10] == '':
                                x_list.append(line)
                            elif line[10] in self.mc:
                                mc_list.append(line)
                            else:
                                if debug:
                                    print(l[10])
                                    print(l[52])
                                print('Found unexpected value in card type field. Please refresh source data, as it may be corrupted.')
                                raise ValueError()
                        else:
                            land_list.append(line)
        # Check to see if the named files exist and deletes them before proceeding
        for num in range(len(source_list)):
            path = source_list[num]
            list_ = list_container[num]
            if os.path.exists(path):
                os.remove(path)
                with open(path, 'w', newline='', encoding='utf-8') as sort:
                    write = csv.writer(sort)
                    for card in list_:
                        write.writerow(card)
                        print('Finished sorting row ' +str(row_count))
                        row_count += 1
            else:
               with open(path, 'w', newline='', encoding='utf-8') as sort:
                write = csv.writer(sort)
                for card in list_:
                    write.writerow(card)
                    print('finished sorting row ' + str(row_count))
                    row_count += 1

class Pack():
    def __init__(self, inst_id, cube, debug):
        """Initialize Pack object to store cards up to max_cards."""
        # Basic identifying information
        self.inst_id = str('pack_', inst_id)
        self.cube = cube
        self.debug = debug
        self.path: str = path
        self.verfd: bool = False
        self.draft: bool = True
        # Max cards and various distribution ratios
        self.max_cards: int = 15
        self.color_ratio_min = 1/15
        self.color_ratio_max = 4/15
        self.color_card_ratio_min = self.color_ratio_min*self.max_cards
        self.color_card_ratio_max = self.color_ration_max*self.max_cards
        self.creature_ratio = 4/15
        self.creature_card_ratio = self.creature_ratio*self.max_cards
        self.instant_ratio = 1/15
        self.instant_card_ratio = self.instant_ratio*self.max_cards
        self.sorcery_ratio = 1/15
        self.sorcery_card_ratio = self.sorcery_ratio*self.max_cards
        self.common_ratio = 2/3
        self.uncommon_ratio = 4/15
        self.mythicrare_ratio = 1/15
        self.common_counter_ratio = ((self.common_ratio)*self.max_cards)
        self.uncommon_counter_ratio = ((self.uncommon_ratio+common_ratio)*self.max_cards)
        self.mythicrare__counter_ratio = ((1-(self.mythicrare_ratio))*self.max_cards)
        # Distribution constraint variables
        self.color_counter = {'B':10,
                     'U':10,
                     'G':10,
                     'R':10,
                     'W':10,
                     '':10,
                     'mc':10}
        self.color_pool = ['B', 'G', 'R', 'U', 'W', '', 'mc']
        self.color_dis = {'B': False,
                     'G': False,
                     'R': False,
                     'U': False,
                     'W': False,
                     '': False,
                     'mc': False}
        self.color_bool = False
        self.type_counter = {'Creature': 10,
                        'Instant': 10,
                        'Sorcery': 10}
        self.type_dis = {'Creature': False,
                    'Instant': False,
                    'Sorcery': False}
        self.type_bool = (self.type_dis['Creature'] and
                     self.type_dis['Instant'] and
                     self.type_dis['Sorcery'])
        self.rarity_counter = {'common':10,
                               'uncommon':10,
                               'mythicrare':10}
        self.rarity_pool = ['common', 'uncommon', 'rare', 'mythic']
        self.rarity_dis = {'common':False,
                           'uncommon':False,
                           'mythicrare':False}
        self.rarity_bool = (self.rarity_dis['common'] and
                            self.rarity_dis['uncommon'] and
                            self.rarity_dis['mythicrare'])
        #UUID Lists
        self.pack_list = []
        self.sorted_list = []
        if self.debug:
            print('Finished initializing Pack().')

    def add_card(self, card):
        """Add card to pack_list and pack.filepath by UUID."""
        if self.debug:
            print('Adding card to Pack().')
        with open(self.path, 'w', encoding='utf-8') as pack:
            pack.write(card)
            pack.flush()
            pack.close()
        self.pack_list.append(card[79])            
        return self.pack_list

    def generate(self, rare=True, ratio_c=True, ratio_t=True):
        """Build a self.max_card sized pack of cards from self.cube.
        Rare, ratio_c, and ratio_t should be bool objects denoting
        whether the method should respect distribution constraints
        while generation each pack. they default to True."""
        # Cube should be class cube() object, rare should be bool, ratio_c should be bool, ratio_t should be bool
        # Reset counters
        if self.debug:
            print('Generating Pack() data with - ')
        num = 0
        for key in self.color_counter.keys():
            self.color_counter[key] = 0
        for key in self.rarity_counter.keys():
            self.self.rarity_counter[key]
        for key in type_counter.keys():
            self.type_counter[key] = 0
        # Toggle distribution verification flags
        if not rare:
            if self.debug:
                print('-')
            self.rarity_bool = True
        else:
            if self.debug:
                print('Rarity')
        if not ratio_c:
            if self.debug:
                print('-')
            self.color_bool = True
        else:
            if self.debug:
                print('Color')
        if not ratio_t:
            if self.debug:
                print('-')
            self.type_bool = True
        else:
            if self.debug:
                print('Type')
        if self.debug:
            print('constraints.')
        # Random pack generation resource population
        if self.color_bool and self.rarity_bool and self.type_bool:
            with open(self.cube.path,  'r', encoding='utf-8') as cube:
                cards = []
                for line in cube:
                    card = cube.readline()
                    cards.append(card)
                cube.close()
        # Run until all constraints flags true
        while not color_bool or not type_bool or not rare_bool:
            if self.debug:
                print('Statrting generation process.')
            while not num == self.max_cards:
                ## Variables state reset each card pull iteration
                # Compare cards in pack to rarity ratios
                common = (True if n<=common_counter_ratio else False)
                uncommon = (True if n<=uncommon_counter_ratio and n>= common_counter_ratio else False)
                mythicrare = (True if n<=1 and n>=mythicrare_counter_ratio else False)
                # Make a random selection from the available distribution pools
                color_random = random.random(0, len(color_pool))
                color_select = color_pool[color_random]
                multicolor = False
                rarity_random = random.random(0, len(rarity_pool))
                rarity_select = rarity_pool[rarity_random]
                type_random = random.random(0, len(type_pool))
                type_select = type_pool[type_random]
                # Prepare to track whether the card meets the criterion
                approve = {'color':False,
                           'rarity':False,
                           'type':False}
                if not self.color_bool:
                    approve['color'] = True
                if not self.rarity_bool:
                    approve['rarity'] = True
                if not self.type_bool:
                    approve['type'] == True
                # Track if a card was added to the pack this iteration
                success = False
                # Type check the variables
                if cube.type() ==  'roper.Cube' and rare.type() == bool:
                    # Rarity, type, and color constraints
                    if rare and ratio_c and ratio_t:
                        # Read the cube file
                        if self.debug:
                            print('Reading Cube().')
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            # Line by line
                            for line in cube:
                                if self.debug:
                                    print('Reading card:')
                                # Turn the line into a list of str objects, comma delineated
                                card = cube.readline()
                                ## Make sure the card meets the random selection criterion
                                # Check for color_select to roll multicolored
                                if color_select != 'mc':
                                    # Check if the three selections are in the current line
                                    if color_select and type_select and rarity_select in card:
                                        # Check if the color is allowed by distribution constraints
                                        for key in self.color_pool.keys():
                                            if card[10] in self.color_pool:
                                                if self.debug:
                                                    print('Validating card color.')
                                                if self.color_dis[key]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for key in self.type_pool.keys():
                                            if card[77] in type_pool:
                                                if self.debug:
                                                    print('Validating card type.')
                                                if type_dis[key]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for key in self.rarity_pool.keys():
                                            if card[64] in self.rarity_pool:
                                                if self.debug:
                                                    print('Validating card rarity.')
                                                if rarity_dis[key]:
                                                    pass
                                                else:
                                                    approve['rarity'] = True
                                        # Track if the card was approved by the distribution constraints
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        # Increase the appropriate counter if the card was approved, add it to the pack, then mark success True
                                        if approval:
                                            self.color_counter[card[10]] += 1
                                            self.rarity_counter[card[64]] += 1
                                            for key in self.type_counter.keys():
                                                if key in card[77]:
                                                    self.type_counter[key] += 1
                                            self.add_card(card)
                                            success = True   
                                # Run multicolored verifications
                                elif color_select == 'mc':
                                    if 'mc' in self.color_pool:
                                        if card[10] in self.cube.mc:
                                            if self.debug:
                                                print('Validating card color.')
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for key in self.type_pool.keys():
                                            if card[77] in type_pool:
                                                if self.debug:
                                                    print('Validating card type.')
                                                if type_dis[key]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for key in self.rarity_pool.keys():
                                            if card[64] in self.rarity_pool:
                                                if self.debug:
                                                    print('Validating card rarity.')
                                                if rarity_dis[key]:
                                                    pass
                                                else:
                                                    approve['rarity'] = True
                                        # Track if the card was approved by the distribution constraints
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        # Increase the appropriate counter if the card was approved, add it to the pack, then mark success True
                                        if approval:
                                            self.color_counter['mc'] += 1
                                            self.rarity_counter[card[64]] += 1
                                            for key in self.type_counter.keys():
                                                if key in card[77]:
                                                    self.type_counter[key] += 1
                                            self.add_card(card)
                                            success = True
                            cube.close()
                    ## Rarity and type constraints
                    elif rare and not ratio_c and ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if rarity_select and type_select in card:
                                    for key in self.type_pool.keys():
                                        if card[77] in type_pool:
                                            if self.debug:
                                                print('Validating card type.')
                                            if type_dis[key]:
                                                pass
                                            else:
                                                approve['type'] = True
                                    for key in self.rarity_pool.keys():
                                        if card[64] in self.rarity_pool:
                                            if self.debug:
                                                print('Validating card rarity.')
                                            if rarity_dis[key]:
                                                pass
                                            else:
                                                approve['rarity'] = True
                                    approval = (approve['color'] and
                                                approve['type'] and
                                                approve['rarity'])
                                    if approval:
                                        self.rarity_counter[card[64]] += 1
                                        for key in self.type_counter.keys():
                                            if key in card[77]:
                                                self.type_counter[key] += 1
                                        self.add_card(card)
                                        success = True  
                            cube.close()
                    ## Rarity and color constraints
                    elif rare and ratio_c and not ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if color_select != 'mc':
                                    if rarity_select and color_select in card:
                                        for key in self.color_pool.keys():
                                            if card[10] in self.color_pool:
                                                if self.debug:
                                                    print('Validating card color.')
                                                if self.color_dis[key]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                            elif card[10] in self.cube.mc:
                                                if self.debug:
                                                    print('Validating card color.')
                                                if self.color_dis['mc']:
                                                    pass
                                                else:
                                                    multicolor = True
                                                    approve['color'] = True
                                        for key in self.rarity_pool.keys():
                                            if card[64] in self.rarity_pool:
                                                if self.debug:
                                                    print('Validating card rarity.')
                                                if rarity_dis[key]:
                                                    pass
                                                else:
                                                    approve['rarity'] = True
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        if approval:
                                            if multicolor:
                                                self.color_counter['mc'] += 1
                                            else:
                                                self.color_counter[card[10]] += 1
                                            self.rarity_counter[card[64]] += 1
                                            self.add_card(card)
                                            success = True  
                                # Run multicolored verifications
                                elif color_select == 'mc':
                                    if 'mc' in self.color_pool:
                                        if card[10] in self.cube.mc:
                                            if self.debug:
                                                print('Validating card color.')
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for key in self.rarity_pool.keys():
                                            if card[64] in self.rarity_pool:
                                                if self.debug:
                                                    print('Validating card rarity.')
                                                if rarity_dis[keys]:
                                                    pass
                                                else:
                                                    approve['rarity'] = True
                                        # Track if the card was approved by the distribution constraints
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        # Increase the appropriate counter if the card was approved, add it to the pack, then mark success True
                                        if approval:
                                            self.color_counter['mc'] += 1
                                            self.rarity_counter[card[64]] += 1
                                            for key in self.type_counter.keys():
                                                if key in card[77]:
                                                    self.type_counter[key] += 1
                                            self.add_card(card)
                                            success = True
                            cube.close()
                    ## Color and type Restraints
                    elif not rare and ratio_c and ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if color_select != 'mc':
                                    if color_select and type_select in card:
                                        for key in self.color_pool.keys():
                                            if card[10] in self.color_pool:
                                                if self.debug:
                                                    print('Validating card color.')
                                                if self.color_dis[key]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                            elif card[10] in self.cube.mc:
                                                if self.debug:
                                                    print('Validating card color.')
                                                if self.color_dis['mc']:
                                                    pass
                                                else:
                                                    multicolor = True
                                                    approve['color'] = True
                                        for key in self.type_pool.keys():
                                            if card[77] in type_pool:
                                                if self.debug:
                                                    print('Validating card type.')
                                                if type_dis[key]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        if approval:
                                            if multicolor:
                                                self.color_counter['mc'] += 1
                                            else:
                                                self.color_counter[card[10]] += 1
                                            for key in self.type_counter.keys():
                                                if key in card[77]:
                                                    self.type_counter[key] += 1
                                            self.add_card(card)
                                            success = True  
                                # Run multicolored verifications
                                elif color_select == 'mc':
                                    if 'mc' in self.color_pool.keys():
                                        if card[10] in self.cube.mc:
                                            if self.debug:
                                                print('Validating card color.')
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for key in self.type_pool.keys():
                                            if card[77] in self.type_pool:
                                                if self.debug:
                                                    print('Validating card type.')
                                                if type_dis[key]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        # Track if the card was approved by the distribution constraints
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        # Increase the appropriate counter if the card was approved, add it to the pack, then mark success True
                                        if approval:
                                            self.color_counter['mc'] += 1
                                            self.rarity_counter[card[64]] += 1
                                            for key in self.type_counter.keys():
                                                if key in card[77]:
                                                    self.type_counter[key] += 1
                                            self.add_card(card)
                                            success = True
                            cube.close()
                    ## Color constraints only
                    elif not rare and ratio_c and not ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if color_select != 'mc':
                                    if color_select in card:
                                        for key in self.color_pool.keys():
                                            if card[10] in self.color_pool:
                                                if self.debug:
                                                    print('Validating card color.')
                                                if self.color_dis[key]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                            elif card[10] in self.cube.mc:
                                                if self.debug:
                                                    print('Validating card color.')
                                                if self.color_dis['mc']:
                                                    pass
                                                else:
                                                    multicolor = True
                                                    approve['color'] = True
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        if approval:
                                            if multicolor:
                                                self.color_counter['mc'] += 1
                                            else:
                                                self.color_counter[card[10]] += 1
                                            self.add_card(card)
                                            success = True
                                # Run multicolored verifications
                                elif color_select == 'mc':
                                    if 'mc' in self.color_pool:
                                        if card[10] in self.cube.mc:
                                            if self.debug:
                                                print('Validating card color.')
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for key in self.type_pool:
                                            if card[77] in type_pool:
                                                if self.debug:
                                                    print('Validating card type.')
                                                if type_dis[key]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for key in self.rarity_pool.keys():
                                            if card[64] in self.rarity_pool:
                                                if self.debug:
                                                    print('Validating card rarity.')
                                                if rarity_dis[key]:
                                                    pass
                                                else:
                                                    approve['rarity'] = True
                                        # Track if the card was approved by the distribution constraints
                                        approval = (approve['color'] and
                                                    approve['type'] and
                                                    approve['rarity'])
                                        # Increase the appropriate counter if the card was approved, add it to the pack, then mark success True
                                        if approval:
                                            self.color_counter['mc'] += 1
                                            self.rarity_counter[card[64]] += 1
                                            for key in self.type_counter.keys():
                                                if key in card[77]:
                                                    self.type_counter[key] += 1
                                            self.add_card(card)
                                            success = True
                            cube.close()
                    ## Type constraints only
                    elif not rare and not ratio_c and ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if type_select in card:
                                    for key in self.type_pool.keys():
                                        if card[77] in type_pool:
                                            if self.debug:
                                                print('Validating card type.')
                                            if type_dis[key]:
                                                pass
                                            else:
                                                approve['type'] = True
                                    approval = (approve['color'] and
                                                approve['type'] and
                                                approve['rarity'])
                                    if approval:
                                        for key in self.type_counter.keys():
                                            if key in card[77]:
                                                self.type_counter[key] += 1
                                        self.add_card(card)
                                        success = True  
                            cube.close()
                    ## No distribution constraints, fairly resource intensive
                    elif not rare and not ratio_c and not ratio_t:
                        random = random.random(0, len(cards))
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            if card == cards[random]:
                                self.add_card(card)
                                success = True
                            cube.close()
                else:
                    raise TypeError('pack.generate() was passed an incorrect argument type')
                self.get_color_bool()
                self.get_rarity_bool()
                self.get_type_bool()
                if success:
                    num+=1

    def get_color_bool(self):
        """Return True if color constraint met."""
        if self.debug:
            print('Getting status of Color constraint flags.')
        for key in self.color_dis.keys():
            if self.color_counter[key] >= self.color_ratio_min and self.color_counter[key] <= color_ratio_max:
                self.color_dis[key] = True
            else:
                pass
        for key in self.color_dis.keys():
            if self.color_dis[key] == False:
                return False
        return True

    def get_rarity_bool(self):
        """Return True if rarirty constraint met."""
        if self.debug:
            print('Getting status of Rarity constraint flags.')
        if self.rarity_counter['common'] == self.common_card_ratio:
            self.rarity_dis['common'] = True
        if self.rarity_counter['uncommon'] == self.uncommon_card_ratio:
            self.rarity_dis['uncommon'] = True
        if self.rarity_counter['mythicrare'] == self.mythicrare_card_ratio:
            self.rarity_dis['mythicrare'] = True
        for key in self.rarity_dis.keys():
            if self.rarity_dis[key] == False:
                return False
        return True

    def get_type_bool(self):
        """Return True if type constraint met."""
        if self.debug:
            print('Getting status of Type constraint flags.')
        if self.type_counter['creature'] >= self.creature_card_ratio_min:
            self.type_dis['Creature'] = True
        if self.type_counter['Instant'] >= self.instant_ratio_min:
            self.type_dis['Instant'] = True
        if self.type_counter['Sorcery'] >= self.sorcery_ratio_min:
            self.type_dis['Sorcery'] = True
        for key in self.type_dis.keys():
            if self.type_dis[key] == False:
                return False
        return True

    def list_cards(self, sorted=False):
        """List cards in Pack.pack_list by Name, Color, and Type info.
        Pass sorted=True to the method to list the cards by their sorted
        values."""
        if self.debug:
            print('Listing cards in Pack():')
        with open(self.path, 'r', encoding='utf-8', newline='') as pack:
            for line in pack:
                line = pack.readline()
                print('name:'+line[52]+', '+'color(s):'+line[10]+', '+'type:'+line[77])

    def list_sort(self):
        """Sort Pack.pack_list by rarity to display."""
        # Create separate lists of cards by rarity then populate
        common = []
        uncommon = []
        rare = []
        mythic =[]
        if self.debug:
            print('Sorting cards in Pack().packlist.')
        with open(self.path, 'r', encoding='utf-8') as cards:
            for cid in self.cube_list:
                # Check the rarity of each card and append it to the appropriate list
                    for num in range(len(cards)):
                        line = cards.readline()
                        if cid in line and line[64] == 'common':
                            common.append(cid)
                        elif cid in line and line[64] == 'uncommon':
                            uncommon.append(cid)
                        elif cid in line and line[64] == 'rare':
                            rare.append(cid)
                        elif cid in line and line[64] == 'mythic':
                            mythic.append(cid)
                        else:
                            pass
        self.sorted_list['common']: common
        self.sorted_list['uncommon']: uncommon
        self.sorted_list['rare']: rare
        self.sorted_list['mythic']: mythic
        return self.sorted_list
        
    def remove_card(self, card_id):
        """Remove card from the Pack.pack_list, Pack.sorted_list,
        and the Pack.filepath. card_id should be card UUID."""
        if self.debug:
            print(f'Removing {card} from Pack().')
        for cid in self.pack_list:
            if card_id == cid:
                self.pack_list.remove(cid)
        return self.pack_list

    def replace_card(self, *kwargs):
        """Replace one card with another, using UUIDs to identify
        both the target and the replacement."""
        if self.debug:
            print('Replacing target cards with replacement cards.')
        for num in range(len(self.replace_card[args])):
            for cid in self.pack_list:
                if cid == n[num]:
                    self.remove_card(cid)
                else:
                    self.add_card(cid)
        return self.pack_list
