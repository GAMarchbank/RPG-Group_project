import json
import random
from items_generator import inventory_edit
from copy import deepcopy
from Enemy_generator import enemy_stat_calculator


# G - I've enlarged the locations dictionary and made it so it functions more smoothly with ramoniser. I've also moved it so its now saved onto the game_data file.

# G - this is the updated location generator, what we have been calling in some conversations in the room generator, I've left space for us to insert our ideas for quests.
def generate_location(rand = True, location = None, dungeon_dic = None, quest_data = False):
    # G - a basic list of dictions which the player move
    doors_lst = ['north', 'east', 'south', 'west'] 
    # G - Loading the locations dictionary
    with open('game_data.txt', 'r')as file:
        file = file.read()
    game_data = json.loads(file)
    locations_dic = game_data['locations dic']
    # G - This section will load if ther are no quest options. may edit later
    if rand == True or (rand == False and location != None and quest_data == False):
        # G - if its the first time around the choices are all completely random
        if rand == True:
            loc_type = random.choice(list(locations_dic.keys()))
            sub_cat = 'deep'
            loc_choice = random.choice(list(locations_dic[loc_type]['locations'][sub_cat].keys()))
        else:
            # G - else it extracts the previous rooms from the dungeon dictionary and then uses them to work out how likely the other options will be. 
            loc_type = location
            pre_rooms_lst = []
            for keys in dungeon_dic:
                if dungeon_dic[keys] != None:
                    pre_rooms_lst.append(keys)
            num = 0
            for item in pre_rooms_lst:
                if dungeon[item]['type'] == location:
                    num += 1
            if num in [0,1]:
                sub_cat = 'deep'
            elif num in range(2, 4):
                sub_cat = random.choice(['deep', 'deep', 'deep', 'transition'])
            else:
                sub_cat = random.choice(['deep', 'transition'])
            loc_choice = random.choice(list(locations_dic[loc_type]['locations']['deep'].keys()))
        # G - based on these previous choices the other details for the rooms are then randomly selected
        loc_descript = random.choice(locations_dic[loc_type]['locations'][sub_cat][loc_choice]['description'])
        loc_doors = {}
        # G - It selects one direct that the player can't move it. I might change this later to mirror the direction that you previously traveled in. 
        direction_index_non_num = random.choice([0,1,2,3])
        doors_choice = deepcopy(locations_dic[loc_type]['locations'][sub_cat][loc_choice]['doors']['exit points'])
        for directions in doors_lst:
            if doors_lst.index(directions) != direction_index_non_num:
                if len(doors_choice) != 0:
                    door_opt = random.choice(doors_choice)
                    doors_choice.remove(door_opt)
                else:
                    door_opt = random.choice(locations_dic[loc_type]['locations'][sub_cat][loc_choice]['doors']['exit points'])
                loc_des_des = random.choice(locations_dic[loc_type]['locations'][sub_cat][loc_choice]['doors']['descriptions'][door_opt])
                loc_doors[directions] = {'exit point': door_opt, 'description': loc_des_des} 
        # G - the skeleton of the location that will be returned with some data input
        room_instance = {'name': loc_choice, 'description': loc_descript, 'type': loc_type, 'doors': loc_doors, 'objects': []}
        # G - here it chooses how many objects to populate this location with, then the items and enemies for that object
        object_num = random.randrange(3,5)
        location_objects_lst = deepcopy(locations_dic[loc_type]['objects'])
        while object_num != 0:
            obj = random.choice(location_objects_lst)
            # G -edit blow to insert enermies and the such, change for location enermy difficulty and type
            if random.randrange(0,2) == 1:
                enemy_lst = []
                enermy_num = random.randrange(1,4)
                while enermy_num != 0:
                    enemy = enemy_stat_calculator(loc_type)
                    enemy_lst.append(enemy)
                    enermy_num -=1
            else:
                enemy_lst = None
            if random.randrange(0,2) == 1:
                item = inventory_edit()
            else:
                item = None
            object_dic = {'name': obj, 'enemies': enemy_lst, 'item': item}
            room_instance['objects'].append(object_dic)
            object_num -= 1
        return room_instance
        

#function to create the 'dungeon' i.e. series of locations/rooms to explore for each game instance
# G - changed this function so it creates the foundations of the dungeon and only populates one room. 
def create_dungeon() :
    #variable to set random number of linked locations/rooms
    num_of_rooms = random.choice(range(5,15))
    dungeon = {}
    i = 1
    while i <= num_of_rooms :
        dungeon[i] = None
        i += 1
    dungeon[1] = generate_location()
    return (dungeon)


if __name__ == '__main__':
    # G - Example of the initial dungeon creation 
    dungeon = create_dungeon()
    # G - Example of the second room in the dungeon being generated
    # dungeon[2] = generate_location(False, dungeon[1]['type'], dungeon)
    # print(dungeon)
    for items in dungeon:
        print(items)
        try:
            for obs in dungeon[items]:
                print(f"{obs}:\t{dungeon[items][obs]}")
        except Exception:
            print(dungeon[items])