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

#---------------------------------------------

# Below is the enemy level calculator. It generates an enemy level in the approximate region of the player's with a rough bell-curve distribution.


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
    
def loot_calculator(enemy_level):
    
    drop_base_probability = {"Gold Coin":2,"Silver Coin":4, "Bronze Coin":8,"Healing potion":4,"Greater Healing potion":1}
        
    lootlist = list()
    
    
    for item in drop_base_probability:
        
        probability_calculator = drop_base_probability.get(item)
    
        probability_score = (int(probability_calculator) * int(enemy_level))
        
        num_generator = random.randint(0,100)
        if num_generator >= probability_score:
            pass
        else:
            lootlist.append(item)
    
    if bool(lootlist) == False:
        lootlist = ["None"]
    else:
        return lootlist
    
"""
Below is the enemy stat calculator. It currently has 3 functions:
(1) It parses the player_data and game_data txt files for player level, location and data about enemy attacks.
(2) It generates an appropriate monster type from the player's biome.
(3 It uses the the previous functions to generate an enemy stats (complete with treasure)

"""

def enemy_stat_calculator():
      
        
    # This segment parses the "player_data.txt" file for the playerstats_dict and pulls the player's level and location

    with open('player_data.txt') as json_file:
        playerstats = json.load(json_file)
    
    player_level = playerstats.get('level')


    player_location = playerstats.get('location')

    # This section parses the "game_data.txt" file for the "personality" list:    

    with open ('game_data.txt') as json_file:
        gamedata = json.load(json_file)
    
    
    personality_list = gamedata.get('personality_types')

    personality = random.choice(personality_list)

    attacks = gamedata.get("attacks")
    
    items = gamedata.get("items")
    
    #---------------------------------------------------------------------------------------------------
        
    # I suppose at some point the "monster_locations dict" (see below) should go to the game_data.txt file....but it is here for now
        
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
                   "attacks": attacks,
                   "loot": loot_calculator(enemy_level),}
    
    return enemy_stats


"""
The final section opens the "game_data.txt" file and alters the value of the "enemies" key from "[]" to the 
results of the executed enemy_stat_calcualtor.

"""

enemy_stat_calculator_executed = enemy_stat_calculator()


with open('game_data.txt', 'r') as infile:
    data = json.load(infile)
    
data["enemies"] = enemy_stat_calculator_executed
    
with open('game_data.txt', 'w') as outfile:
    json.dump(data, outfile)
