import json
from statistics import mean


attacks = [{'name': 'Scratch', 'attack_modifer': 1, 'lvl_avilble': 0, 'description': 'Rake the foe with long, unclean finger nails.', 'effects': ['burn'], 'mult_targets': 'single'}]

items = [{'name': 'Stone Aroma', 'description': 'A mysterious Blue smell. It is not known how it is carried. When inhaled inbibes defence effects.', 'combat_check': True, 'effects': {'type': 'defence', 'impact': 6}}, {'name': 'Insignificant Green Spray', 'description': 'An old perfume bottle filled with an InsignificantGreen liquid. When inhaled will cause Poison damage.', 'combat_check': True, 'effects': {'type': 'effects', 'impact': 'poison', 'mod': 2}}, {'name': 'Invigorating Aroma', 'description': 'A mysterious Green smell. It is not known how it is carried. When inhaled inbibes healing effects.', 'combat_check': True, 'effects': {'type': 'healing', 'impact': 3}}, {'name': 'Smokebomb', 'description': 'A small explosive device that produces a lot of smoke. Pretty sure you could run if you threw this at the ground.', 'combat_check': True, 'effects': {'type': 'escape', 'impact': None}}, {'name': 'Purifying Vibes', 'description': 'A mysterious Yellow feeling. When felt inbibes clensing effects. Must be a very powerful feeling.', 'combat_check': True, 'effects': {'type': 'clensing', 'impact': 0}}, {'name': 'Strengthening Leaf', 'description': 'A mysterious Red leaf. Can be chewed or brewed to make a tea. When drunk inbews attack effects.', 'combat_check': True, 'effects': {'type': 'attack', 'impact': 2}}, {'name': 'Insignificant Red Mist', 'description': 'A arosol can filled with an, InsignificantRed liquid. When inhale will cause Explosive damage.', 'combat_check': True, 'effects': {'type': 'damage', 'impact': 3, 'mod': 3}}]

effects = [{'name': 'burn', 'description': 'This indiviuals skin in scortched or blistered.', 'effects': {'type': 'damage', 'impact': 5}}, {'name': 'poison', 'description': 'Toxins course though this individuals body.', 'effects': {'type': 'damage', 'impact': 6}}, {'name': 'sleep', 'description': 'This individual is fast asleep.', 'effects': {'type': 'skip_go', 'impact': None}}]

player_data = {'name': 'jeff','level': 1, 'location': 'Desert', 'hp': 10, 'a_p': 10, 'd_p': 40, 's_p': 0, 'aim': 50, 'items': ['Stone Aroma', 'Insignificant Green Spray', 'Invigorating Aroma', 'Smokebomb', 'Purifying Vibes', 'Strengthening Leaf', 'Insignificant Red Mist'], 'attacks': ['Scratch'], 'max_hp': 10}

ai_personality_types = ['timid', 'aggressive', 'smart', 'resourceful', 'wild', 'average']


game_data = {'attacks': attacks, 'items': items, 'effects': effects, 'personality_types': ai_personality_types, 'enemies': []}

p_d = json.dumps(player_data)
g_d = json.dumps(game_data)

with open('game_data.txt', 'w')as file:
    file.write(g_d)

with open('player_data.txt', 'w') as file:
    file.write(p_d)
    

