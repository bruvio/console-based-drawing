import pytest
from canvas import createCanvas, modifyPixel, writeCanvas2File, drawRectangle, fillArea

from utils.data import (
    areVert,
    areHorz,
    pointNotInCanvas,
    drawHorizontalLine,
    drawVerticalLine,
    printCanvas,
    get_surroundings,
)


@pytest.mark.parametrize("x", [3, 4, 1])
@pytest.mark.parametrize("y", [4, 5, 20])
def test_createCanvas(x, y):
    can = createCanvas(x, y)
    width = len(can[0]) - 2
    height = len(can)
    assert (width == x) and (height == y)


@pytest.mark.parametrize("x", [-3, -4, 0])
@pytest.mark.parametrize("y", [4, 0, -20])
@pytest.mark.xfail(reason="wrong input parameters for canvas")
def test_badSizeCanvas(x, y):
    can = createCanvas(x, y)
    width = len(can[0]) - 2
    height = len(can)
    assert (width == x) and (height == y)


@pytest.mark.parametrize("x", [3, 4, 5])
@pytest.mark.parametrize("y", [4, 5, 20])
@pytest.mark.parametrize("point", [[1, 1], [2, 2], [3, 3]])
def test_modifyPixel1(x, y, point):
    can = createCanvas(x, y)
    can = modifyPixel(can, point[0], point[1], "f")
    assert can[point[0]][point[1] + 1] == "f"


@pytest.mark.parametrize("x", [3, 4, 5])
@pytest.mark.parametrize("y", [4, 5, 20])
@pytest.mark.parametrize("point", [[-1, 1], [10, 2], [3, 3]])
@pytest.mark.xfail(reason="some wrong input parameters for canvas")
def test_modifyPixel2(x, y, point):
    can = createCanvas(x, y)
    can = modifyPixel(can, point[0], point[1], "f")
    assert can[point[0]][point[1] + 1] == "f"


@pytest.mark.parametrize("x", [3, 4, 5])
@pytest.mark.parametrize("y", [4, 5, 20])
def test_writeCanvas2File(x, y):
    canvas = createCanvas(x, y)
    test_file = "test-output.txt"
    test_path = "".join(test_file)
    writeCanvas2File(canvas, test_path)

    with open(test_file, "r") as testoutput:
        text = testoutput.readlines()

    for i in range(0, len(canvas)):
        lst = canvas[i]
        lst = "".join(map(str, lst)) + "\n"
        assert lst == text[i]


@pytest.mark.parametrize("point1", [[-1, 1], [10, 2], [3, 3]])
@pytest.mark.parametrize("point2", [[-1, 1], [5, 2], [3, 3]])
@pytest.mark.xfail(reason="some points are not horizontal")
def test_areHorz(point1, point2):
    assert areHorz(point1, point2) is True


@pytest.mark.parametrize("point1", [[-1, 1], [10, 1], [3, 3]])
@pytest.mark.parametrize("point2", [[-1, 1], [10, 2], [3, 4]])
@pytest.mark.xfail(reason="some points are not vertical")
def test_areVert(point1, point2):
    assert areVert(point1, point2) is True


@pytest.mark.parametrize("x", [-3, -4, 0])
@pytest.mark.parametrize("y", [4, 0, -20])
@pytest.mark.xfail(reason="some points are inside")
@pytest.mark.usefixtures("canvas")
def test_areInCanvas(canvas, x, y):
    assert pointNotInCanvas(canvas, x, y) is True


@pytest.mark.parametrize("point1", [[0, 0], [0, 1], [0, 2]])
@pytest.mark.parametrize("point2", [[0, 2], [0, 1], [0, 3]])
def test_drawHorzLine(canvas, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if areHorz(point1, point2):
        x = x1
        canvas_line = drawHorizontalLine(canvas, x, y1, y2)
        assert all([a == "x" for a in canvas_line[x][y1 + 1 : y2 + 1]])


@pytest.mark.parametrize("point1", [[0, 0], [1, 0], [2, 0]])
@pytest.mark.parametrize("point2", [[2, 0], [1, 0], [3, 0]])
def test_drawVertLine(canvas, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if areVert(point1, point2):

        y = y1
        canvas_line = drawVerticalLine(canvas, x1, x2, y)
        # transpose list of list (nested list) and get column as row
        selected_column = list(zip(*canvas_line))[y + 1]
        assert all([a == "x" for a in selected_column[x1 : x2 + 1]])


@pytest.mark.parametrize("point1", [[0, 0], [1, 0], [2, 0]])
@pytest.mark.parametrize("point2", [[1, 0], [2, 2], [3, 3]])
def test_drawRectangle(canvas, point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    canvas_rect = drawRectangle(canvas, x1, y1, x2, y2)

    selected_column = list(zip(*canvas_rect))[y2 + 1]

    if len(canvas_rect[x1][y1 + 1 : y2 + 1]) == 0:
        assert all([a == "x" for a in selected_column[x1 : x2 + 1]])
    elif len(selected_column) == 0:
        assert all([a == "x" for a in selected_column[x1 : x2 + 1]])
    else:

        assert (all([a == "x" for a in canvas_rect[x1][y1 + 1 : y2 + 1]])) and (
            all([a == "x" for a in selected_column[x1 : x2 + 1]])
        )


@pytest.mark.parametrize(
    "point, output",
    [
        ([0, 0], [(1, 0), (0, 1), (1, 1)]),
        ([0, 1], [(1, 1), (0, 0), (0, 2), (1, 0), (1, 2)]),
        ([0, 2], [(1, 2), (0, 1), (1, 1)]),
        ([1, 2], [(0, 2), (2, 2), (1, 1), (0, 1), (2, 1)]),
        ([1, 0], [(0, 0), (2, 0), (1, 1), (0, 1), (2, 1)]),
        ([2, 1], [(1, 1), (3, 1), (2, 0), (2, 2), (1, 0), (1, 2), (3, 0), (3, 2)]),
        ([1, 1], [(0, 1), (2, 1), (1, 0), (1, 2), (0, 0), (0, 2), (2, 0), (2, 2)]),
    ],
)
def test_getSurroundings(point, output):
    x1, y1 = point
    can = createCanvas(3, 4)
    adjacent_indexes = get_surroundings(x1, y1, can)
    assert adjacent_indexes == output


@pytest.mark.parametrize(
    "point, output",
    [
        (
            [0, 0],
            [
                ["|", "p", "p", "p", "|"],
                ["|", "p", "p", "p", "|"],
                ["|", "p", "p", "p", "|"],
                ["|", "p", "p", "p", "|"],
            ],
        )
    ],
)
def test_fillArea(point, output):
    x1, y1 = point
    can = createCanvas(3, 4)
    filled = fillArea(can, x1, y1, "p")
    assert filled == output
