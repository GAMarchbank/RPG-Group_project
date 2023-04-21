import json


# functiom that increases the player level the player holds enough xp
def xp_caclulator():
    # starts by opening the player data file and extracting the player data
    with open('player_data.txt', 'r')as file:
        player_data = file.read()
    player_data = json.loads(player_data)
    # continues by calculating the xp multiplier which is part of the equation that works out the xp cap needed to incrase level.
    # the xp cap functions this way so that it is exponential, as you get high in level it becomes steadily harder to level up
    if player_data['level'] * 0.5 > 1:
        xp_multiplyer = 1
    else:
        xp_multiplyer = round(player_data['level'] * 0.5) 
    # this if statment activates if the player meets this xp cap
    if player_data['xp'] >= round((player_data['level'] * 1000) * xp_multiplyer):
        # the xp up to the level cap is removed from the players xp stores
        player_data['xp'] = player_data['xp'] - round((player_data['level'] * 1000) * xp_multiplyer)
        print('\n------------------------')
        print('You have gained a level!')
        print('------------------------\n')
        print(f'You have assended from level {player_data["level"]} to level {player_data["level"] + 1}.')
        # the players level is increased by 1
        player_data['level'] += 1
        # the player is then allowed to increase two statistics by 3 points
        num = 2
        while num != 0:
            print(f'You have {num} stat points to spend.\n')
            nums = 1
            # the program filters though the stats in teh player_data for the items that its reasonable to increase and allows teh player to select one of them
            stat_check_dic = {}
            for statistics in player_data:
                if statistics not in ['name', 'level', 'xp', 'location', 'items', 'attacks', 'hp']:
                    print(f"{nums}:\t{statistics}\t{player_data[statistics]}")
                    stat_check_dic[nums] = statistics
                    nums += 1
            # this while loop check that the player is inputing a number the corrently conforms to an availble statistic.
            while True:
                player_choice = input('Please choose a stat to increase.\t')
                try:
                    player_choice = int(player_choice)
                    if player_choice in range(1, nums+1):
                        break
                except Exception:
                    continue
            # prints out the information about that statisic and increases it by 3
            print(f"You've chosen to increase your {stat_check_dic[player_choice]}.\nYou'r {stat_check_dic[player_choice]} has risen from {player_data[stat_check_dic[player_choice]]} to {player_data[stat_check_dic[player_choice]]+3}.\n")
            player_data[stat_check_dic[player_choice]] += 3
            num -= 1
        # reopens the player_data file and dumps the data back into it.
        json_dump = json.dumps(player_data)
        with open('player_data.txt', 'w')as file:
            file.write(json_dump)
        # recalls upon the function itself to check if there are any more levels to be increased. 
        xp_caclulator()

            
        