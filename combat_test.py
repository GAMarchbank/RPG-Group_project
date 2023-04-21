import player_game_data_write_file
from Enemy_generator import enemy_stat_calculator
from run_full_battle import combat
from xp_calc import xp_caclulator
import random
from copy import deepcopy
import json


chance_lst = [1,2,3,4,5]
rev_chance_lst = deepcopy(chance_lst)
rev_chance_lst = list(reversed(rev_chance_lst))
whole_lst = []
for numbers in chance_lst:
    num = rev_chance_lst[chance_lst.index(numbers)]
    while num != 0:
        whole_lst.append(numbers)
        num -= 1
enemy_number = random.choice(whole_lst)
en_lst = []
location = random.choice(['Temperate Woodlands', 'Mountains', 'Wetlands', 'Urban', 'Grasslands', 'Desert', 'Water', 'Underground'])
while enemy_number != 0:
    enemy = enemy_stat_calculator(location)
    en_lst.append(enemy)
    enemy_number -= 1

combat(en_lst)
xp_caclulator()





