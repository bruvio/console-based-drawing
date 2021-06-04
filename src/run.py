from canvas import createCanvas

# Import the modules needed to run the script.
import sys
import os

from utils.data import printCanvas

# Main definition - constants
menu_actions = {}
canvas = []
# =======================
#     MENUS FUNCTIONS
# =======================
# Main menu


def main_menu():

    os.system("clear")
    print("Welcome,\n")
    print("This is a console based drawing program \n")
    print("do you want to draw a canvas?\n")
    print("1. Yes")
    print("2. No")
    print("\nq. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    os.system("clear")
    ch = choice.lower()
    if ch == "":
        menu_actions["main_menu"]()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions["main_menu"]()
    return


# def exec_menu(choice):
#     os.system("clear")
#     ch = choice.lower()
#     if ch == "":
#         menu_actions["main_menu"]()
#     else:
#         try:
#             menu_actions[ch]()
#         except KeyError:
#             print("Invalid selection, please try again.\n")
#             menu_actions["main_menu"]()
#     return


# Menu 1
def menu1():
    print("\n")
    x = []
    while len(x) != 3:
        try:
            x = list(
                map(str, input("The command to draw a canvas is `C w h: ").split())
            )
            if (type(x[0]) == str) and (x[0] == "C"):
                try:
                    width = int(x[1])
                    height = int(x[2])
                    canvas = createCanvas(width, height)
                    printCanvas(canvas)
                except Exception:
                    print("Invalid selection, please try again.\n")
                    menu_actions[1]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions[1]()

    return


# Menu 2
def menu2():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("q. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions["main_menu"]()


# Exit program
def exit():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    "main_menu": main_menu,
    "1": menu1,
    "2": menu2,
    "9": back,
    "0": exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
