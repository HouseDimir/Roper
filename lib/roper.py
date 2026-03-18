import os
import re
import nput
import random
import smartjack

#UUIDs card[79]

##
# Prepare for consistent cube generation
class cube():
    def __init__(self, inst_id):
        # Basic identifying information
        self.inst_id = str('cube_', inst_id)
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
        self.bl = []
        self.gl = []
        self.ll = []
        self.ml = []
        self.rl = []
        self.ul = []
        self.wl = []
        self.xl = []
        self.lc = [bl, gl, ll, ml, rl, ul, wl, xl]
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
        self.bfp = str(cwd) + '/bin/cards_black.csv' 
        self.gfp = str(cwd) + '/bin/cards_green.csv'
        self.lfp = str(cwd) + '/bin/cards_nbl.csv'
        self.mfp = str(cwd) + '/bin/cards_multi.csv'
        self.rfp = str(cwd) + '/bin/cards_red.csv'
        self.ufp = str(cwd) + '/bin/cards_blue.csv'
        self.wfp = str(cwd) + '/bin/cards_white.csv'
        self.xfp = str(cwd) + '/bin/cards_colorless.csv'
        self.sl = [bfp, gfp, lfp, mfp, rfp, ufp, wfp, xfp]

    # Add card to the cube path file and card UUID to cube.cube_list
    def add_card(self, card):
        with open(self.path, 'w', encoding='utf-8') as cube:
            cube.write(card)
        self.cube_list.append(card[79])
        return

    # Generate the cube_list to be sorted through by the pack generator as requested
    def generate(self, output):
        """Iterate through card source files and create a list of all cards
        that match the supplied arguments."""
        exclusive = False
        # Explicit type check all values
        if output not dict:
            raise TypeError(f"Improper argument type passed to _sourceIter(): "+output.type)
        elif k in output not str:
            raise TypeError(f"Improper argument typed passed from nParse.parse_input(): "+arg.type)
        else:
            # Iterate across sorted card lists
            for i in source_list:
                i_path = str(cwd) + i
                with open(i_path, 'r', newline='', encoding='utf-8') as source:
                    # Iterate over each card in each list
                    for card in source:
                        operand = ''
                        if '-excl' in output.keys():
                            excl = True
                        if excl:
                            # Exclusivity handling
                            pass
                        if k == '-gc':
                            # GameChanger card[33]
                            pass
                        for  k in output.keys():
                            # Compare arguments sorted into dicts; Key = str(kwarg) : Value = list(positional, args, space, deliniated)
                            if k == '-kw':
                                # Keywords card[44]
                                for arg_kw in output['-kw']:
                                    if arg_kw in card[44]:
                                        self.add_card(card)
                            elif k == '-s':
                                # Set codes card[68]
                                for arg_set in output['-s']:
                                    if arg_set in card[68]:
                                        self.add_card(card)
                            elif k == '-mv':
                                # Mana value card[51]
                                for v in output['-mv']:
                                    try int(v):
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
                            elif k == '-subt':
                                # Subtype card[73]
                                pass
                            elif k == '-supt':
                                # Supertype card[74]
                                pass
                            elif k == '-t':
                                # Type card[77]
                                for arg_t in output['-t']:
                                    if arg_t in r[77]:
                                        self.add_card(card)
                            else:
                                # Handle unexpected kwargs
                                return ValueError("Cubitrice did not recognize the argument you passed "+str(arg))
                else:
                    raise ValueError(f'Incorrect command passed to {self}.generate()')
        if len(self.cube_list) > self.max_cards:
            self.purge = True
        self.populated = True
        return

    # List the various cards in the cube
    def list_cards(self):
        with open(self.path, 'r', encoding='utf-8', newline='') as cube:
            for line in cube:
                line = pack.readline()
                print('name: '+line[52]+', '+'color(s): '+line[10]+', '+'type: '+line[77])

    # Sorting list of cards by rarity, then alphabetical
    def list_sort(self):
        # Create separate lists of cards by rarity then populate
        common = []
        uncommon = []
        rare = []
        mythic =[]
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

    # Remove cards from the cube card list, cube sorted list, and cube path file
    def remove_card(self, card_id):
        # Init list to track all cards from cube.path file
        cards = []
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

    # Select the relevant card(s) by cardID and replace it with the next cardID, repeat for each pair 
    def replace_card(self, [name1, replace1], [name2, replace2], *args):
        for num in range(len(self.replaceCard[args])):
            for cid in self.cube_list:
                # Rework this????
                #
                #
                #
                if cid == n[num]:
                    self.remove_card(cid)
                else:
                    self.add_card(cid)
        return self.cube_list

    def source_sort(self, source_path):
        # Counts each iteration when sorting the cards into the respective files
        rc = 0
        # Opens and loads the csv into a nested set of lists to process
        try:
            with open(source_path, 'r', newline='', encoding='utf-8') as cards:
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
        # Exception handling to ensure there is a file for the cards to go to                    
        except FileNotFoundError:
            # Some code that pulls the necessary card files
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
        # Check to see if the named files exist and deletes them before proceeding
        for num in range(len(sl)):
            p = sl[num]
            l = lc[num]
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
##


##
# Prepare for consistent pack generation across many iterations
class pack():
    def __init__(self, inst_id):
        # Basic identifying information
        self.inst_id = str('pack_', inst_id)
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

    # Add card to the pack file and list. card must be open.readline() object from csv file
    def add_card(self, card):
            with open(self.path, 'w', encoding='utf-8') as pack:
                pack.write(card)
                pack.flush()
                pack.close()
            self.pack_list.append(card[79])            
            return self.pack_list

    # Generate the pack randomly from the assigned cube.
    def generate(self, cube, rare, ratio_c, ratio_t):
        # Cube should be class cube() object, rare should be bool, ratio_c should be bool, ratio_t should be bool
        # Reset counters
        num = 0
        for k in self.color_counter:
            self.color_counter[k] = 0
        for k in self.rarity_counter:
            self.self.rarity_counter[k]
        for k in type_counter:
            self.type_counter[k] = 0
        # Toggle distribution verification flags
        if not rare:
            self.rarity_bool = True
        if not ratio_c:
            self.color_bool = True
        if not ratio_t:
            self.type_bool = True
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
                if cube.type() ==  'roper.cube' and rare.type() == bool:
                    # Rarity, type, and color constraints
                    if rare and ratio_c and ratio_t:
                        # Read the cube file
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            # Line by line
                            for line in cube:
                                # Turn the line into a list of str objects, comma delineated
                                card = cube.readline()
                                ## Make sure the card meets the random selection criterion
                                # Check for color_select to roll multicolored
                                if color_select != 'mc':
                                    # Check if the three selections are in the current line
                                    if color_select and type_select and rarity_select in card:
                                        # Check if the color is allowed by distribution constraints
                                        for k in self.color_pool:
                                            if card[10] in self.color_pool:
                                                if self.color_dis[k]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for k in self.type_pool:
                                            if card[77] in type_pool:
                                                if type_dis[k]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for k in self.rarity_pool:
                                            if card[64] in self.rarity_pool:
                                                if rarity_dis[k]:
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
                                            for k in self.type_counter:
                                                if k in card[77]:
                                                    self.type_counter[k] += 1
                                            self.add_card(card)
                                            success = True   
                                # Run multicolored verifications
                                elif color_select == 'mc':
                                    if 'mc' in self.color_pool:
                                        if card[10] in self.cube.mc:
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for k in self.type_pool:
                                            if card[77] in type_pool:
                                                if type_dis[k]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for k in self.rarity_pool:
                                            if card[64] in self.rarity_pool:
                                                if rarity_dis[k]:
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
                                            for k in self.type_counter:
                                                if k in card[77]:
                                                    self.type_counter[k] += 1
                                            self.add_card(card)
                                            success = True
                            cube.close()
                    ## Rarity and type constraints
                    elif rare and not ratio_c and ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if rarity_select and type_select in card:
                                    for k in self.type_pool:
                                        if card[77] in type_pool:
                                            if type_dis[k]:
                                                pass
                                            else:
                                                approve['type'] = True
                                    for k in self.rarity_pool:
                                        if card[64] in self.rarity_pool:
                                            if rarity_dis[k]:
                                                pass
                                            else:
                                                approve['rarity'] = True
                                    approval = (approve['color'] and
                                                approve['type'] and
                                                approve['rarity'])
                                    if approval:
                                        self.rarity_counter[card[64]] += 1
                                        for k in self.type_counter:
                                            if k in card[77]:
                                                self.type_counter[k] += 1
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
                                        for k in self.color_pool:
                                            if card[10] in self.color_pool:
                                                if self.color_dis[k]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                            elif card[10] in self.cube.mc:
                                                if self.color_dis['mc']:
                                                    pass
                                                else:
                                                    multicolor = True
                                                    approve['color'] = True
                                        for k in self.rarity_pool:
                                            if card[64] in self.rarity_pool:
                                                if rarity_dis[k]:
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
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for k in self.rarity_pool:
                                            if card[64] in self.rarity_pool:
                                                if rarity_dis[k]:
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
                                            for k in self.type_counter:
                                                if k in card[77]:
                                                    self.type_counter[k] += 1
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
                                        for k in self.color_pool:
                                            if card[10] in self.color_pool:
                                                if self.color_dis[k]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                            elif card[10] in self.cube.mc:
                                                if self.color_dis['mc']:
                                                    pass
                                                else:
                                                    multicolor = True
                                                    approve['color'] = True
                                        for k in self.type_pool:
                                            if card[77] in type_pool:
                                                if type_dis[k]:
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
                                            for k in self.type_counter:
                                                if k in card[77]:
                                                    self.type_counter[k] += 1
                                            self.add_card(card)
                                            success = True  
                                # Run multicolored verifications
                                elif color_select == 'mc':
                                    if 'mc' in self.color_pool:
                                        if card[10] in self.cube.mc:
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for k in self.type_pool:
                                            if card[77] in type_pool:
                                                if type_dis[k]:
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
                                            for k in self.type_counter:
                                                if k in card[77]:
                                                    self.type_counter[k] += 1
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
                                        for k in self.color_pool:
                                            if card[10] in self.color_pool:
                                                if self.color_dis[k]:
                                                    pass
                                                else:
                                                    approve['color'] = True
                                            elif card[10] in self.cube.mc:
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
                                            if self.color_dis['mc']:
                                                pass
                                            else:
                                                multicolor = True
                                                approve['color'] = True
                                        # Check if the type is allowed by distribution constraints
                                        for k in self.type_pool:
                                            if card[77] in type_pool:
                                                if type_dis[k]:
                                                    pass
                                                else:
                                                    approve['type'] = True
                                        # Check if the rarity is allowed by distribution constraints
                                        for k in self.rarity_pool:
                                            if card[64] in self.rarity_pool:
                                                if rarity_dis[k]:
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
                                            for k in self.type_counter:
                                                if k in card[77]:
                                                    self.type_counter[k] += 1
                                            self.add_card(card)
                                            success = True
                            cube.close()
                    ## Type constraints only
                    elif not rare and not ratio_c and ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if type_select in card:
                                    for k in self.type_pool:
                                        if card[77] in type_pool:
                                            if type_dis[k]:
                                                pass
                                            else:
                                                approve['type'] = True
                                    approval = (approve['color'] and
                                                approve['type'] and
                                                approve['rarity'])
                                    if approval:
                                        for k in self.type_counter:
                                            if k in card[77]:
                                                self.type_counter[k] += 1
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
                    n+=1
            
    # Return true if color constraint met
    def get_color_bool(self):
        for k in self.color_dis:
            if self.color_counter[k] >= self.color_ratio_min and <= color_ratio_max:
                self.color_dis[k] = True
            else:
                pass
        for key in self.color_dis.keys():
            if self.color_dis[key] == False:
                return False
        return True

    # Return true if rarirty constraint met
    def get_rarity_bool(self):
        if self.rarity_counter['common'] == self.common_card_ratio:
            self.rarity_dis['common'] = True
        if self.rarity_counter['uncommon'] == self.uncommon_card_ratio:
            self.rarity_dis['uncommon'] = True
        if self.rarity_counter['mythicrare'] == self.mythicrare_card_ratio:
            self.rarity_dis['mythicrare'] = True
        for k in self.rarity_dis.keys():
            if self.rarity_dis[k] == False:
                return False
        return True

    # Return true if type constraint met
    def get_type_bool(self):
        if self.type_counter['creature'] >= self.creature_card_ratio_min:
            self.type_dis['Creature'] = True
        if self.type_counter['Instant'] >= self.instant_ratio_min:
            self.type_dis['Instant'] = True
        if self.type_counter['Sorcery'] >= self.sorcery_ratio_min:
            self.type_dis['Sorcery'] = True
        for k in self.type_dis.keys():
            if self.type_dis[k] == False:
                return False
        return True

    # Count and display some identifying information about the packs generated
    def list_cards(self):
        with open(self.path, 'r', encoding='utf-8', newline='') as pack:
            for line in pack:
                line = pack.readline()
                print('name:'+line[52]+', '+'color(s):'+line[10]+', '+'type:'+line[77])

    # PackList sorting by rarity, then alphabetical
    def list_sort(self):
        pass
        # Create separate lists of cards by rarity then populate
        common = []
        uncommon = []
        rare = []
        mythic =[]
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
        
    # Remove cards from the pack card list
    def remove_card(self, card_id):
        for cid in self.pack_list:
            if card_id == cid:
                self.pack_list.remove(cid)
        return self.pack_list

    # Select the relevant card(s) by cardID and replace it with the next cardID, repeat for each pair 
    def replace_card(self, [name1, replace1], [name2, replace2], *args):
        for num in range(len(self.replace_card[args])):
            for cid in self.pack_list:
                if cid == n[num]:
                    self.remove_card(cid)
                else:
                    self.add_card(cid)
        return self.pack_list
##
