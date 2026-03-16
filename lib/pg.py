import os
import st
import random

source_list = [
    'bin/cards_black.csv',
    'bin/cards_blue.csv',
    'bin/cards_colorless.csv',
    'bin/cards_green.csv',
    'bin/cards_multicolor.csv',
    'bin/cards_nbl.csv',
    'bin/cards_red.csv',
    'bin/cards_white.csv'
    ]

#UUIDs card[79]

##
#Prepare for consistent cube generation
class cube():
    def __init__(self, inst_id):
        self.inst_id = str('cube_', inst_id)
        self.path: str = path
        self.verfd: bool = False
        self.draft: bool = False
        self.populated: bool = False
        self.max_cards: int = 360
        self.max_packs: int = self.max_cards/15
        self.cube_list = []
        self.sorted_list = {}

    #Add card to the cube
    def add_card(self, card_id):
        self.cube_list.append(card_id)
        return self.cube_list

    #generate the cube_list to be sorted through by the pack generator as requested
    def generate(self, output):
        '''Iterate through card source files and create a list of all cards
        that match the supplied arguments.

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
        '''
        exclusive = False
        #Explicit type check all values
        if output not dict:
            raise TypeError(f"Improper argument type passed to _sourceIter(): "+output.type)
        elif k in output not str:
            raise TypeError(f"Improper argument typed passed from nParse.parse_input(): "+arg.type)
        else:
            #rework to respect exclusivity
            #Iterate across sorted card lists
            for i in source_list:
                i_path = str(cwd) + i
                with open(i_path, 'r', newline='', encoding='utf-8') as gen:
                    #Iterate over each card in each list
                    for r in gen:
                        if output['-excl']:
                            exclusive = True
                        if exclusive:
                            pass
                        k in output.keys():
                            #Compare arguments sorted into dicts; Key = str(kwarg) : Value = list(positional, args, space, deliniated)
                            if k == '-kw':
                                #Keywords r[44]
                                for arg_kw in output['-kw']:
                                    if arg_kw in r[44]:
                                        with open(str(cwd)+'bin/pcan.csv', 'w', newline='', encoding='utf8') as pcan:
                                                pcan.write(r)
                                                pcan.flush()
                                                pcan.close()
                            elif k == '-s':
                                #Set Codes r[68]
                                for arg_set in output['-s']:
                                    if arg_set in r[68]:
                                        with open(str(cwd)+'bin/pcan.csv', 'w', newline='', encoding='utf-8') as pcan:
                                            pcan.write(r)
                                            pcan.flush()
                                            pcan.close()
                            elif k == '-mv':
                                #Mana Value r[]
                                pass
                            elif k == '-gc':
                                #GameChanger r[33]
                                for arg_gc in output['-gc']:
                                    if arg_gc:
                                        if r[33]:
                                            with open(str(cwd)+'bin/pcan.csv', 'w', newline='', encoding='utf8') as pcan:
                                                pcan.write(r)
                                                pcan.flush()
                                                pcan.close()
                            elif k == '-subt':
                                #Subtype r[]
                                pass
                            elif k == '-supt':
                                #Supertype r[]
                                pass
                            elif k == '-t':
                                #Type r[77]
                                for arg_t in output['-t']:
                                    if arg_t in r[77]:
                                        with open(str(cwd)+'bin/pcan.csv', 'w', newline='', encoding='utf-8') as pcan:
                                            pcan.write(r)
                                            pcan.flush()
                                            pcan.close()
                            else:
                                #Handle unexpected kwargs
                                return ValueError("Cubitrice did not recognize the argument you passed "+str(arg))
                else:
                    raise ValueError(f'Incorrect command passed to {self}.generate()')
        self.populated = True
        return self.populated

    #List the various cards in the cube
    def list_cards(self):
        with open(self.path, 'r', encoding='utf-8', newline='') as cube:
            for line in cube:
                line = pack.readline()
                print('name: '+line[52]+', '+'color(s): '+line[10]+', '+'type: '+line[77])

    #cube_list sorting by rarity, then alphabetical
    def list_sort(self):
        #Create separate lists of cards by rarity then populate
        common = []
        uncommon = []
        rare = []
        mythic =[]
        with open(self.path, 'r', encoding='utf-8') as cards:
            for cid in self.cube_list:
                #check the rarity of each card and append it to the appropriate list
                    for n in range(len(cards)):
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

    #Remove cards from the pack card list
    def remove_card(self, card_id):
        for cid in self.cube_list:
            if card_id == cid:
                self.cube_list.remove(cid)
        return self.cube_list

    #Select the relevant card(s) by cardID and replace it with the next cardID, repeat for each pair 
    def replace_card(self, [name1, replace1], [name2, replace2], *args):
        for n in range(len(self.replaceCard[args])):
            for cid in self.cube_list:
                if cid == n[n]:
                    self.remove_card(cid)
                else:
                    self.add_card(cid)
        return self.cube_list
##


##
#Prepare for consistent pack generation across many iterations
class pack():
    def __init__(self, inst_id):
        self.inst_id = str('pack_', inst_id)
        self.path: str = path
        self.verfd: bool = False
        self.draft: bool = True
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
        self.pack_list = []
        self.sorted_list = []
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

    #Add card to the pack list using cardID
    def add_card(self, card):
            with open(self.path, 'w', encoding='utf-8') as pack:
                pack.write(card)
                pack.flush()
                pack.close()
            self.pack_list.append(card[79])            
            return self.pack_list

    #Generate the pack randomly from the assigned cube
    def generate(self, cube, rare, ratio_c, ratio_t):
        #cube should be class cube() object, rare should be bool, ratio_c should be bool, ratio_t should be bool
        #reset counters
        n = 0
        for k in self.color_counter:
            self.color_counter[k] = 0
        for k in self.rarity_counter:
            self.self.rarity_counter[k]
        for k in type_counter:
            self.type_counter[k] = 0
        #toggle distribution verification flags
        if not rare:
            self.rarity_bool = True
        if not ratio_c:
            self.color_bool = True
        if not ratio_t:
            self.type_bool = True
        #random pack generation resource population
        if self.color_bool and self.rarity_bool and self.type_bool:
            with open(self.cube.path,  'r', encoding='utf-8') as cube:
                cards = []
                for line in cube:
                    card = cube.readline()
                    cards.append(card)
                cube.close()
        #run until all constraints flags true
        while not color_bool or not type_bool or not rare_bool:
            while not n = self.max_cards:
                #distribution state checks
                if not self.color_bool:
                    
                #variables repeated each card pull iteration
                common = (True if n<=common_counter_ratio else False)
                uncommon = (True if n<=uncommon_counter_ratio and n>= common_counter_ratio else False)
                mythicrare = (True if n<=1 and n>=mythicrare_counter_ratio)
                color_random = random.random(0, len(color_pool))
                color_select = color_pool[color_random]
                multicolor = False
                rarity_random = random.random(0, len(rarity_pool))
                rarity_select = rarity_pool[rarity_random]
                type_random = random.random(0, len(type_pool))
                type_select = type_pool[type_random]
                approve = {'color':False,
                           'rarity':False,
                           'type':False}
                if not self.color_bool:
                    approve['color'] = True
                if not self.rarity_bool:
                    approve['rarity'] = True
                if not self.type_bool:
                    approve['type'] == True
                success = False
                #type check the variables
                if cube.type() == 'class pg.cube' and rare.type() == bool:
                    #Rarity, Type, and Color Constraints
                    if rare and ratio_c and ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if color_select and type_select and rarity_select in card:
                                    for k in self.color_pool:
                                        if card[10] in self.color_pool:
                                            if self.color_dis[k]:
                                                pass
                                            else:
                                                approve['color'] = True
                                        elif card[10] in st.mc:
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
                                        for k in self.type_counter:
                                            if k in card[77]:
                                                self.type_counter[k] += 1
                                        self.add_card(card)
                                        success = True   
                            cube.close()
                    #Rarity and Type Constraints
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
                    #Rarity and Color Constraints
                    elif rare and ratio_c and not ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if rarity_select and color_select in card:
                                    for k in self.color_pool:
                                        if card[10] in self.color_pool:
                                            if self.color_dis[k]:
                                                pass
                                            else:
                                                approve['color'] = True
                                        elif card[10] in st.mc:
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
                            cube.close()
                    #Color and Type Restraints
                    elif not rare and ratio_c and ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if color_select and type_select in card:
                                    for k in self.color_pool:
                                        if card[10] in self.color_pool:
                                            if self.color_dis[k]:
                                                pass
                                            else:
                                                approve['color'] = True
                                        elif card[10] in st.mc:
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
                            cube.close()
                    #Color Constraints only
                    elif not rare and ratio_c and not ratio_t:
                        with open(self.cube.path, 'r', encoding='utf-8') as cube:
                            for line in cube:
                                card = cube.readline()
                                if color_select in card:
                                    for k in self.color_pool:
                                        if card[10] in self.color_pool:
                                            if self.color_dis[k]:
                                                pass
                                            else:
                                                approve['color'] = True
                                        elif card[10] in st.mc:
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
                            cube.close()
                    #Type Constraints only
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
                    #No Distribution Constraints, fairly resource intensive
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
            
    #Return True if color constraint met
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

    #return true if rarirty constraint met
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

    #Return True if type constraint met
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

    #Count and display some identifying information about the packs generated
    def list_cards(self):
        with open(self.path, 'r', encoding='utf-8', newline='') as pack:
            for line in pack:
                line = pack.readline()
                print('name:'+line[52]+', '+'color(s):'+line[10]+', '+'type:'+line[77])

    #packList sorting by rarity, then alphabetical
    def list_sort(self):
        pass
        #Create separate lists of cards by rarity then populate
        common = []
        uncommon = []
        rare = []
        mythic =[]
        with open(self.path, 'r', encoding='utf-8') as cards:
            for cid in self.cube_list:
                #check the rarity of each card and append it to the appropriate list
                    for n in range(len(cards)):
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
        
    #Remove cards from the pack card list
    def remove_card(self, card_id):
        for cid in self.pack_list:
            if card_id == cid:
                self.pack_list.remove(cid)
        return self.pack_list

    #Select the relevant card(s) by cardID and replace it with the next cardID, repeat for each pair 
    def replace_card(self, [name1, replace1], [name2, replace2], *args):
        for n in range(len(self.replace_card[args])):
            for cid in self.pack_list:
                if cid == n[n]:
                    self.remove_card(cid)
                else:
                    self.add_card(cid)
        return self.pack_list
##
