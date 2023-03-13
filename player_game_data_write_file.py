import json
from statistics import mean


attacks = [{'name': 'Scratch', 'attack_modifer': 1, 'lvl_avilble': 0, 'description': 'Rake the foe with long, unclean finger nails.', 'effects': ['burn'], 'mult_targets': 'single'}]

items = [{'name': 'ball', 'description': 'round object used for fun', 'combat_check': True, 'effects': {'type': 'escape', 'impact': False}}, {'name': 'great vibes', 'description': 'a feeling of mild contentment.', 'combat_check': True, 'effects': {'type': 'healing', 'impact': 1}}]

effects = [{'name': 'burn', 'description': 'hot flame applied to skin', 'effects': {'type': 'damage', 'impact': 5}}]

player_data = {'name': 'jeff','level': 1, 'hp': 10, 'a_p': 10, 'd_p': 40, 's_p': 0, 'aim': 50, 'items': ['ball', 'great vibes'], 'attacks': ['Scratch'], 'max_hp': 10}

ai_personality_types = ['timid', 'aggressive', 'smart', 'resourceful', 'wild', 'average']


game_data = {'attacks': attacks, 'items': items, 'effects': effects, 'personality_types': ai_personality_types}

p_d = json.dumps(player_data)
g_d = json.dumps(game_data)

with open('game_data.txt', 'w')as file:
    file.write(g_d)

with open('player_data.txt', 'w') as file:
    file.write(p_d)

