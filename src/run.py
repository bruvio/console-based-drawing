from canvas import createCanvas, writeCanvas2File, fillArea, drawRectangle, drawLine

# Import the modules needed to run the script.
import sys
import os
from utils.data import printCanvas

# Main definition - constants
menu_actions = {}

# =======================
#     MENUS FUNCTIONS
# =======================
# Main menu


def main_menu(canvas):

    os.system("clear")
    print("Welcome,\n")
    print("This is a console based drawing program \n")
    print("do you want to draw a canvas?\n")
    print("1. Yes")
    # print("2. No")
    print("\nq. Quit")
    choice = input(" >>  ")
    exec_menu(choice, canvas)
    return


# Execute menu
def exec_menu(choice, canvas):
    os.system("clear")
    ch = choice.lower()
    if ch == "":
        menu_actions["main_menu"]()
    if ch == "q":
        menu_actions["q"]()
    else:

        if int(choice) == 1:
            try:
                menu1()
            except Exception:
                print("error creating canvas")
        if int(choice) == 2:
            try:
                menu2(canvas)
            except Exception:
                print("error drawing line in canvas")
        if int(choice) == 3:
            try:
                menu3(canvas)
            except Exception:
                print("error creating rectangle in canvas")
        if int(choice) == 4:
            try:
                menu4(canvas)
            except Exception:
                print("error filling canvas")
        if int(choice) == 5:
            try:
                menu5(canvas)
            except Exception:
                print("error saving canvas")


def draw_menu(canvas):
    os.system("clear")
    print("Here is your canvas,\n")
    printCanvas(canvas)
    print("\n")
    print("What do you want to do now?")
    print("\n")
    print("1. Draw a new canvas")
    print("2. Draw a line")
    print("3. Draw a rectangle")
    print("4. Fill the canvas")
    print("5. Save the canvas to file")
    print("\nq. Quit")
    choice = input(" >>  ")
    exec_menu(choice, canvas)


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
                    draw_menu(canvas)
                except Exception:
                    print("Invalid selection, please try again.\n")
                    menu_actions[1]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions[1]()

    return canvas


def menu2(canvas):
    print("\n")
    x = []
    while len(x) != 5:
        try:
            x = list(
                map(
                    str,
                    input("The command to draw a line is L x1 y1 x2 y2: ").split(),
                )
            )
            if (type(x[0]) == str) and (x[0] == "L"):
                try:
                    x1 = int(x[1])
                    y1 = int(x[2])
                    x2 = int(x[3])
                    y2 = int(x[4])

                    canvas = drawLine(canvas, x1, y1, x2, y2)

                    printCanvas(canvas)
                    draw_menu(canvas)
                except Exception:
                    print("Invalid selection, please try again.\n")
                    draw_menu(canvas)
        except KeyError:
            print("Invalid selection, please try again.\n")
            draw_menu(canvas)

    return canvas


def menu3(canvas):
    print("\n")
    x = []
    while len(x) != 5:
        try:
            x = list(
                map(
                    str,
                    input("The command to Draw a rectangle is R x1 y1 x2 y2: ").split(),
                )
            )
            if (type(x[0]) == str) and (x[0] == "R"):
                try:
                    x1 = int(x[1])
                    y1 = int(x[2])
                    x2 = int(x[3])
                    y2 = int(x[4])
                    canvas = drawRectangle(canvas, x1, y1, x2, y2)
                    printCanvas(canvas)
                    draw_menu(canvas)
                except Exception:
                    print("Invalid selection, please try again.\n")
                    draw_menu(canvas)
        except KeyError:
            print("Invalid selection, please try again.\n")
            draw_menu(canvas)

    return canvas


def menu4(canvas):
    print("\n")
    x = []
    import pdb

    # pdb.set_trace()
    while len(x) != 4:
        try:
            x = list(
                map(
                    str,
                    input(
                        "The command to fill an area containing a point is B x y c: "
                    ).split(),
                )
            )
            pdb.set_trace()
            if (type(x[0]) == str) and (x[0] == "B"):
                try:
                    x = int(x[1])
                    y = int(x[2])
                    colour = x[3]

                    canvas = fillArea(canvas, x, y, colour)

                    printCanvas(canvas)
                    draw_menu(canvas)
                except Exception:
                    print("Invalid selection, please try again.\n")
                    draw_menu(canvas)
        except KeyError:
            print("Invalid selection, please try again.\n")
            draw_menu(canvas)

    return canvas


def menu5(canvas):
    print("\n")
    x = []
    # import pdb

    # pdb.set_trace()
    while len(x) != 2:
        try:
            x = list(
                map(
                    str,
                    input(
                        "The command to save the current canvas to file is  s filename: "
                    ).split(),
                )
            )
            if (type(x[0]) == str) and (x[0] == "S"):
                try:
                    filename = x[1]

                    canvas = writeCanvas2File(canvas, filename)
                    draw_menu(canvas)
                except Exception:
                    print("Invalid selection, please try again.\n")
                    draw_menu(canvas)
        except KeyError:
            print("Invalid selection, please try again.\n")
            draw_menu(canvas)

    return canvas


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
    "3": menu3,
    "4": menu4,
    "5": menu5,
    "q": exit,
}


# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    canvas = None
    main_menu(canvas)
