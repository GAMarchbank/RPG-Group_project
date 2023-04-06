# REQUIRES "player_data.txt" and "game_data.txt" files to function.

"""
This enemy stat calculator consists of
(1) a section to import data from the "player_data.txt and the "game_data.txt" files ,
(2) a function to determine the enemy level based on the player's level,
(3) a function to calculate the enemy loot drops, 
(4) a function to bring it all together into the "enemy stats" dictionary,
(5) a few lines of code to upload the enemy stats into a JSON file.

"""

import json
import random
from items_generator import inventory_edit
from copy import deepcopy

#---------------------------------------------

# Below is the enemy level calculator. It generates an enemy level in the approximate region of the player's with a rough bell-curve distribution.
# G - I have left unchanged. possible will need updating as currenlty will break when player level is over 10, maybe tie the random choice list to being directly created by the player level. not importatnt now

def enemy_level_calculator(player_level):
    if player_level == 1:
        enemy_level = 1
    elif player_level >= 2 and player_level <= 3:
        enemy_level = random.choice([1,2,2,2,3,3,3,4])
    elif player_level > 3 and player_level <= 5:
        enemy_level = random.choice([2,3,3,4,4,4,5,5,6])
    elif player_level > 5 and player_level <=7:
        enemy_level = random.choice([4,5,5,6,6,6,7,7,8])
    elif player_level > 7 and player_level <=9:
        enemy_level = random.choice([6,7,7,8,8,8,9,9,10])
    elif player_level == 10:
        enemy_level = random.choice([8,9,9,10,10,10])
    else:
        print("Error calculating enemy strength.")
    return enemy_level


# below is the loot calculator. It calculates the loot drop based upon a "base" drop chance for each item multiplied by the enemy level
# G - have edited so the items are taken from the item generator, have removed the loot submenu as the loot will just be the items that are left from each account. we can add some form of currency if we choose to add that to the game later. 

def item_calculator():
    prob_lst = [0,1,2,3,4,5,6]
    rev_prob_lst = deepcopy(prob_lst)
    rev_prob_lst = list(reversed(rev_prob_lst))
    chance_lst = []
    for items in prob_lst:
        num = rev_prob_lst[prob_lst.index(items)]
        while num != 0:
            chance_lst.append(items)
            num -= 1
    item_amount = random.choice(chance_lst)
    items_list = []
    while item_amount != 0:
        item = inventory_edit()
        items_list.append(item['name'])
        item_amount -= 1
    return items_list
    
"""
Below is the enemy stat calculator. It currently has 3 functions:
(1) It parses the player_data and game_data txt files for player level, location and data about enemy attacks.
(2) It generates an appropriate monster type from the player's biome.
(3 It uses the the previous functions to generate an enemy stats (complete with treasure)

"""

def enemy_stat_calculator():
      
        
    # This segment parses the "player_data.txt" file for the playerstats_dict and pulls the player's level and location

    with open('player_data.txt', 'r') as json_file:
        playerstats = json.load(json_file)
    
    player_level = playerstats.get('level')

    # G- will change this when game is loaded to be take directly from the map as it in in play
    player_location = playerstats.get('location')

    # This section parses the "game_data.txt" file for the "personality" list:    

    with open ('game_data.txt', 'r') as json_file:
        gamedata = json.load(json_file)
    
    
    personality_list = gamedata.get('personality_types')

    personality = random.choice(personality_list)

    attacks = []
    attack = gamedata["attacks"]
    for items in attack:
        attacks.append(items['name'])
    
    # G- Changed to be taken directly form the itemscalc function, what what the loot funct function
    items = item_calculator()
    
    #---------------------------------------------------------------------------------------------------
        
    # I suppose at some point the "monster_locations dict" (see below) should go to the game_data.txt file....but it is here for now
    # G - we can put this into the game data when the map has been written, till now this will do. should also think about putting more data into here so its ties to what attacks or data each enermy can have, though that might just be complxity for hte sake of complexity
   
    monster_locations_dict = {
    
    "Desert" : ["Scarab Beetle","Scorpion", "Giant Sandworm"],
    
    "Haunted Castle" : ["Possessed Armour", "Ghost","Gargoyle"],
    
    "Swamp" : ["Goblin", "Living Slime", "Witch"],
    
    "Forest" : ["Spider", "Ogre", "Carnivorous Tree"]
    
    }
    
    # This bit below selects a random monster from the location of the player
      
        
    all_local_monsters = monster_locations_dict.get(player_location)
    
    monster_type = random.choice(all_local_monsters)
    
       
    """
    These placeholder enemy stat calculations (aside from enemy level) are deliberately basic until a better system is decided
    upon.
    """
    # G - have left unedited untill we come to balencing the game

    enemy_level = enemy_level_calculator(player_level)
    
    hitpoints = 5 + enemy_level
    attackpoints = enemy_level
    defencepoints = enemy_level
    speedpoints = enemy_level
    aim = enemy_level
    
    
    
    enemy_stats = {"name": monster_type,
                   "level":enemy_level,
                   "location": (player_location),
                   "items": items,
                   "personality": personality,
                   "hp": hitpoints,
                   "a_p": attackpoints,
                   "d_p": defencepoints,
                   "s_p": speedpoints,
                   "aim": aim,
                   "attacks": attacks}
                   
    gamedata['enemies'].append(enemy_stats)
    game_data = json.dumps(gamedata)
    
    
    with open('game_data.txt', 'w')as file:
        file.write(game_data)    
    
    return enemy_stats


"""
The final section opens the "game_data.txt" file and alters the value of the "enemies" key from "[]" to the 
results of the executed enemy_stat_calcualtor.

"""

# G - I have moved this section up to be contained within the function 
