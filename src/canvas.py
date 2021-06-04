from utils.data import pointNotInCanvas


def printCanvas(width, height):
    if width < 1 or height < 1:
        print("\n failed to create canvas \n")
    else:
        print("Canvas pattern is: ")
        for i in range(1, height + 1):
            for j in range(0, width + 2):
                if j == 0:
                    print("|", end="")
                elif j == width + 1:
                    print("|", end="")
                else:
                    print("*", end="")
            print()


def createCanvas(width, height):
    if width < 1 or height < 1:
        print("\n failed to create canvas \n")
        return None
    else:
        canvas = [[None for i in range(0, width + 2)] for j in range(0, height)]
        for i in range(0, len(canvas)):
            for j in range(0, len(canvas[0])):
                if j == 0:
                    canvas[i][j] = "|"
                elif j == len(canvas[1]) - 1:
                    canvas[i][j] = "|"
                else:
                    canvas[i][j] = " "
        return canvas


def modifyPixel(canvas, i, j, character):
    if pointNotInCanvas(canvas, i, j):
        print("error")
        return canvas
    else:
        canvas[i][j] = character
    return canvas


def writeCanvas2File(canvas, filename):
    with open(filename, "w") as myfile:
        for i in range(0, len(canvas)):
            lst = canvas[i]
            myfile.write("".join(map(str, lst)) + "\n")
    myfile.close()


if __name__ == "__main__":
    width = 3
    height = 4
    printCanvas(width, height)
    canvas = createCanvas(width, height)

    modifyPixel(canvas, 3, 4, "o")
    print(canvas)
    # writeCanvas2File(canvas, "output.txt")
