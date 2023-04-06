import json
import random
import items_generator

#TODO - SEE COMMENTS IN investigate_object function below

#GEORGE = BATTLES
#TANYA = TBC
#JUSTIN = GENERATE ITEMS E.G. HEALTH, WEAPONS AND ATTACKS
#TOBI = XP AND LEVELLING UP
#GEORGE = BASE CODE
#FABIAN = ENEMIES LIST
# QUESTIONS: Do I need to push the found item to the player_data file or is there a function somewhere I can call for that?

# Using 'with' closes the file after use. As 'file' creates a variable
with open('player_data.txt', 'r')as file:
    #assigns parsed contents to the variable 'player_data'
    player_data = json.load(file)

#THIS SAVE FUNCTION IS POSSIBLY NEEDED IN FUTURE VERSIONS
#def save(data):
    #data = json.dumps(data)
    #with open('player_data.txt', 'w')as file:
        #file.write(data)

#descript_lst = ['dark', ]

# List of locations including description and links to other destinations
locations = {
    'forest' : {
        'name':'forest',
        'description':'dark',
        'objects': {
            1:'Rotten treetrunk',            
            2:'Animal bone',
            3:'Spotted mushrooms'
        },
        'destinations': {
            4:'Meadow', 
            5:'Path'
        }
    },
    'meadow' : {
        'name':'meadow',
        'description':'verdant',
        'objects': {
            1:'Fox hole',
            2:'Fairy ring',
            3:'Yellow buttercups'
        },
        'destinations': {
            4:'Forest',
            5:'Hut',
            6:'Hilltop',
            7:'Lake'
        }
    },
    'alleyway' : {
        'name':'alleyway',
        'description':'dank',
        'objects': {
            1:'Broken bottle',
            2:'Old barrel',
        },
        'destinations': {
            3:'Tavern',
            4:'Hut'
        }
    },
    'hut' : {
        'name':'hut',
        'description':'derelict',
        'objects': {
            1:'Mildewed bed',
            2:'Rusty tin',
            3:'Old newspaper'
        },
        'destinations': {
            4:'Cellar',
            5:'Alleyway',
            6:'Meadow'
        }
    },
    'lake' : {
        'name':'lake',
        'description':'glacial',
        'objects': {
            1:'Large stone',
            2:'Animal footprints',
            3:'Fish head'
        },
        'destinations': {
            4:'Meadow',
            5:'Mountainside'
        }
    },
    'mountainside' : {
        'name':'mountainside',
        'description':'rocky',
        'objects': {
            1:'Gorse bush',
            2:'Animal bone'
        },
        'destinations': {
            3:'Lake',
            4:'Bridge'
        }
    },
    'hilltop' : {
        'name':'hilltop',
        'description':'windswept',
        'objects': {
           1:'Rabbit hole',
           2:'Half buried necklace'
        },
        'destinations': {
            3:'Meadow',
            4:'Beach'
        }
    },
    'tavern' : {
        'name':'tavern',
        'description':'smoky',
        'objects': {
            1:'Dirty tankard',
            2:'Stew pot',
            3:'Three legged stool'
        },
        'destinations': {
            4:'Hut',
            5:'Alleyway'
        }
    },
    'path' : {
        'name':'path',
        'description':'muddy',
        'objects': {
            1:'Yellow pebble',
            2:'Apple tree',
            3:'Rose bush'
        },
        'destinations': {
            4:'Meadow',
            5:'Forest'
        }
    },
    'beach' : {
        'name':'beach',
        'description':'cold',
        'objects': {
            1:'Twisted driftwood',
            2:'Large seashell',
            3:'Clump of seaweed'
        },
        'destinations': {
            4:'Hilltop',
            5:'Harbour'
        }
    },
    'harbour' : {
        'name':'harbour',
        'description':'ramshackle',
        'objects': {
            1:'Length of rope',
            2:'Blue paint',
            3:'Small rowboat'
        },
        'destinations': {
            4:'Beach'
        }
    },
    'bridge' : {
        'name':'bridge',
        'description':'rickety',
        'objects': {
            1:'Rusty nail',
            2:'Tarnished ring'
        },
        'destinations': {
            3:'Mountainside',
            4:'Path'
        }
    },
    'cellar' : {
        'name':'cellar',
        'description':'damp',
        'objects': {
            1:'Pile of boxes',
            2:'Black tophat',
            3:'Wine bottle'
        },
        'destinations': {
            4:'Hut'
        }
    }
}

#extracting location keys for random generator
loc_list = list(locations)

#return random location from loc_list
def generate_location() :
    #returns a random location name
    return random.choice(loc_list)

# setting current location
current_location = generate_location()

#function to create the 'dungeon' i.e. series of locations/rooms to explore for each game instance
def create_dungeon() :
    #variable to set random number of linked locations/rooms
    num_of_rooms = random.choice(range(1,8))
    print(num_of_rooms)
    dungeon = {}
    i = 1
    while i <= num_of_rooms :
        print(num_of_rooms)
        random_location = generate_location()
        dungeon.update({random_location : locations[random_location]})
        print(i)
        i += 1
        print(random_location)
    print(dungeon)

create_dungeon()

#setting the random game_item variable by calling the inventory_edit function from items_generator file
game_item = items_generator.inventory_edit()

#function to decide whether an object has a hidden item attached when investigated
def investigate_object() :
    #variable to decide whether or not an item is attached to a physical object in locations
    is_item = random.choice([True, False])

    #if is_item is True, declare attached_item to be the random game_item
    if (is_item == True) :
        attached_item = game_item
        #Todo 
        # - potentially look at how the received item is pushed to the player inventory
        # - code to inform player of received item on terminal

#CURRENTLY REDUNDANT CODE THAT MIGHT BE USEFUL FOR THE MAIN CODE GEORGINA IS DOING

# Function to print current location with description
def print_location(current_location) :
    loc = locations[current_location]['name']
    desc = locations[current_location]['description']
    print(f'You are in a {desc} {loc}.')


# Function to print objects in current location
def list_objects(current_location) :
    print(f'You look around and see: \n')
    for key, value in locations[current_location]['objects'].items():
        print(key, ': ', value)
    print(f'\nFrom here, you can travel to: \n')
    for key, value in locations[current_location]['destinations'].items():
        print(key, ': ', value)

# Function to offer choices and accept user choice
def make_choice(current_location) :
    #set current_location as global to reassign it
    numbers_of_objects = list(locations[current_location]['objects'].keys())
    numbers_of_destinations = list(locations[current_location]['destinations'].keys())
    user_choice = input('What do you want to do? Choose 1 to investigate an item, or 2 to leave.')
    #if user chooses option 1, list available objects to investigate
    if(user_choice == '1') :  
        #NEED TO IMPLEMENT WHAT HAPPENS WHEN USER INVESTIGATES AN OBJECT!
        item_choice = input(f'Which item do you want to investigate? Choose a number: {numbers_of_objects}')
     #if user chooses option 2, list available destinations to go to
    elif(user_choice == '2') :
        #ADD CODE IF USER SELECTS INCORRECT OPTION
        new_location_number = int(input(f'Where do you want to go? Choose a number: {numbers_of_destinations}'))
        #reassign current_location
        current_location = str.lower((locations[current_location]['destinations'][new_location_number]))
        print(f'\n--------------You are travelling to {current_location}--------------\n')
        print_location(current_location)
        list_objects(current_location)
        make_choice(current_location)

print_location(current_location)

list_objects(current_location)

make_choice(current_location)