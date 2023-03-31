# Title : RPG - Simple Menu
# Coder Name: Kyle Eidsness
# Class: CS 30 Period 1
# Date: March 14, 2023
# -----------------------------------------------------------------------------
""" This is a simple RPG Menu

    User is given the option to walk, look around, interact, open map, and attack

    This is a skeleton for an improved program and the game continuously loops until
    the user quits"""
# -----------------------------------------------------------------------------

def performAction(action):
    """ Character looks, interacts, open's map, or attack's
    according to the user's input (action)"""
    if action == "w":
        print("You walk in a direction!")
    elif action == "l":
        print("You look!")
    elif action == "i":
        print("You interact")
    elif action == "m":
        print("You open the map")
    elif action == "a":
        print("You attack")


def printOptions():
    """ Prints to console the actions the user can
    perform by inputting first letter"""
    print("""Actions:
    *(W)alk
    *(L)ook
    *(I)nteract
    *(M)ap
    *(A)ttack
    *(O)ptions
    *(Q)uit\n""")


# prints out the actions user can perform before running the program
printOptions()
while True:
    """main code that asks user to enter an action to perform and 
    'outsources' performing the action"""
    userInput = input("Enter an action (or o for options): ").lower()[:1]
    if userInput == "q":
        # Exits program
        break
    elif userInput == "o":
        printOptions()
    elif userInput in ["w", "l", "i", "m", "a"]:
        performAction(userInput)
    else:
        # Tells user input was invalid
        print(f"\033[91m'{userInput}' is not a valid action\033[0m")
