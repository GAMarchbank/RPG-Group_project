from locations import create_dungeon, generate_location
from run_full_battle import combat
from player_game_data_write_file import new_game, player_new_game, load_game_data, load_player_data, save_game_data, save_player_data
from xp_calc import xp_caclulator
import time
import os.path



print('==================')
print('Welcome to The RPG')
print('==================')
time.sleep(2)
if os.path.exists('player_data.txt'):
    print('1:\tContinue\n2:\tNew Game')
    path_check = True
else:
    print('1:\tNew Game')
    path_check = False
while True:
    main_menu_choice = input('Please select a menu option?')
    try:
        int(main_menu_choice)
    except Exception:
        print('Unrecognised input.')
        continue
    else:
        if (path_check == True and int(main_menu_choice) not in [1, 2]) or (path_check == False and int(main_menu_choice) != 1):
            print('Unrecognised input.')
            continue
        else:
            break
        
if path_check == True and int(main_menu_choice) == 1:
    game_data = load_game_data()
    player_data = load_player_data()
    new_game_bool = False
    print('\nLoading previous game.\n')
    time.sleep(2)
    print(f'You rejoin the action where our main character {player_data["name"]} has just arrived at a {game_data["dungeon_dic"][game_data["player_location"]]["name"]}.\n')
    current_dungeon = game_data['dungeon_dic']
else:
    game_data = new_game()
    player_data = player_new_game()
    new_game_bool = True
    print('\nYour jouney begins here...\n')
    time.sleep(2)
    current_dungeon = create_dungeon()
    game_data['player_location'] = 1
    game_data['dungeon_dic'] = current_dungeon
    save_game_data(game_data)
    print(f"Our story begins with our main character {player_data['name']} arriving at a {game_data['dungeon_dic'][game_data['player_location']]['name']}.\n")

name = player_data['name']

while True:
    # double nest this while statment so the player can look through multiple objects. 
    # have an object recognition variable so we can check how many objects the player has looked at per room. 
    # display room name, description, populate objects, doors
    print(f'{name} arrives at a {current_dungeon[game_data["player_location"]]["name"]}. {current_dungeon[game_data["player_location"]]["description"]}')
    print(f'\nIn the immediate area {name} can see.')
    for objs in current_dungeon[game_data["player_location"]]["objects"]:
        print(f"\t{objs['name']}")
    break
    