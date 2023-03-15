# set the initial experience level to 0
experience_level = 0

# define a dictionary to store the level names and their corresponding experience point values
level_data = {
    "Level 1": 10,
    "Level 2": 20,
    "Level 3": 30,
    "Level 4": 40,
    "Level 5": 50
}


# define a function to simulate winning a level and updating the experience level
def win_level(level_name):
    global experience_level  # use the global experience_level variable
    level_points = level_data[level_name]  # get the experience point value for the level
    experience_level += level_points  # increase experience_level by the level's point value
    print("You won", level_name + "!", "You earned", level_points, "experience points.")
    print("Your experience level is now", experience_level)


# define a function to track the player's highest experience level achieved
def track_highest_level():
    global experience_level  # use the global experience_level variable
    highest_level = max(level_data, key=level_data.get)  # get the level with the highest experience point value
    if experience_level >= level_data[highest_level]:
        print("Congratulations! You've achieved a new highest experience level of", experience_level)
    else:
        print("Your current highest experience level is still", highest_level)


# simulate winning levels and tracking the highest level achieved
win_level("Level 1")
track_highest_level()
win_level("Level 2")
track_highest_level()
win_level("Level 4")
track_highest_level()
win_level("Level 3")
track_highest_level()
win_level("Level 5")
track_highest_level()

