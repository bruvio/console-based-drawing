import pytest
from canvas import createCanvas, modifyPixel, writeCanvas2File


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
def test_modifyPixel(x, y, point):
    can = createCanvas(x, y)
    can = modifyPixel(can, point[0], point[1], "f")
    assert can[point[0]][point[1]] == "f"


@pytest.mark.parametrize("x", [3, 4, 5])
@pytest.mark.parametrize("y", [4, 5, 20])
@pytest.mark.parametrize("point", [[-1, 1], [10, 2], [3, 3]])
@pytest.mark.xfail(reason="some wrong input parameters for canvas")
def test_modifyPixel(x, y, point):
    can = createCanvas(x, y)
    can = modifyPixel(can, point[0], point[1], "f")
    assert can[point[0]][point[1]] == "f"


# pytest.mark.usefixtures("canvas")


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
