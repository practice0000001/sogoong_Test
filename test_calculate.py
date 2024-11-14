from calculate import add, subtract

import pytest

def test_add():
    assert add(1, 2) == 3, "1과 2를 더하면 3이 나와야 합니다."
    assert add(-1, 1) == 0, "-1과 1을 더하면 0이 나와야 합니다."
