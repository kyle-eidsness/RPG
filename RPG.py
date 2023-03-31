import time
import setup
import random

"""Spartans = "Spartans"
Forest = "Forest"
Tomb = "Tomb"
Wall = "Wall"
Mountain = "\033[37mMountain\033[0m"""""
display = [
    [" Spartans ", " Spartans ", "", "  Forest  ", "  Forest  "],
    ["Giants", "", "", "Forest", "Tomb"],
    ["Bandits", "Giants", "", "", "Forest"],
    ["\033[37mMountain\033[0m", "\033[37mMountain\033[0m", "", "Wall", "Wall"],
    ["Entrance", "Giants", "Wall", "Athenian", "Athenian"]
]

main_map = f"""
+----------+----------+----------+----------+----------+
|{display[0][0]}|{display[0][1]}|{display[0][2]}|{display[0][3]}|{display[0][4]}|
+----------+----------+----------+----------+----------+
|{display[1][0]}|{display[1][1]}|{display[1][2]}|{display[1][3]}|{display[1][4]}|
+----------+----------+----------+----------+----------+
|{display[2][0]}|{display[2][1]}|{display[2][2]}|{display[2][3]}|{display[2][4]}|
+----------+----------+----------+----------+----------+
|{display[3][0]}|{display[3][1]}|{display[3][2]}|{display[3][3]}|{display[3][4]}|
+----------+----------+----------+----------+----------+
|{display[4][0]}|{display[4][1]}|{display[4][2]}|{display[4][3]}|{display[4][4]}||
+----------+----------+----------+----------+----------+"""


labyrinth_map = setup.labyrinth_map
greek_map = setup.greek_map
minotaur_labyrinth = setup.minotaur_labyrinth
player_position = [1, 1]  # players current position on map (y, x) (also start position)
user_equipment = []  # users inventory
current_location = greek_map  # determines which map to use
quitProgram = False


def generateWeapon():
    """Randomly generates weapon and stores in user's inventory"""
    names = ["Great Sword", "Sword of Apostate", "Dire Flail", "Scimitar", "Morningstar", "War Hammer"]
    dice_options = [4, 6, 8, 10, 24]
    dice = dice_options[random.randint(0, 4)]
    num_dice = random.randint(4, 23) // dice
    if num_dice == 0:
        num_dice = 1
    bonus = random.randint(2, 5)
    return f"{names[random.randint(0, 5)]} ({num_dice}d{dice} + {bonus})"


def printBreak(pos):
    if pos == "e":
        print("\033[0m", end="")
    if pos == "s":
        print("")
    # print("==============================================================================")
    print("------------------------------------------------------------------------------")
    if pos == "s":
        print("\033[1m", end="")


def changePosition(direction):
    """ Moves the character north, east, south, or west based on user's input (direction) if allowed"""
    if player_position[0] >= 1:
        north_tile = current_location[player_position[0] - 1][player_position[1]]
    if player_position[0] <= 3 and current_location == greek_map:
        south_tile = current_location[player_position[0] + 1][player_position[1]]
    elif player_position[0] <= 7 and current_location == minotaur_labyrinth:
        south_tile = current_location[player_position[0] + 1][player_position[1]]
    if player_position[1] <= 3 and current_location == greek_map:
        east_tile = current_location[player_position[0]][player_position[1] + 1]
    elif player_position[1] <= 7 and current_location == minotaur_labyrinth:
        east_tile = current_location[player_position[0]][player_position[1] + 1]
    if player_position[1] >= 1:
        west_tile = current_location[player_position[0]][player_position[1] - 1]

    if direction == "n" and player_position[0] >= 1 and north_tile != "wall" and north_tile != "mountain":
        player_position[0] -= 1
    elif direction == "e" and player_position[
        1] <= 3 and current_location == greek_map and east_tile != "wall" and east_tile != "mountain":
        player_position[1] += 1
    elif direction == "e" and player_position[
        1] <= 7 and current_location == minotaur_labyrinth and east_tile != "wall" and east_tile != "mountain":
        player_position[1] += 1
    elif direction == "s" and player_position[
        0] <= 3 and current_location == greek_map and south_tile != "wall" and south_tile != "mountain":
        player_position[0] += 1
    elif direction == "s" and player_position[
        0] <= 7 and current_location == minotaur_labyrinth and south_tile != "wall" and south_tile != "mountain":
        player_position[0] += 1
    elif direction == "w" and player_position[1] >= 1 and west_tile != "wall" and west_tile != "mountain":
        player_position[1] -= 1
    elif direction == "m":
        if current_location == greek_map:
            print(main_map)
        else:
            print(labyrinth_map)
    else:
        print("\033[91mYou cannot move in that direction\033[0m")
    # returns new location to player
    print(f"Location: \033[32m{current_location[player_position[0]][player_position[1]]}\033[0m")


def printDirections():
    # current_position = current_location[player_position[0]][player_position[1]]
    if player_position[0] >= 1:
        north_tile = current_location[player_position[0] - 1][player_position[1]]
    if player_position[0] <= 3 and current_location == greek_map:
        south_tile = current_location[player_position[0] + 1][player_position[1]]
    elif player_position[0] <= 7 and current_location == minotaur_labyrinth:
        south_tile = current_location[player_position[0] + 1][player_position[1]]
    if player_position[1] <= 3 and current_location == greek_map:
        east_tile = current_location[player_position[0]][player_position[1] + 1]
    elif player_position[1] <= 7 and current_location == minotaur_labyrinth:
        east_tile = current_location[player_position[0]][player_position[1] + 1]
    if player_position[1] >= 1:
        west_tile = current_location[player_position[0]][player_position[1] - 1]

    printBreak("s")
    print(f"Directions:")
    if player_position[0] >= 1 and north_tile != "wall" and north_tile != "mountain":
        print("    *(N)orth")
    if player_position[1] <= 3 and current_location == greek_map and east_tile != "wall" and east_tile != "mountain":
        print("    *(E)ast")
    elif player_position[
        1] <= 7 and current_location == minotaur_labyrinth and east_tile != "wall" and east_tile != "mountain":
        print("    *(E)ast")
    if player_position[0] <= 3 and current_location == greek_map and south_tile != "wall" and south_tile != "mountain":
        print("    *(S)outh")
    elif player_position[
        0] <= 7 and current_location == minotaur_labyrinth and south_tile != "wall" and south_tile != "mountain":
        print("    *(S)outh")
    if player_position[1] >= 1 and west_tile != "wall" and west_tile != "mountain":
        print("    *(W)est")
    printBreak("e")


def interact():
    global current_location
    global player_position
    cur_tile = current_location[player_position[0]][player_position[1]]
    if cur_tile == "labyrinth entrance":
        print("You have entered the minotaur's labyrinth!")
        current_location = minotaur_labyrinth
        player_position = [8, 0]
    elif cur_tile == "ancient tomb":
        user_equipment.append("labyrinth map")
        user_equipment.append(generateWeapon())
        print(", ".join(user_equipment))
    elif cur_tile == "chest" or cur_tile == "war supplies" or cur_tile == "bandit outpost":
        user_equipment.append(generateWeapon())
        print(", ".join(user_equipment))


def printOptions():
    """ Prints to console the actions the user can perform by inputting first letter"""
    printBreak("s")
    print("""Actions:
    *(W)alk
    *(L)ook
    *(I)nteract
    *(M)ap
    *(E)quipment
    *(A)ttack
    *(Q)uit""")
    printBreak("e")


printOptions()
while not quitProgram:
    userInput = input("\nEnter an action (or o for options): ").lower()[:1]
    if userInput == "q":
        # Exits program
        break
    elif userInput == "o":
        printOptions()
    elif userInput == "w":
        # shows the directions the player can move based on the current map they are on
        while True:
            printDirections()
            userDirection = input("\nChoose direction (or b for back): ").lower()[0]
            if userDirection == "b":
                break
            elif userDirection == "q":
                quitProgram = True
                break
            changePosition(userDirection)
            time.sleep(0.5)
    elif userInput == "l":
        print(setup.tiles[current_location[player_position[0]][player_position[1]]]["description"])
    elif userInput == "i":
        interact()
    elif userInput == "m":
        if current_location == greek_map:
            print(main_map)
        else:
            print(labyrinth_map)
    elif userInput == "e":
        if len(user_equipment) >= 1:
            print(", ".join(user_equipment))
        else:
            print("You have no equipment in your inventory!")
    elif userInput == "a":
        print("You attack")
    else:
        # Tells user input was invalid
        print(f"\033[91m'{userInput}' is not a valid action\033[0m")

print("Thanks for playing!")
