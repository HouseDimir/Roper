##                        cards_dict = cube.list_sort()
##                        common_len = len(cards_dict['common'].items())
##                        uncommon_len = len(cards_dict['uncommon'].items())
##                        mythicrare = []
##                        mythicrare.append(cube.sorted_list['mythic'], cube.sorted_list['rare'])
##                        mr_len = len(mythicrare)
##                        for n in range(15):
##                            if n >= 10:
##                                pick = random.random(0, common_len)
##                                with open(self.path, 'w', encoding='utf-8') as pack:
##                                    with open(cube.path, 'r', encoding='utf-8') as cube:
##                                         for l in cube:
##                                            l = cube.readline()
##                                            if cards_dict['common'][pick] in l and l[64] == 'common':
##                                                pack.write(l)
##                                                pack.flush()
##                                                pack.close()
##                                        cube.close()
##                                    pack.close()
##                            elif n <= 10 and n >= 14:
##                                pick = random.random(0, uncommon_len)
##                                with open(self.path, 'w', encoding='utf-8') as pack:
##                                    with open(cube.path, 'r', encoding='utf-8') as cube:
##                                         for l in cube:
##                                            l = cube.readline()
##                                             if cards_list[pick] in l and l[64] == 'uncommon':
##                                                pack.write(l)
##                                                pack.flush()
##                                                pack.close()
##                                        cube.close()
##                                    pack.close()
##                            elif n = 15:
##                                pick = random.random(0, mr_len)
##                                with open(self.path, 'w', encoding='utf-8') as pack:
##                                    with open(cube.path, 'r', encoding='utf-8') as cube:
##                                         for l in cube:
##                                            l = cube.readline()
##                                            mr = True if l[64] == 'rare' or l[64] == 'mythic' else False
##                                            if cards_list[pick] in l and mr:
##                                                pack.write(l)
##                                                pack.flush()
##                                                pack.close()
##                                        cube.close()
##                                    pack.close()
##                    while not rare:
##                        #dump 15 random cards into a list
##                        cards_list = cube.cube_list
##                        p = len(cards_list)
##                        for n in range(15):
##                            pick = random.random(0, p)
##                            with open(self.path, 'w', encoding='utf-8') as pack:
##                                with open(cube.path, 'r', encoding='utf-8') as cube:
##                                    for l in cube:
##                                        l = cube.readline()
##                                        if cards_list[pick] in l:
##                                            pack.write(l)
##                                            pack.flush()
##                                            pack.close()
##                                    cube.close()
##                                pack.close()
