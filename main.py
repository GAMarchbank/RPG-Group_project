import json
from statistics import mean
import glob
from run_full_battle import *

def CheckUserInput(number):  # to check user input is a number

        try:
            #convert into an integer
            value=int(number)
            return(value,True)
        except ValueError:
            print('That is not a number, please try again: ')
            return(-1,False)


def CheckNameDuplicates(name):
    txtFiles = glob.glob("*.txt")  #get list of possibles saved games
    #print(txtFiles)
    nameCheck=name + '.txt'
    
    for file in txtFiles:

        if file==nameCheck:
            if file=='game_data.txt':
                print('That would be confusing. Try again. ')
                return(False)
            elif file=='Exit.txt':
                print('That would be confusing. Try again. ')
                return(False)
            else:
                print('The name '+ name + ' is taken, please try agan: ')
                return(False)

        
    return(True)

def listSavedGames():
    txtFiles = glob.glob("*.txt")  #get list of possibles saved games

    saveList={}
    saveGame=1
    select=0

    for item in txtFiles:
        if item!='game_data.txt':
            saveList[saveGame]=item[:-4]
            saveGame+=1
    saveList[saveGame]='Exit'
    print(saveList)
   
   
    saveGame=0
    loop=False
    while loop==False:
        for item in saveList:
            saveGame+=1
            print(f"{saveGame}. {saveList[item]}.")
                

                
        select=input('\nPlease select option. ')
        select,loop=CheckUserInput(select)
  
        
    print('you chose ',select)
    player = saveList[select]
    print(player)
        
    return(player)
 



def setupGameData(player):
    attacks = [{'name': 'Scratch', 'attack_modifer': 1, 'lvl_avilble': 0, 'description': 'Rake the foe with long, unclean finger nails.', 'effects': ['burn'], 'mult_targets': 'single'}]

    items = [{'name': 'ball', 'description': 'round object used for fun', 'combat_check': True, 'effects': {'type': 'escape', 'impact': False}}, {'name': 'great vibes', 'description': 'a feeling of mild contentment.', 'combat_check': True, 'effects': {'type': 'healing', 'impact': 1}}]

    effects = [{'name': 'burn', 'description': 'hot flame applied to skin', 'effects': {'type': 'damage', 'impact': 5}}]

    player_data = {'name': player,'level': 1, 'hp': 10, 'a_p': 10, 'd_p': 40, 's_p': 0, 'aim': 50, 'items': ['ball', 'great vibes'], 'attacks': ['Scratch'], 'max_hp': 10}

    ai_personality_types = ['timid', 'aggressive', 'smart', 'resourceful', 'wild', 'average']


    game_data = {'attacks': attacks, 'items': items, 'effects': effects, 'personality_types': ai_personality_types}

    p_d = json.dumps(player_data)
    g_d = json.dumps(game_data)




#create game data file if it does not exist
    try:
        with open('game_data.txt', 'r') as fp:
            pass
       

    except IOError:
        #print('File not found, will create a new one.')
        with open('game_data.txt', 'w')as file:
            file.write(g_d)


#create player data for player if it does not exist
    playerfile=player+'.txt'
    try:
        with open(playerfile, 'r') as fp:
            print('Welcome back ',player)
        

    except IOError:
        print('Welcome newbie',player)
       
        with open(playerfile, 'w')as file:
            file.write(p_d)
    return(player_data)

gamenum=0

while gamenum !=4:
    loop=False
    while loop==False:
        print('\nGame options.\n')
        print('1. Start a new game.')    #menu for different games
        print('2. Load a saved game.')
        print('3. Test a battle.')
        print('4. Exit')
        select=input('\nPlease select option. ')
        gamenum,loop=CheckUserInput(select)

    if gamenum==1:
        check=False
        
        while check==False:  
            player=input('What is your name: ')
            check=CheckNameDuplicates(player)
        player_data=setupGameData(player)
        print(player_data)
        input('Press any key to return to the menu. ')

    elif gamenum==2:
        player=listSavedGames()
        if player!='Exit':
            player_data=setupGameData(player)
            print(player_data)
        input('Press any key to return to the menu. ')

    elif gamenum==3:
        combat()
        input('Press any key to return to the menu. ')

    elif gamenum==4:
        print('Goodbye')  

    else:
        print('Try again. ')






