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


def pointNotInCanvas(canvas, i, j):

    width = len(canvas[0]) - 2
    height = len(canvas)
    if (j < 0 or j > width) or (i < 0 or i > height - 1):
        return True
    return False


def get_surroundings(i, j, matrix):
    """given a matrix and a couple of indices finds indexes of points
    adjacent to given input

    Args:
        i ([int]): [index of row]
        j ([int]): [index of column]
        matrix ([list ]): [canvas]

    Returns:
        [list]: [list of adjacent indexes]
    """
    m = len(matrix[0]) - 2
    n = len(matrix)
    # neighbors = lambda x, y: [
    #     (x2, y2)
    #     for x2 in range(x - 1, x + 2)
    #     for y2 in range(y - 1, y + 2)
    #     if (
    #         -1 < x <= m
    #         and -1 < y <= n
    #         and (x != x2 or y != y2)
    #         and (0 <= x2 <= m)
    #         and (0 <= y2 <= n)
    #     )
    # ]

    # return neighbors(m, n)
    # return [
    #     (x2, y2)
    #     for x2 in range(max(0, x - 1), min(width, x + 2))
    #     for y2 in range(max(0, y - 1), min(height, y + 2))
    #     if (x2, y2) != (x, y)
    # ]

    adjacent_indexes = []
    if i > m or j > n or i < 0 or j < 0:
        return adjacent_indexes
    if i > 0:
        adjacent_indexes.append((i - 1, j))

    if i + 1 < m:
        adjacent_indexes.append((i + 1, j))

    if j > 0:
        adjacent_indexes.append((i, j - 1))

    if j + 1 < n:
        adjacent_indexes.append((i, j + 1))

    if i - 1 > 0 and j - 1 > 0:
        adjacent_indexes.append((i - 1, j - 1))
    if i - 1 > 0 and j + 1 < n:
        adjacent_indexes.append((i - 1, j + 1))
    if i + 1 < m and j - 1 > 0:
        adjacent_indexes.append((i + 1, j - 1))
    if i + 1 < m and j + 1 < n:
        adjacent_indexes.append((i + 1, j + 1))

    return adjacent_indexes


def get_adjacents(i, j, matrix):
    """given a matrix and a couple of indices finds indexes of points
    adjacent to given input

    Args:
        i ([int]): [index of row]
        j ([int]): [index of column]
        matrix ([list ]): [canvas]

    Returns:
        [list]: [list of adjacent indexes]
    """
    m = len(matrix[0]) - 2
    n = len(matrix)
    adjacent_indexes = []
    if i > m or j > n or i < 0 or j < 0:
        return adjacent_indexes
    if i > 0:
        adjacent_indexes.append((i - 1, j))

    if i + 1 < m:
        adjacent_indexes.append((i + 1, j))

    if j > 0:
        adjacent_indexes.append((i, j - 1))

    if j + 1 < n:
        adjacent_indexes.append((i, j + 1))
    return adjacent_indexes


def areHorz(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        return True
    return False


def areVert(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if y1 == y2:
        return True
    return False


def drawHorizontalLine(canvas, x, y1, y2):

    if y1 > y2:
        y1, y2 = y2, y1
    for y in range(y1, y2 + 1):
        canvas[x][y + 1] = "x"
    return canvas


def drawVerticalLine(canvas, x1, x2, y):

    if x1 > x2:
        x1, x2 = x2, x1
    for x in range(x1, x2 + 1):
        canvas[x][y + 1] = "x"
    return canvas


def fill_adjacent_list(get_surroundings, matrix, colour):
    """given the list of adjacent indeces fills values for those indexes
    for the given input matrix with string colour

    Args:
        get_surroundings ([list]): [list of adjacent indexes to use]
        matrix ([list ]): [canvas]
        colour ([str]): [character to be used for filling]

    Returns:
        [list]: [list of coordinates]
    """

    if get_surroundings:
        for o in range(0, len(get_surroundings)):
            matrix[get_surroundings[o][0]][get_surroundings[o][1] + 1] = colour
