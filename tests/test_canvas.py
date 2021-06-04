import pytest
from canvas import createCanvas, modifyPixel


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
