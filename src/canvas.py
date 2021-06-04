from utils.data import (
    areHorz,
    areVert,
    drawHorizontalLine,
    drawVerticalLine,
    pointNotInCanvas,
)


def printEmptyCanvas(width, height):
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


def printCanvas(canvas):
    height = len(canvas)
    print("\n")
    for i in range(0, height):
        lst = canvas[i]
        print("".join(map(str, lst)))
    print("\n")


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


def drawLine(canvas, x1, y1, x2, y2):
    point1 = [x1, y1]
    point2 = [x2, y2]
    if pointNotInCanvas(canvas, x1, y1) or pointNotInCanvas(canvas, x2, y2):
        print("error")
        return canvas
    elif areVert(point1, point2):
        print("drawing vertical line")
        y = y1
        canvas = drawVerticalLine(canvas, x1, x2, y)
    elif areHorz(point1, point2):
        print("drawing horizontal line")
        x = x1
        canvas = drawHorizontalLine(canvas, x, y1, y2)
    else:
        print("drawing diagonal line not supported")
    return canvas


if __name__ == "__main__":
    width = 3
    height = 4
    printEmptyCanvas(width, height)
    canvas = createCanvas(width, height)

    canvas = modifyPixel(canvas, 3, 3, "o")
    # # print(canvas)
    printCanvas(canvas)
    # writeCanvas2File(canvas, "output.txt")
