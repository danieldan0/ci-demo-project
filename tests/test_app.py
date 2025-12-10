import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app import add  # noqa: E402


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
