from locations import create_dungeon, generate_location
from run_full_battle import combat
from player_game_data_write_file import new_game, player_new_game, load_game_data, load_player_data, save_game_data, save_player_data
from xp_calc import xp_caclulator
import time
import os.path
from num2words import num2words


# the program starts here
print('\n\n==================')
print('Welcome to The RPG')
print('==================\n\n\n')
time.sleep(2)
# checking to see if a save file exists and displaying corrent menu, creates path_check variable as bool depending on outcome.
while True:
    if os.path.exists('player_data.txt'):
        print('1:\tContinue\n2:\tNew Game')
        path_check = True
    else:
        print('1:\tNew Game')
        path_check = False
    # user input is contained in a while loop to exclude unrelivent results.
    while True:
        main_menu_choice = input('\nPlease select a menu option?')
        try:
            int(main_menu_choice)
        except Exception:
            print('\nUnrecognised input.')
            continue
        else:
            if (path_check == True and int(main_menu_choice) not in [1, 2]) or (path_check == False and int(main_menu_choice) != 1):
                print('\nUnrecognised input.')
                continue
            else:
                break
    # checks both path_check bool variable and player choice, either creates new game or continues previous game.  
    if path_check == True and int(main_menu_choice) == 1:
        # here the files that are needed to run a game are loaded from the previous games saved data.
        game_data = load_game_data()
        player_data = load_player_data()
        new_game_bool = False
        print('\nLoading previous game.')
        time.sleep(2)
        print(f'\nYou rejoin the action where our main character {player_data["name"]} has just arrived at a {game_data["dungeon_dic"][game_data["player_location"]]["name"]}.\n')
        current_dungeon = game_data['dungeon_dic']
        break
    else:
        # here if the player chooses to create a new game but has already got a saved data it lets the user choose to delete their old data or go back to the main menu. 
        if path_check == True:
            while True:
                remove_choice = input('\nAre you sure you want to start a new game and delete your previous save file?')
                if remove_choice.lower() not in ['y', 'n', 'yes', 'no']:
                    print('\nUnrecognised input. Please enter Yes or No.')
                    continue
                else:
                    break
            if remove_choice.lower() in ['y', 'yes']:
                os.remove('player_data.txt')
                os.remove('game_data.txt')
                print('\nPrevious game data has been deleted.')
            else:
                print('\nReturning to previous menu.')
                continue
        # here it creates new data it the player chooses to create a new game. 
        game_data = new_game()
        player_data = player_new_game()
        new_game_bool = True
        print('\nYour jouney begins here...\n')
        time.sleep(2)
        current_dungeon = create_dungeon()
        game_data['player_location'] = '1'
        game_data['dungeon_dic'] = current_dungeon
        save_game_data(game_data)
        print(f"Our story begins with our main character {player_data['name']} arriving at a {game_data['dungeon_dic'][game_data['player_location']]['name']}.\n")
        break

name = player_data['name']

while True:
    # here is the main game play loop. the user is required to observe and interact with two objects minimum to continue to the next room. 
    # this part detects weather this is the final room in the dungeon and defines a variable that will be used to check the number of objects a player has interacted with.
    # also created a variable that lets the program now if its the first time the user has seen this room and a variable the detects if the player has been defeated. 
    defeat_check = False
    objects_explored_number = 0
    if game_data['player_location'] == list(current_dungeon.keys())[-1]:
        final_room = True
    else:
        final_room = False
    first_time_in_room = True
    # this block of text displays the rooms data upon entry. 
    print(f'{name} arrives at a {current_dungeon[game_data["player_location"]]["name"]}. {current_dungeon[game_data["player_location"]]["description"]}')
    print(f'\nIn the immediate area {name} can see.')
    for objs in current_dungeon[game_data["player_location"]]["objects"]:
        word = objs['name']
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            a_an = 'An '
        else:
            a_an = 'A '
        print(f"\t{a_an + word.lower()}")
    # if its the final room a special message is displayed
    if final_room == True:
        print(f"In the distance, a path vanishes over the horizon leading to a new adventure.")
    else:
        doors_list = list(current_dungeon[game_data['player_location']]['doors'].keys())
        print(f'\nTo the {doors_list[0]}, {doors_list[1]} and {doors_list[2]}, {name} can exit the area.')
        for directions in doors_list:
            print(f"\t{directions}:\t{current_dungeon[game_data['player_location']]['doors'][directions]['description']}")
    # this while loop is the while loop for exploring the room
    while True:
        # reload the game and save data at the start of each loop to make sure we are working with the most current data. 
        game_data = load_game_data()
        player_data = load_player_data()
        current_dungeon = game_data['dungeon_dic']
        # if its not the first time the player has seen this room. the program displays a simplised version of the info given above. 
        if first_time_in_room != True:
            print(f"{current_dungeon[game_data['player_location']]['name']}\n{current_dungeon[game_data['player_location']]['description']}")
        else:
            first_time_in_room = False
        # the menu that the player uses to make choices within the room. 
        print('\nWhat would you like to do?\n\t1:\tExamine an object.\n\t2:\tLeave the area.')
        # this while loop prevents the player making any other choices then what is allowed by the room. 
        while True:
            room_choice = input('\nPlease select an option.')
            try:
                int(room_choice)
            except Exception:
                print('Unrecognised input.')
                continue
            else:
                if int(room_choice) not in [1, 2]:
                    print('Unrecognised input.')
                else:
                    break
        # this section will give menues to allow the player to interact with the objects and doors. 
        # 1 is objects
        if int(room_choice) == 1:
            obj_num = 0
            print('\nPlease select the object you would like to examine.\n')
            for obs in current_dungeon[game_data["player_location"]]['objects']:
                obj_num += 1
                if obs['searched'] == False:
                    print(f'\t{obj_num}:\t{obs["name"]}')
                else:
                    print(f'\t{obj_num}:\t{obs["name"]}\tAlready examined')
            print(f"\tb:\tBack.\n")
            while True:
                object_choice = input('Your selection?\t')
                if str(object_choice) != 'b' and str(object_choice) not in list(str(x) for x in range(1, obj_num + 1)):
                    print('Unrecognised input.')
                    continue
                else:
                    break
            if object_choice == 'b':
                continue
            else:
                chosen_object = current_dungeon[game_data["player_location"]]['objects'][int(object_choice)-1]
                print(f'\n{name} approaches the {chosen_object["name"]}...')
                if chosen_object['enemies'] !=  None:
                    if len(chosen_object['enemies']) > 1:
                        print(f'\n{num2words(len(chosen_object["enemies"]))} enemies jump out from behind the {chosen_object["name"]}.')
                    else:
                        print(f"\nOne enemy jumps out from behind the {chosen_object['name']}.")
                    combat_result = combat(chosen_object['enemies'])
                    if combat_result == False:
                        defeat_check = True
                        break
                    else:
                        chosen_object['enemies'] = None
                        xp_caclulator()
                    player_data = load_player_data()
                    game_data = load_game_data()
                    game_data['dungeon_dic'] = current_dungeon
                    save_game_data(game_data)
                if chosen_object['item'] != None:
                    print(f'\nLying on the floor behind the {chosen_object["name"]} {name} finds a {chosen_object["item"]["name"]}. {chosen_object["item"]["description"]}.')
                    player_data['items'].append(chosen_object['item']['name'])
                    print(f'\nThe {chosen_object["item"]["name"]} has been added to your inventory.')
                    save_player_data(player_data)
                else:
                    print(f'The ground behind the {chosen_object["name"]} is empty.')
                chosen_object['searched'] = True
                game_data = load_game_data()
                game_data['dungeo_dic'] = current_dungeon
                save_game_data(game_data)
                objects_explored_number += 1
        # 2 is doors. 
        else:
            if objects_explored_number < 3:
                print(f"{name} has not examined the surrounding area enough to move on.")
                continue
            else:
                
        break
    if defeat_check == True:
        print(f"{name}'s adventure has ended in death.")
        break
    break
    