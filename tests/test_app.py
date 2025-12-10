import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app import add, subtract  # noqa: E402


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 0) == 0
