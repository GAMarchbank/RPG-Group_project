import json
import random


def inventory_edit():
    name_dic = {'gen_names': [{'name':'Powder', 'mod': 4, 'rare': 5, 'type': 'all', 'desc': ['a mysterious ', ' powder. When inhales induces ', ' effects.']}, {'name': 'Potion', 'mod': 6, 'rare': 3, 'type': 'all', 'desc': ['A mysterious ', ' potion. When drunk inbibes ', ' effects.']}, {'name': 'Salve', 'mod': 5, 'rare': 4, 'type': 'all', 'desc': ['A mysterious ', ' salve. When applied to the skin inbibes ', ' effects.']}, {'name':'Leaf', 'mod': 2, 'rare': 7, 'type': 'all', 'desc': ['A mysterious ', ' leaf. Can be chewed or brewed to make a tea. When drunk inbews ', ' effects.']}, {'name': 'Aroma', 'mod': 3, 'rare': 6, 'type': 'all', 'desc': ['A mysterious ', ' smell. It is not known how it is carried. When inhaled inbibes ', ' effects.']}, {'name': 'Injection', 'mod': 7, 'rare': 2, 'type': 'all', 'desc': ['A mysterious ', ' syringe. It may be unwise to use. When injected inbibies ', ' effects.']}, {'name': 'Vibes', 'mod': 1, 'rare': 8, 'type': 'all', 'desc': ['A mysterious ', ' feeling. When felt inbibes ', ' effects. Must be a very powerful feeling.']}], 
                'specific_items': [{'name': 'Shield', 'type': 'defence', 'mod': 8, 'rare': 1, 'desc': ['A metaphorical ', ' shield. When used offers ', ' from attack.']}, {'name': 'Sword', 'type': 'attack', 'mod': 8, 'rare': 1, 'desc': ['A metaphorical ', ' sword. When used offers ', ' benifits.' ]}, {'name': 'Medicine', 'type': 'healing', 'mod': 8, 'rare': 1, 'desc': ['A large ', ' pill. When swallowed inbibes ', ' effects.']}, {'name': 'Salts', 'type': 'cleansing', 'mod': 8, 'rare': 1, 'desc': ['A bag of ', ' strong smelling salts. When smelt offers ', ' effects.']}], 
                'escape_items': [{'name': 'Rope', 'type': 'escape', 'rare': 4, 'desc': 'A rope used to climb out of harms way.'}, {'name':'Mysterious Door', 'type': 'escape', 'rare': 2, 'desc': 'A mysterious door. Can be entered to escape combat.'}, {'name': 'Smokebomb', 'type': 'escape', 'rare': 3, 'desc': 'A small explosive device that produces a lot of smoke. Pretty sure you could run if you threw this at the ground.'}], 
                'area_effects': [{'name': 'Bomb', 'mod': 4, 'rare': 2, 'type': 'area', 'desc': ['An ', ' explosive device. When it explodes will cause ', ' damage.']}, {'name': 'Mist', 'mod': 3, 'rare': 4, 'type': 'area', 'desc': ['A arosol can filled with an, ', ' liquid. When inhale will cause ', ' damage.']}, {'name': 'Spray', 'mod': 2, 'rare': 5, 'type': 'area', 'desc': ['An old perfume bottle filled with an ', ' liquid. When inhaled will cause ', ' damage.']}, {'name': 'Spikes', 'mod': 1, 'rare': 6, 'type': 'area', 'desc': ['A bad fill of spikes, coated in a ', ' liquid. When stepped on will cause ', ' damage.']}]}

    discript_names = {'healing': {'words': [{'name': 'Healing', 'mod': 3, 'rare': 1, 'type': 'healing'}, {'name':'Revitalising', 'mod': 2, 'rare': 3, 'type': 'healing'}, {'name':'Invigorating', 'mod': 1, 'rare': 6, 'type': 'healing'}], 'colour': 'Green'}, 
                    'attack':{'words': [{'name': 'Strengthening', 'mod': 1, 'rare': 6, 'type': 'attack'}, {'name':'Enraging', 'mod': 2, 'rare': 3, 'type': 'attack'}, {'name':'Blood', 'mod': 3, 'rare': 1, 'type': 'attack'}], 'colour': 'Red'}, 
                    'defence': {'words':[{'name': 'Iron', 'mod': 3, 'rare': 1, 'type': 'defence'}, {'name': 'Stone', 'mod': 2, 'rare': 3, 'type': 'defence'}, {'name':'Protective', 'mod': 1, 'rare': 6, 'type': 'defence'}], 'colour': 'Blue'}, 
                    'cleansing': {'words': [{'name': 'Purifying', 'mod': 0, 'rare': 4, 'type': 'clensing'}, {'name': 'Purging', 'mod': 0, 'rare': 4, 'type': 'clensing'}], 'colour': 'Yellow'}, 
                    'area_effects': [{'name': 'Poison', 'colour': 'Green', 'rare': 2, 'type': 'poison'}, {'name': 'Soporific', 'colour': 'Purple', 'rare': 2, 'type': 'sleep'}, {'name': 'Acid', 'colour': 'Yellow', 'rare': 2, 'type': 'burn', 'mod': 1}, {'name': 'Explosive', 'colour': 'Red', 'rare': 1, 'type': 'damage', 'mod': 3}, {'name': 'Healing', 'colour': 'Blue', 'rare': 2, 'type': 'healing'}, {'name': 'Sharp', 'colour': 'Spikey', 'rare': 2, 'type': 'damage', 'mod': 2}], 
                    'area_effect_mods': [{'name': 'Insignificant', 'mod': 1, 'rare': 7}, {'name': 'Unstable', 'mod': 2, 'rare': 5}, {'name': 'Advanced', 'mod': 3, 'rare': 3},{'name': 'Atomic', 'mod': 4, 'rare': 1}]}
    
    desc_mod_lst = {'all': ['healing', 'attack', 'defence', 'cleansing'], 'defence': ['defence'], 'attack': ['attack'], 'healing': ['healing'], 'cleansing': ['cleansing']}
    
    items_lst = []
    for items in name_dic:
        for item in name_dic[items]:
            num = item['rare']
            while num > 0:
                items_lst.append(item)
                num -= 1
    name_choice = random.choice(items_lst)
    desc_lst = []
    if name_choice['type'] not in ['escape', 'area']:
        for tags in desc_mod_lst[name_choice['type']]:
            for items in discript_names[tags]['words']:
                num = items['rare']
                while num > 0:
                    desc_lst.append([items, discript_names[tags]['colour']])
                    num -= 1
        des_choice = random.choice(desc_lst)
        description = name_choice['desc'][0] + des_choice[1] + name_choice['desc'][1] + des_choice[0]['type'] + name_choice['desc'][2]
        des_choice = des_choice[0]
        output_dic = {'name': str(des_choice['name']) + ' ' + str(name_choice['name']), 'description': description, 'combat_check': True, 'effects': {'type': des_choice['type'], 'impact': int(des_choice['mod'])*int(name_choice['mod'])}}
         
    elif name_choice['type'] == 'area':
        area_effects_lst = []
        area_effects_mod_lst = []
        for items in discript_names['area_effects']:
            num = items['rare']
            while num > 0:
                area_effects_lst.append(items)
                num -= 1
        for obs in discript_names['area_effect_mods']:
            num = obs['rare']
            while num > 0:
                area_effects_mod_lst.append(obs)
                num -= 1
        des_choice = [random.choice(area_effects_lst), random.choice(area_effects_mod_lst)]
        description = name_choice['desc'][0] + des_choice[1]['name']  + des_choice[0]['colour'] + name_choice['desc'][1] + des_choice[0]['name'] + name_choice['desc'][2]
        if des_choice[0]['type'] == 'damage':
            effects = 'damage'
            impact = des_choice[0]['mod'] * des_choice[1]['mod'] 
        else:
            effects = 'effects'
            impact = des_choice[0]['type']
        output_dic = {'name': des_choice[1]['name'] + ' ' + des_choice[0]['colour'] + ' ' + name_choice['name'], 'description': description, 'combat_check': True, 'effects': {'type': effects, 'impact': impact, 'mod': name_choice['mod'] * des_choice[1]['mod']}}     
        
    else:
        output_dic = {'name': name_choice['name'], 'description': name_choice['desc'], 'combat_check': True, 'effects': {'type': 'escape', 'impact': None}}
    
    
    with open('game_data.txt', 'r')as file:
        file = file.read()
    game_data = json.loads(file)
    
    check = True
    for items in game_data['items']:
        if items['name'] == output_dic['name']:
            check = False
    
    if check == True:
        game_data['items'].append(output_dic)
        game_data = json.dumps(game_data)
        with open('game_data.txt', 'w')as file:
            file.write(game_data)
        
    return output_dic
