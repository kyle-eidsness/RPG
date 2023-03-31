import random

Wall = "\033[37mWall\033[0m"
Enter = "\033[32mEnter\033[0m"
labyrinth_map = f"""
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|         |         |    ?    |  {Wall}   |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|         |  {Wall}   |  {Wall}   |  {Wall}   |         |  {Wall}   |  {Wall}   |  {Wall}   |         |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|         |         |         |  {Wall}   |         |         |         |  {Wall}   |    ?    |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|         |  {Wall}   |         |  {Wall}   |         |  {Wall}   |         |  {Wall}   |  {Wall}   |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|         |  {Wall}   |         |         |         |  {Wall}   |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|         |  {Wall}   |  {Wall}   |  {Wall}   |  {Wall}   |  {Wall}   |  {Wall}   |  {Wall}   |         |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|    ?    |  {Wall}   |         |         |         |         |         |  {Wall}   |         |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|  {Wall}   |  {Wall}   |         |  {Wall}   |  {Wall}   |  {Wall}   |         |  {Wall}   |         |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|  {Enter}  |         |         |  {Wall}   |    ?    |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+---------+---------+"""


# database of different tiles and their description
tiles = {
    "empty": {
        "description": "Nothing interesting seems to be around"
    },
    "spartan camp": {
        "description": "A military outpost heavily fortified with the equipment to treat wounds and resupply"
    },
    "forest": {
        "description": "Below the towering trees, the dense foliage suffocates the floor. Visibility is incredibly low"
    },
    "giant's path": {
        "description": "A path travelled commonly by the giants. Be careful, you might run into one!"
    },
    "wolf pack": {
        "description": "A pack of wolves exploiting the low visibility in the forest"
    },
    "ancient tomb": {
        "description": "The entrance to an ancient tomb found deep in the jungle. Finding it is a miracle!"
    },
    "bandit outpost": {
        "description": "A group of bandits that have been taking high value spartan captives"
    },
    "mountain": {
        "description": "Steep, treacherous, terrain that even the giant's struggle to traverse. Not fit for climbing"
    },
    "athenian wall": {
        "description": "A heavily fortified wall protecting the inner city of Athens"
    },
    "war supplies": {
        "description": "Military supplies meant for fighting sparta"
    },
    "temple of athena": {
        "description": "People come from all around to give gifts to athena. Surprisingly little security"
    },
    "labyrinth entrance": {
        "description": "The floor collapsed to reveal a massive opening leading deep underground"
    },
    "wall": {
        "description": "You shouldn't be on this tile!"
    },
    "snakes": {
        "description": "Snakes seem to have infested every deep "
    },
    "chest": {
        "description": "Contains a randomly generated weapon (name not attached to stats)"
    },
    "minotaur": {
        "description": "A mythical creature that is half human, half bull. Appears to be angry..."
    }
}

# each element of a list is a tile which together form a grid the player can explore
greek_map = [
    ["spartan camp", "spartan camp", "empty", "forest", "forest"],
    ["giant's path", "empty", "empty", "wolf pack", "ancient tomb"],
    ["bandit outpost", "giant's path", "empty", "empty", "forest"],
    ["mountain", "mountain", "empty", "athenian wall", "athenian wall"],
    ["labyrinth entrance", "giant's path", "athenian wall", "war supplies", "temple of athena"]
]

labyrinth_random = ["", "", ""]
labyrinth_random[random.randint(0, 2)] = "minotaur"
while "chest" not in labyrinth_random:
    chest_location = random.randint(0, 2)
    if labyrinth_random[chest_location] != "minotaur":
        labyrinth_random[chest_location] = "chest"
count = 0
for item in labyrinth_random:
    if item == "":
        labyrinth_random[count] = "snake"
    count += 1

# a grid of a maze the player must navigate in order to find the minotaur
minotaur_labyrinth = [
    ["empty", "empty", labyrinth_random[1], "wall", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "empty"],
    ["empty", "empty", "empty", "wall", "empty", "empty", "empty", "wall", labyrinth_random[0]],
    ["empty", "wall", "empty", "wall", "empty", "wall", "empty", "wall", "wall"],
    ["empty", "wall", "empty", "empty", "empty", "wall", "empty", "empty", "empty"],
    ["empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty"],
    [labyrinth_random[2], "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty"],
    ["wall", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "empty"],
    ["empty", "empty", "empty", "wall", "snake", "empty", "empty", "empty", "empty"]
]