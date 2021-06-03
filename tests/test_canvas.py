import pytest
from canvas import createCanvas


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
