import json
from statistics import mean
import random


def inventory_edit():
    items = [
        {'name': 'ball', 'description': 'round object used for fun',
            'combat_check': True, 'effects': {'type': 'escape', 'impact': False}},
        {'name': 'great vibes', 'description': 'a feeling of mild contentment.',
            'combat_check': True, 'effects': {'type': 'healing', 'impact': 1}},
        {'name': 'water', 'description': 'refreshment', 'combat_check': True,
            'effects': {'type': 'healing', 'impact': False}},
        {'name': 'camouflage', 'description': 'use this to hide from potential threats',
            'combat_check': True, 'effects': {'type': 'escape', 'impact': False}},
        {'name': 'repellant', 'description': 'rebounds any shots that go towards you back to enemy',
            'combat_check': True, 'effects': {'type': 'healing', 'impact': 5}},
        {'name': 'shield', 'description': 'protects the user from incoming attacks',
            'combat_check': True, 'effects': {'type': 'healing', 'impact': 10}},
        {'name': 'map', 'description': 'reveals the location of nearby enemies and items',
            'combat_check': False, 'effects': {'type': 'none', 'impact': 0}},
    ]

    def items_list(perfect_items):
        if len(perfect_items) > 0:
            user_item = random.choice(perfect_items)
            return user_item
        else:
            return None
    
    ret_item = items_list(items)
    
    with open('game_data.txt', 'r')as file:
        file = file.read()
    game_data = json.loads(file)
    
    game_data['items'].append(ret_item)
    game_data = json.dumps(game_data)
    
    with open('game_data.txt', 'w')as file:
        file.write(game_data)
        
    return ret_item
