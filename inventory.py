import json
from statistics import mean
import json
import random
import json


def inventory():
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

    perfect_items = [item for item in items if item['combat_check'] == True]

    # print(perfect_items)

    def items_list(perfect_items):
        if len(perfect_items) > 0:
            user_item = random.choice(perfect_items)
            return user_item
        else:
            return None

    # print('working', items_list(perfect_items))

    # different attacks list of ten
    attacks = [
        {'name': 'Scratch', 'attack_modifer': 1, 'lvl_avilble': 0,
            'description': 'Rake the foe with long, unclean finger nails.', 'effects': ['burn'], 'mult_targets': 'single'},
        {'name': 'Flamethrower', 'attack_modifer': 1.5, 'lvl_avilble': 10,
            'description': 'Blasts the opponent with a powerful stream of flames.', 'effects': ['burn'], 'mult_targets': 'single'},
        {'name': 'Thunderbolt', 'attack_modifer': 1.5, 'lvl_avilble': 20,
            'description': 'A powerful electrical discharge that deals damage and may paralyse the target.', 'effects': ['paralyze'], 'mult_targets': 'single'},
        {'name': 'Ice Beam', 'attack_modifer': 1.5, 'lvl_avilble': 30,
            'description': 'A beam of freezing ice that deals damage and may freeze the target.', 'effects': ['freeze'], 'mult_targets': 'single'},
        {'name': 'Earthquake', 'attack_modifer': 2.0, 'lvl_avilble': 40,
            'description': 'A powerful earthquake that deals damage to all opponents.', 'effects': [], 'mult_targets': 'all'},
        {'name': 'Psychic', 'attack_modifer': 1.5, 'lvl_avilble': 50, 'description': 'A powerful mental attack that deals damage and may lower the target\'s Special Defense.',
            'effects': ['lower_special_defense'], 'mult_targets': 'single'},
        {'name': 'Shadow Ball', 'attack_modifer': 1.5, 'lvl_avilble': 60, 'description': 'A ball of dark energy that deals damage and may lower the target\'s Special Defense.',
            'effects': ['lower_special_defense'], 'mult_targets': 'single'},
        {'name': 'Hyper Beam', 'attack_modifer': 2.0, 'lvl_avilble': 70,
            'description': 'A devastatingly powerful attack that requires a turn to recharge after use.', 'effects': [], 'mult_targets': 'single'},
        {'name': 'Hydro Pump', 'attack_modifer': 1.5, 'lvl_avilble': 80,
            'description': 'A powerful jet of water that deals damage.', 'effects': [], 'mult_targets': 'single'},
        {'name': 'Explosion', 'attack_modifer': 2.0, 'lvl_avilble': 90,
            'description': 'A suicidal attack that deals massive damage to all opponents.', 'effects': [], 'mult_targets': 'all'}
    ]

    effects = [{'name': 'burn', 'description': 'hot flame applied to skin',
                'effects': {'type': 'damage', 'impact': 5}}]

    player_data = {'name': 'jeff', 'level': 1, 'hp': 10, 'a_p': 10, 'd_p': 40, 's_p': 0,
                   'aim': 50, 'items': ['ball', 'great vibes'], 'attacks': ['Scratch'], 'max_hp': 10}

    ai_personality_types = ['timid', 'aggressive',
                            'smart', 'resourceful', 'wild', 'average']

    game_data = {'attacks': attacks, 'items': items,
                 'effects': effects, 'personality_types': ai_personality_types}

    p_d = json.dumps(player_data)
    g_d = json.dumps(game_data)

    with open('game_data.txt', 'w')as file:
        file.write(g_d)

    with open('player_data.txt', 'w') as file:
        file.write(p_d)

# below not working.
    # with open('game_data.txt', 'r') as file:
    #     file = file.read()
    #     game_data = json.load(file)


# without this i'm unable to print anything out this needs to remain here.
if __name__ == '__main__':
    inventory()
