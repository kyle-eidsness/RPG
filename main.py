"""Allows the user to enter one of the letters in order to perform an action or quit"""
def performAction(action):
    """ Character looks, interacts, open's map, or attack's according to the user's input (action)"""
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
    """ Prints to console the actions the user can perform by inputting first letter"""
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
    """main code that asks user to enter an action to perform and 'outsources' performing the action"""
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