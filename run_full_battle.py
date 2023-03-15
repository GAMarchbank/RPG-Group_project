import json
import random
import time
from statistics import mean


# hey guys. 
# run other_data_save_types.py first, it will create the necessary json files.
# the whole thing returns False if you lose and True if you win. 
# it saves all other data back to the player_data.txt file
# these used to be two files but ive combined them to upload here.
# when we use this in the program ill delect the final line where the code is called. 


# just an enemy example to run with the program
en_lst = [{"name": "Scorpion", "level": 2, "Location": "Desert", "items": ['great vibes'], "hp": 7, "a_p": 2, "d_p": 2, 's_p': 10, 'aim': 20, "attacks": ['Scratch'], 'personality': 'wild'}, {"name": "Scorpion", "level": 2, "Location": "Desert", "items": ['great vibes'], "hp": 7, "a_p": 2, "d_p": 2, 's_p': 10, 'aim': 20, "attacks": ['Scratch'], 'personality': 'average'}]

# this is the class which will be used to run both sides of the combat
class Battle_Class:
    def __init__(self, name, hp, ap, dp, sp, aim, items, attacks, max_hp, is_player, level, id_num = 0, personality = 0):
        self.name = name
        self.current_hp = hp
        self.max_hp = max_hp
        self.ap = ap
        self.dp = dp
        self.sp = sp
        self.aim = aim
        self.items = items
        self.attacks = attacks
        self.max_hp = hp
        self.effects_lst = []
        self.skip_go = False
        self.is_player = is_player
        self.personality = personality
        self.level = level
        self.status = 'alive'
        self.id_num = id_num
        
    
    # returns the status of the player
    def return_status(self):
        return self.status
    
    # sets the status of the player when it changes
    def set_status(self, opt):
        if opt == 1:
            self.status = 'escaped'
        if opt == 2:
            self.status = 'defeated'

    # returns the unique id number of the player
    def return_id_num(self):
        return self.id_num
    
    # returns the level of the player, used in the ai
    def return_level(self):
        return self.level

    # returns True if the combattee is the player
    def return_is_plyer(self):
        return self.is_player

    # returns max_hp as a value
    def return_max_hp(self):
        return self.max_hp
    
    # returns current hp as a value
    def return_hp(self):
        return self.current_hp
    
    # returns name as a value
    def return_name(self):
        return self.name
    
    # returns speed stat of the combatee
    def return_speed_no_edit(self):
        return self.sp
    
    # returns the speed stat of the combatee edited for in combat use
    def return_speed(self):
        if self.current_hp <= self.max_hp * 0.25:
            low_num = 10
            high_num = 3
        else:
            low_num = 5
            high_num = 5
        this_speed = random.randrange(self.sp-low_num, self.sp+high_num)
        return this_speed
    
    def escape_calc(self, speed):
        if self.current_hp <= self.max_hp * 0.25:
            low_num = 10
            high_num = 3
        else:
            low_num = 5
            high_num = 5
        this_speed = random.randrange(self.sp-low_num, self.sp+high_num)
        if this_speed >= speed:
            return False
        return True

    # saves the player data at the end of combat
    def exit_game_save(self):
        with open('player_data.txt', 'r')as file:
            file = file.read()
        player_data = json.loads(file)
        player_data['hp'] = self.current_hp
        player_data['items'] = self.items
        fil = json.dumps(player_data)
        with open('player_data.txt', 'w')as file:
            file.write(fil)
    
    # inacts teh effects of any status effects applied to the combatee
    # currently either skip go ['skip_go'], damage['damage', postive value] or health['damage', negative value] effects can be applied
    def action_events(self):
        self.skip_go = False
        if len(self.effects_lst) != 0:
            for items in self.effects_lst:
                if items['remaining turns'] == 0:
                    self.effects_lst.remove(items)
                else:
                    print(f"{items['remaining turns']} left of {items['name']}")
                    if items['effects']['type'] == 'damage':
                        self.current_hp -= items['effects']['impact']
                        print(f"{self.name} took {items['effects']['impact']} points of damage.")
                        if self.current_hp > self.max_hp:
                            self.current_hp = self.max_hp
                        elif self.current_hp < 0:
                            self.current_hp = 0
                    elif items['effects']['type'] == 'skip_go':
                        self.skip_go = True
                    items['remaining turns'] = items['remaining turns'] - 1
        if self.skip_go == True:
            return False
    
    # enermy picks an attack depending on its personality
    def gen_enermy_attack(self, personality):
        if personality in  ['timid', 'average', 'resourceful']:
            attack = random.choice(self.attacks)
            with open('game_data.txt', 'r') as file:
                game_data = file.read()
            game_data = json.loads(game_data)
            attack_data = game_data['attacks']
            for atta in attack_data:
                if attack == atta['name']:
                    return atta
        else:
            attack_lst = []
            with open('game_data.txt', 'r')as file:
                game_data = file.read()
            game_data = json.loads(game_data)
            attack_data = game_data['attacks']
            for atta in attack_data:
                for attack in self.attacks:
                    if attack == atta['name']:
                        attack_lst.append(atta)
            if personality in ['aggressive', 'wild']:
                sortation = []
                for atta in attack_lst:
                    sortation.append(atta['attack_modifer'])
                sortation = sorted(sortation, reverse=True)
                for attack in attack_lst:
                    if attack['attack_modifer'] == sortation[0]:
                        return attack
            elif personality == 'smart':
                sortation = []
                for atta in attack_lst:
                    if len(atta['effects']) != 0:
                        sortation.append(atta)
                if len(sortation) == 0:
                    chip = self.gen_enermy_attack('aggressive')
                else:
                    chip = random.choice(sortation)
                return chip
                 
        
    
    # lets the player choose what attack they want to use and returns the sepefic data for that attack
    def gen_player_attack(self):
        with open('game_data.txt', 'r') as file:
            game_data = file.read()
        game_data = json.loads(game_data)
        attack_data = game_data['attacks']
        while True:
            num = 1
            attack_dict = {}
            print('Select an attack.\n')
            for atta in attack_data:
                for attacks in self.attacks:
                    if attacks == atta['name']:
                        print(f"\t{num}\t{atta['name']}\n\t\tdesc:\t{atta['description']}\n\t\ttgt:\t{atta['mult_targets']}")
                        if atta['effects'] != None:
                            for items in game_data['effects']:
                                if atta['effects'] == items['name']:
                                    print(f"\t\teft:\t{items['name']}\n\t\t\t{items['description']}")
                        else:
                            pass
                        attack_dict[num] = atta
                        print('\n')
                        num += 1
            print("\tb:\tBack")
            attack_choice = input('Please make your selection?\t')
            try:
                if int(attack_choice) not in range(1, num):
                    print('Unrecognised entry')
                    continue
            except Exception:
                if attack_choice.lower() != 'b':
                    print('Unrecognised entry')
                    continue
            if attack_choice == 'b':
                return False
            print(f'\nyou have selected {attack_dict[int(attack_choice)]["name"]}.\n')
            while True:
                final_choice = input('Are you happy with this selection?\t')
                if final_choice.lower() not in ['y', 'yes', 'n', 'no']:
                    print('Unrecognised entry.')
                    continue
                break
            if final_choice.lower() in ['y', 'yes']:
                return attack_dict[int(attack_choice)]

    # generates teh attack damage and aim for an attack, these vary by enemy personality type
    def gen_attack_damage(self, attack_dic, personality = 'player'):
        print(f"{self.name} tries to use {attack_dic['name']}.")
        if personality in ['player', 'average', 'resourceful']:
            damage = self.ap * attack_dic['attack_modifer']
            damage = random.randrange(damage - 10, damage + 10)
            if damage < 0:
                damage = 0
            aim = random.randrange(self.aim - 5, self.aim + 5)
        elif personality == 'aggressive':
            damage = self.ap * (attack_dic['attack_modifer'] + 0.5 )
            damage = random.randrange(damage - 10, damage + 10)
            if damage < 0:
                damage = 0
            aim = random.randrange(self.aim - 5, self.aim +5)
        elif personality == 'wild':
            damage = self.ap * attack_dic['attack_modifer']
            damage = random.randrange(damage-25, damage + 25)
            if damage < 0:
                damage = 0
            aim = random.randrange(self.aim -10, self.aim +10)
        elif personality == 'smart':
            damage = self.ap * attack_dic['attack_modifer']
            damage = random.randrange(damage-5, damage+5)
            if damage < 0:
                damage = 0
            aim = random.randrange(self.aim -5, self.aim +15)
        elif personality == 'timid':
            damage = self.ap * attack_dic['attack_modifer']
            damage = random.randrange(damage -10, damage +15)
            if damage < 0:
                damage = 0
            aim = random.randrange(self.aim - 10, self.aim + 15)
        return {'damage': damage, 'aim': aim, 'attack_dic': attack_dic}
    
    # calculates weather and attack hits, then works out damage and effects
    def gen_defense(self, atk_dic):
        return_dic = {'damage': 0, 'effect': None}
        defense = random.randrange(self.dp - 10, self.dp + 10)
        if defense < 0:
            defense = 0
        speed = random.randrange(self.sp-10, self.sp+10)
        if atk_dic['aim'] >= speed:
            if atk_dic['damage'] >= defense * 1.5:
                return_dic['damage'] = round(atk_dic['damage'])
            elif atk_dic['damage'] == defense:
                return_dic['damage'] = round(atk_dic['damage'] *0.75)
            elif atk_dic['damage'] >= defense *0.5:
                return_dic['damage'] = round(atk_dic['damage'] * 0.5)
            else:
                return_dic['damage'] = round(atk_dic['damage'] *0.25)
            if atk_dic['attack_dic']['effects'] != None:
                if random.randrange(1, 3) == 1:
                    return_dic['effect'] = atk_dic['attack_dic']['effects']
            if return_dic['damage'] == 0 and return_dic['effect'] == None:
                return 'fail'
            return return_dic
        else:
            return False
    
    # this applies damage to the combatee, also applies effects if relivent
    def take_damage(self, attack_dic):
        effect_check = []
        if attack_dic['effect'] != None:
            with open('game_data.txt', 'r') as file:
                file = file.read()
            game_data = json.loads(file)
            for items in game_data['effects']:
                if attack_dic['effect'] == items['name']:
                    if items['effects']['type'] == 'skip_go':
                        effect_check.append(items['name'])
                        self.effects_lst.append({'name': items['name'], 'remaining turns': 1, 'effects': {'type': 'skip_go', 'impact': None}})
                    elif items['type'] == 'damage':
                        effect_check.append(items['name'])
                        self.effects_lst.append({'name': items['name'], 'remaining turns': 3, 'effects': {'type': 'damage', 'impact': items['effects']['impact']}})
        self.current_hp -= attack_dic['damage']
        if self.current_hp < 0:
            self.current_hp = 0
        if attack_dic['damage'] == 0:
            print(f"the attack was wholly inaffective.\n{self.name} took no damage.")
        else:
            print(f"{self.name} took {attack_dic['damage']} points of damage")
        if len(effect_check)> 0:
            for effects in effect_check:
                print(f"{self.name} is affected by {effects}.\n")

    # function checks if there any any combat usable items in the combatees inventories
    def check_items(self):
        check_num = 0
        if len(self.items) != 0:
            with open('game_data.txt', 'r') as file:
                file = file.read()
            game_data = json.loads(file)
            for items in game_data['items']:
                for it in self.items:
                    if it == items['name']:
                        if items['combat_check'] != False:
                            check_num += 1
            if check_num != 0:
                return True
            else:
                return False
        else:
            return False

    # lets player choose an item and returns its data as a dictioary
    def chose_items_player(self):
        if len(self.items) != 0:
            with open('game_data.txt', 'r') as file:
                file = file.read()
            game_data = json.loads(file)
            items_data = game_data['items']
            while True:
                print('Please select an item.')
                it_dict = {}
                num = 1
                for items in items_data:
                    for  it in self.items:
                        if it == items['name']:
                            it_dict[num] = items
                            print(f"\t{num}:\t{items['name']}\n\t\t{items['description']}")
                            num += 1
                print("\bb:\tBack.")
                while True:
                    item_choice = input('please make your selection?\t')
                    try:
                        if int(item_choice) not in range(1, num):
                            print('Unrecognised input.')
                            continue
                    except Exception:
                        if item_choice.lower() != 'b':
                            print('Unrecognised input.')
                            continue
                    break
                if item_choice.lower() == 'b':
                    return False
                print(f"\rYou have selected {it_dict[int(item_choice)]['name']}\n")
                while True:
                    final_check = input('Are you happy with this selection?\t')
                    if final_check.lower() not in ['y', 'n', 'yes', 'no']:
                        print('Unrecognised input')
                        continue
                    break
                if final_check.lower() in ['y', 'yes']:
                    self.items.remove(it_dict[int(item_choice)]['name'])
                    return it_dict[int(item_choice)]
        else:
            return False
    
    # lets the enemy select an item, some personalities have a higher chance of picking specific items
    def enemy_item_gen(self, personality):
        it_lst = []
        with open('game_data.txt', 'r')as file:
            file = file.read()
        game_data = json.loads(file)
        for items in game_data['items']:
            for it in self.items:
                if it == items['name']:
                    it_lst.append(items)
        if personality in  ['average', 'resourceful']:
            chice = random.choice(it_lst)
            self.items.remove(chice['name'])
            return chice
        elif personality == 'timid':
            chip = []
            for items in it_lst:
                if items['effects']['type'] == 'escape':
                    chip.append(items)
            if len(chip) == 0:
                for items in it_lst:
                    chip.append(items)
            chice = random.choice(chip)
            self.items.remove(chice['name'])
            return chice
        elif personality == 'smart':
            if self.check_magic_heal == True:
                for items in it_lst:
                    if items['effects']['type'] == 'healing' and items['effects']['impact'] >= self.max_hp - self.current_hp:
                        return items
            else:
                trim = self.enemy_item_gen('average')
                return trim
        

    # applies effect of the item
    def apply_item(self, item_dic):
        print(f"{self.name} uses {item_dic['name']}.")
        if item_dic['effects']['type'] == 'escape':
            return 'escape'
        elif item_dic['effects']['type'] == 'healing':
            self.current_hp += item_dic['effects']['impact']
            print(f"{self.name} was healed {item_dic['effects']['impact']}hp.")
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp
            elif self.current_hp < 0:
                self.current_hp = 0
    
    # checks if the combatee stil has hp
    def check_if_alive(self):
        if self.current_hp == 0:
            return False
        return True
    
    # checks the effectivness of any heal items held in the player inventory
    def check_magic_heal(self):
        with open('game_data.txt', 'r')as file:
            file = file.read()
        game_data = json.loads(file)
        for it in game_data['items']:
            for items in self.items:
                if it['name'] == items:
                    if it['effects']['type'] == 'healing':
                        if it['effects']['impact'] >= self.max_hp - self.current_hp:
                            return True
        return False
                    

    # returns the enermies personality type
    def return_personality(self):
        return self.personality
    

    # returns teh correct personality type depending on the enermy personality 
    def personality_check(self, ave_player_level_speed = None):
        if self.personality == 'timid':
            return self.timid_personality()
        elif self.personality == 'aggressive':
            return self.aggressive_personality()
        elif self.personality == 'smart':
            return self.smart_personality(ave_player_level_speed)
        elif self.personality == 'resourceful':
            return self.resourceful_personality()
        elif self.personality == 'wild':
            return self.wild_personality()
        elif self.personality == 'average':
            return self.average_personality()
    

    # start of the timid personality chain, they favour running but will attack if cornered
    def timid_personality(self):
        flavour_text = [' is scared.', ' is nervous.', ' is trepidatious.', 'is shaking with fear.', ' looks unsettled.', ' looks unwilling to fight.', ' wants to flee.']
        print(self.name + random.choice(flavour_text))
        choice_lst = [3, 3, 3]
        if self.check_items() == True:
            choice_lst.append(2)
        else:
            choice_lst.append(1)
        return random.choice(choice_lst)
        

    # start of the aggresiv personality chain. they always attack
    def aggressive_personality(self):
        flavour_text = [' is filled with rage.', ' is angry.', ' is waiting to attack.', ' looks intimidating.', ' is shaking with rage.', ' wants to fight.', ' is ready for a fight.']
        print(self.name + random.choice(flavour_text))
        return 1

    # start of the smart personality chain. they choose options based on teh situation they find themselves in. will edit further as we create more items/effects/attacks ect
    def smart_personality(self, ave_player_level):
        flavour_text = [' looks deep in thought.', ' is calculating its next move.', ' is looking for weaknesses.', ' has a plan.', ' knows its next move.', ' has something planned.']
        print(self.name + random.choice(flavour_text))
        # edit this personality so that its more likly to select items also when they has positive effects on stats
        choice_lst = []
        if self.level < ave_player_level[0] * 1.25 and self.sp >= ave_player_level[1] * 0.90:
            choice_lst.append(3)
        else:
            choice_lst.append(1)
        if self.current_hp < self.max_hp * 0.25:
            choice_lst.append(3)
        else:
            choice_lst.append(1)
        if self.check_items == True:
            choice_lst.append(2)
        if self.check_magic_heal == True:
            return 2
        chip = random.choice(choice_lst)
        return chip

    # really wants to use item effects, we havent got many atm but this will become more complex as we add more
    def resourceful_personality(self):
        flavour_text = [' is holding something.', ' is waiting to pull something out.', ' is fiddling with something.', ' wants to use an item.']
        print(self.name + random.choice(flavour_text))
        choice_lst = [1]
        if self.check_items() == True:
            num = 1
            while num != 3:
                choice_lst.append(2)
                num += 1
        else:
            choice_lst.append(3)
        chip = random.choice(choice_lst)
        return (chip)
        
    # start of the wild personality, always attacks unless low on health, then runs,  can do more damage but may also attack fellow enermies
    def wild_personality(self):
        flavour_text = [' is foaming at the mouth.', ' has a wild look in its eyes.', ' is charging around.', ' wants violence.', ' is grinding its teeth.']
        print(self.name + random.choice(flavour_text))
        choice_lst = [1]
        if self.current_hp < self.max_hp *0.10:
            choice_lst.append(3)
        return random.choice(choice_lst)

    #start of standard personality, pretty basic but thats not nes bad
    def average_personality(self):
        flavour_text = [' looks annoied.', ' is staring you down.', ' hopes this goes well.', ' is waiting to make its move.', "doesn't look particularly smart.", ' needs this to go well.']
        print(self.name + random.choice(flavour_text))
        choice_lst = [1]
        if self.check_items() == True:
            choice_lst.append(2)
        if self.current_hp < self.max_hp * 0.25:
            choice_lst.append(3)
        return random.choice(choice_lst)
        
    
# here the main body of the code starts

# this function simply prints out hp bars for each combatee
def print_hp_stats_bar(class_instance, speed_indicator = None):
    if speed_indicator == None:
        return f"{class_instance.return_name()}:\t{class_instance.return_hp()}/{class_instance.return_max_hp()}HP"
    else:
        return f"{class_instance.return_name()}:\t{class_instance.return_hp()}/{class_instance.return_max_hp()}HP\tOrder:\t{speed_indicator}"

# this is function that you call to start the combat encouter
def combat(enermies_lst):
    defeated_enemies = []
    battle_escape = False
    victory_condition = False
    # these lines of code call the data from the player_data.txt file, then instatuate the class for both enermies and player characters
    with open('player_data.txt', 'r')as file:
        file = file.read()
    player_data = json.loads(file)
    player = Battle_Class(player_data['name'], player_data['hp'], player_data['a_p'], player_data['d_p'], player_data['s_p'], player_data['aim'], player_data['items'], player_data['attacks'], player_data['max_hp'], True, player_data['level'])
    encounter_class_lst = []
    for enermies in enermies_lst:
        id_num = ''
        num = 0
        while num < 32:
            id_num = id_num + str(random.randrange(0, 9))
            num +=1
        encounter_class_lst.append(Battle_Class(enermies['name'], enermies['hp'], enermies['a_p'], enermies['d_p'], enermies['s_p'], enermies['aim'], enermies['items'], enermies['attacks'], enermies['hp'], False, enermies['level'], id_num, enermies['personality']))

    # this is just a bit of fun that alters the intro message depending on the number of enermies that are called into combat
    if len(encounter_class_lst) == 1:
        print('\n=================')
        print('Enemy Encountered')
        print('=================\n')
    else:
        print('\n===================')
        print('Enemies Encountered')
        print('===================\n')
    encounter_class_lst.append(player)
    # this while loop is the start of the combat loop
    while True:
        # these next lines of code reorder the turns of the combatees based on their speed stat
        speed_lst = []
        for units in encounter_class_lst:
            speed_lst.append(units.return_speed_no_edit())
        speed_lst = sorted(speed_lst, reverse = True)
        temp_lst = []
        for speed in speed_lst:
            for units in encounter_class_lst:
                if units.return_speed_no_edit() == speed:
                    encounter_class_lst.remove(units)
                    temp_lst.append(units)
        encounter_class_lst = temp_lst
        # these lines of code print the hp stats for each of the combatees, starting with the player character
        print(f"\n----------------\n  Player Stats  \n----------------\n")
        for entities in encounter_class_lst:
            if entities.return_is_plyer() == True:
                print(print_hp_stats_bar(entities, encounter_class_lst.index(entities)+1))
        print(f"\n\n---------------\n  Enemy Stats  \n---------------\n")
        for entities in encounter_class_lst:
            if entities.return_is_plyer() == False:
                print(print_hp_stats_bar(entities, encounter_class_lst.index(entities)+1))
        # here the combat loop is acted, all combatees class instances are contained in teh list encourter_class_lst. we can call them one at a time, 
        # checking for the is_plyer class variable and use that to checkif the instance is computer controled or player controlled
        for entities in encounter_class_lst:
            bar = '--------'
            for characters in entities.return_name():
                bar = bar + '-'
            print(f"\n{bar}\n{entities.return_name()}'s turn.\n{bar}\n\n")
            # the next two lines enact any effects the instance has on it, and apply the skip_go modifier if relivant, they also check the status of the enemy, weather it is alive or has escaped
            skip_go_indicator = entities.action_events()
            if skip_go_indicator != False and entities.return_status() == 'alive':
                # here it filters to see if this is the player or an enemy
                if entities.return_is_plyer() == True:
                    # next segment checks if the player is still alive
                    if entities.check_if_alive() == False:
                        print(f"{entities.return_name()} has been defeated.")
                        entities.set_status(2)
                    # main menu loop and the true start of the players turn
                    while True:
                        print(f"Main Menu\n1:\tAttack.\n2:\tItems.\n3:\tRun.\n")
                        main_menu_choice = input('Please select an option.\t')
                        try: 
                            if int(main_menu_choice) not in range(1, 4):
                                print('Unrecognised input.')
                                continue
                        except Exception:
                            print('Unrecognised input.')
                            continue
                        # this is the attack subchoice, starts by choosing an attack
                        if int(main_menu_choice) == 1:
                            while True:
                                en_lst = []
                                attack_lst = []
                                attack = entities.gen_player_attack()
                                if attack == False:
                                    break
                                # the next segment selects an enemy for the attack to attack
                                for enermies in encounter_class_lst:
                                    if enermies.return_is_plyer() == False and enermies.return_status() == 'alive':
                                        en_lst.append(enermies)
                                # no choice needed if just one enemy
                                if len(en_lst) == 1:
                                    attack_lst = en_lst
                                else:
                                    # if the attack is mono-targeting and there are multiple enermies, submenu opened so you can select an enemy
                                    if attack['mult_targets'] == 'single':
                                        print('\nPlease select a target.')
                                        while True:
                                            nums = 1
                                            for enermies in en_lst:
                                                print(f"{en_lst.index(enermies)+1}:\t{print_hp_stats_bar(enermies)}") 
                                                nums += 1
                                            print('b:\tback.')
                                            target_choice = input('\nChoose your target?\t')
                                            try:
                                                if int(target_choice) not in range(1, nums):
                                                    print('Unrecognised Input.')
                                                    continue  
                                            except Exception:
                                                if target_choice.lower() != 'b':
                                                    print('Unrecognised input.')
                                                    continue
                                            if target_choice.lower() != 'b':
                                                while True:
                                                    print(f'You have chosen {en_lst[int(target_choice)-1].return_name()}.')
                                                    final_choice = input('Are you happy with this choice?\t')
                                                    if final_choice.lower() not in ['y', 'n', 'yes',' no']:
                                                        print('Unrecognised input.')
                                                        continue
                                                    break
                                                if final_choice.lower() in ['n','no']:
                                                    continue
                                            break
                                        if target_choice.lower() == 'b':
                                            continue
                                        attack_lst.append(en_lst[int(target_choice)-1])
                                    # not needed if the attack attacks all enemies at once
                                    else:
                                        attack_lst = en_lst
                                # here for each enemy targeted it generates attack damage, sees if it passes defense, then applies the damage
                                for enermies in attack_lst:
                                    damage_dic = entities.gen_attack_damage(attack)
                                    attack_check = enermies.gen_defense(damage_dic)
                                    time.sleep(3)
                                    if attack_check == False:
                                        print(f'\nThey missed.\n{enermies.return_name()} avoided the attack.')
                                    else:
                                        if attack_check == 'fail':
                                            print('The attack hits.')
                                            time.sleep(1)
                                            print('But fails to do any damage.')
                                        else:
                                            print('\nThe attack hits.')
                                            enermies.take_damage(attack_check)
                                            life_check = enermies.check_if_alive()
                                            # here it checks if the enemy has been defeated
                                            if life_check == False:
                                                print(f'{enermies.return_name()} has been defeated.')
                                                enermies.set_status(2)
                                break
                        # this main_menu_choice selects and uses items
                        elif int(main_menu_choice) == 2:
                            # if you have no usable items you cannot access this menu
                            if entities.check_items() == False:
                                print('You have no useable items.')
                                continue
                            else:
                                # the next few lines open the item selection menu and then apply that item
                                item_data = entities.chose_items_player()
                                if item_data == False:
                                    continue
                                item = entities.apply_item(item_data)
                                if item == 'escape':
                                    battle_escape = True
                        # this main_menu_choice attempts to flee the battle
                        elif int(main_menu_choice) == 3:
                            while True:
                                run_check = input('Are you sure you want to run?')
                                if run_check.lower() not in ['y', 'n', 'yes', 'no']:
                                    print('Unrecognised input.')
                                    continue
                                break
                            if run_check.lower() in ['no', 'n']:
                                continue
                            print(f"You try to escape.")
                            no_catch_num = 0
                            en_num = 0
                            # is these lines, your sp score competes agains the sp score of the opponant, if you win you escape. if they win they get a free attack on you.
                            for enermies in encounter_class_lst:
                                if enermies.return_is_plyer() == False and enermies.return_status() == 'alive':
                                    en_num +=1
                                    escape_check = enermies.escape_calc(entities.return_speed())
                                    if escape_check == False:
                                        print(f"{enermies.return_name()} caught {entities.return_name()}.")
                                        attack = enermies.gen_enermy_attack()
                                        attack = enermies.gen_attack_damage()
                                        def_dic = entities.gen_defense(attack)
                                        time.sleep(3)
                                        if def_dic == False:
                                            print(f"{entities.return_name()} avoided the attack.")
                                        else:
                                            if def_dic == 'fail':
                                                print('The attack hit.')
                                                time.sleep(1)
                                                print('But failed to do any damage.')
                                            else:
                                                print('The attack hit.')
                                                entities.take_damage(def_dic)
                                                if entities.check_if_alive() == False:
                                                    print(f"{entities.return_name()} has been defeated.")
                                                    entities.set_status(2)
                                    else:
                                        no_catch_num += 1
                            # just a bit of fun, prints the appropriate message depending on how many times you were caught.
                            if en_num == 1 and no_catch_num == 0:
                                pass
                            elif no_catch_num == 0:
                                print(f'{entities.return_name()} was caught by every enemy.')
                            elif en_num - no_catch_num == 1:
                                print(f"{entities.return_name()} almost escaped. They were caught by 1 enemy.")
                            elif en_num > no_catch_num:
                                print(f'{entities.return_name()} was caught by {en_num-no_catch_num} enemies.')
                            else:
                                battle_escape = True
                        # idenfies weather you have suceeded in escaping combat and exits the function.
                        if battle_escape == True:
                            print(f'{entities.return_name()} escaped.')
                            entities.exit_game_save()
                            return True
                        break
                    time.sleep(3)
                else:
                    # checks if the enemy is alive at the start of the turn.
                    if entities.check_if_alive() == False:
                        print(f'{entities.return_name()} has been defeated.')
                        entities.set_status(2)
                    else:

                        # ok here the enermy ai is called, it returns the correct ai function depending on what personality is put into the personality check funciton

                        speed_av_lst = []
                        level_av_lst = []
                        for obs in encounter_class_lst:
                            if obs.return_is_plyer() == True:
                                speed_av_lst.append(obs.return_speed_no_edit())
                                level_av_lst.append(obs.return_level())
                        av_insert = [round(mean(level_av_lst)), round(mean(speed_av_lst))]
                        
                        main_menu_choice = entities.personality_check(av_insert)

                        # depending on the personallity these secontions change, both liklyhood and behaviour of choice
                        if main_menu_choice == 1:
                            attack = entities.gen_enermy_attack(entities.return_personality())
                            attack = entities.gen_attack_damage(attack, entities.return_personality())
                            # here it is selecting a target
                            # if the enemy type is wild it has a chance of selecting other enermies to attack. this feature may need to be removed as it seemingly causes chaos
                            attack_lst = []
                            for players in encounter_class_lst:
                                if entities.return_personality() == 'wild' and players.return_id_num() != entities.return_id_num() and entities.return_status() == 'alive':
                                    attack_lst.append(players)
                                elif players.return_is_plyer() == True:
                                    attack_lst.append(players)
                            if attack['attack_dic']['mult_targets'] == 'single':
                                attack_lst = [random.choice(attack_lst)]
                            # and here the targets get attacked/use their defense stat
                            for players in attack_lst:
                                print(f"{entities.return_name()} tried to attack {players.return_name()}")
                                attack_check = players.gen_defense(attack)
                                time.sleep(3)
                                if attack_check == False:
                                    print(f"The attack missed")
                                else:
                                    if attack_check == 'fail':
                                        print('The attack hit.')
                                        time.sleep(1)
                                        print('But failed top do any damage.')
                                    else:
                                        print(f'The attack hit.')
                                        players.take_damage(attack_check)



                        # here the enemy uses items. the selection paramerters are defined by their personality
                        elif main_menu_choice == 2:
                            item = entities.enemy_item_gen(entities.return_personality())
                            escape = entities.apply_item(item)
                            if escape == 'escape':
                                print(f'{entities.return_name()} escaped')
                                entities.set_status(1)

                        # here the enemy attepts to flee/ contesting its speed with yours. its likelyhood of picking this option depends on its personality
                        elif main_menu_choice == 3:
                            print(f"{entities.return_name()} tries to flea.")
                            speed = entities.return_speed()
                            pl_num = 0
                            escape_num = 0
                            for players in encounter_class_lst:
                                if players.return_is_plyer() == True:
                                    pl_num += 1
                                    # if the enemy is caught you get a free attack
                                    if players.escape_calc(speed) == False:
                                        print(f'{players.return_name()} caught them.')
                                        attack = players.gen_player_attack()
                                        attack = players.gen_attack_damage(attack)
                                        def_dic = entities.gen_defense(attack)
                                        time.sleep(3)
                                        if def_dic == False:
                                            print(f'The attack missed.')
                                        else:
                                            print('The attack hit.')
                                            entities.take_damage(def_dic)
                                    else:
                                        escape_num += 1
                            # here if the enemy escapes it is removed from the list
                            if pl_num == escape_num:
                                print(f'{entities.return_name()} escaped')
                                entities.set_status(1)
                    time.sleep(2)




            # here at the end of every loop of the encounter_class_lst the program checks if the battle has been won by seeing who is still alive or in play.
            en_c = 0
            p_c = 0
            p_es_c = 0
            for obs in encounter_class_lst:
                if obs.return_status() != 'alive' or obs.check_if_alive() == False:
                    if (obs.return_status() == 'defeated' or obs.check_if_alive() == False) and obs.return_is_plyer() == False:
                        obs.set_status(2)
                        defeated_enemies.append(obs)
                    if obs.return_is_plyer() == True:
                        if obs.return_status == 'escaped':
                            p_es_c += 1
                else:
                    if obs.return_is_plyer() == False:
                        en_c += 1
                    else:
                        p_c += 1     
            # if there are 0 of either opposing side alive or in play, the program breaks the loop and changes the victory_condition variable   
            if p_c == 0:
                if p_es_c == 0:
                    victory_condition = 'defeat'
                    break
                else:
                    victory_condition = 'escape'
                    break
            if en_c == 0:
                victory_condition = 'victory'
                break

        # applies victory conditions based upon the victory_conditions modifier.
        if victory_condition == 'defeat':
            print('Player Defeated')
            return False
        elif victory_condition =='escape':
            print('Player Escaped')
            return True
        elif victory_condition == 'victory':
            print('Player Victorious')
            # here we would insert loot and exp functions
            return True


                                        
                                

                        
# still not working, now wont let the player leave the battle when all of the enermies are no longer present
                    




                                



                                
                                    



                            


            








