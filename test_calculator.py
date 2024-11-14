from calculator import add

def test_add():
    assert add(2, 3) == 5, "2와 3을 더하면 5가 나와야 합니다"
    assert add(-1, 1) == 0, "-1과 1을 더하면 0이 나와야 합니다"
    assert add(-1, -1) == -2, "-1과 -1을 더하면 -2가 나와야 합니다"
