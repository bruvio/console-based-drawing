import pathlib
import sys
import pytest

src_dir = pathlib.Path(__file__).parents[1].absolute() / "src"
sys.path.append(src_dir.as_posix())

from src.canvas import createCanvas


@pytest.fixture(scope="session")
def canvas():
    yield createCanvas(20, 4)
