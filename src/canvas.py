from utils.data import (
    areHorz,
    areVert,
    drawHorizontalLine,
    drawVerticalLine,
    fill_adjacent_list,
    get_surroundings,
    pointNotInCanvas,
    printCanvas,
    printEmptyCanvas,
)


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
        canvas[i][j + 1] = character
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
        return canvas
    elif areHorz(point1, point2):
        print("drawing horizontal line")
        x = x1
        canvas = drawHorizontalLine(canvas, x, y1, y2)
        return canvas
    else:
        print("drawing diagonal line not supported")
        return canvas


def drawRectangle(canvas, x1, y1, x2, y2):
    # point1 = [x1, y1]
    # point2 = [x2, y2]
    if pointNotInCanvas(canvas, x1, y1) or pointNotInCanvas(canvas, x2, y2):
        print("error")
        return canvas
    else:
        canvas = drawHorizontalLine(canvas, x1, y1, y2)
        canvas = drawVerticalLine(canvas, x1, x2, y2)
        return canvas


def fillArea(canvas, x, y, colour):
    adjacent_indexes = get_surroundings(x, y, canvas)
    fill_adjacent_list(adjacent_indexes, canvas, colour)
    explored = []
    while len(adjacent_indexes) > 0:
        adj = adjacent_indexes.pop()
        explored.append(adj)
        xx, yy = adj
        adjacent_indexes += get_surroundings(xx, yy, canvas)
        adjacent_indexes = [x for x in adjacent_indexes if x not in explored]
        adjacent_indexes = list(set(adjacent_indexes))
        fill_adjacent_list(adjacent_indexes, canvas, colour)

    return canvas


if __name__ == "__main__":
    width = 3
    height = 4
    printEmptyCanvas(width, height)
    canvas = createCanvas(width, height)

    # # canvas = modifyPixel(canvas, 0, 0, "o")
    # # canvas = modifyPixel(canvas, 1, 0, "p")
    # # canvas = modifyPixel(canvas, 1, 1, "t")
    # canvas = modifyPixel(canvas, 1, 2, "z")
    # # # print(canvas)
    # printCanvas(canvas)
    # # writeCanvas2File(canvas, "output.txt")
    # # canvas = drawLine(canvas, 0, 0, 1, 1)
    # # printCanvas(canvas)
    # # canvas, err = drawLine(canvas, 0, 0, 0, 3)
    # # printCanvas(canvas)
    # # canvas = drawLine(canvas, 2, 0, 2, 0)
    # # printCanvas(canvas)
    # # print(canvas[0:2][0])
    # # canvas = drawRectangle(canvas, 0, 0, 2, 0)
    # # printCanvas(canvas)

    fillArea(canvas, 0, 0, "p")
    print(canvas)
    printCanvas(canvas)
