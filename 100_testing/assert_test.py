def add(a, b):
    return a + b


def test_add():
    assert add(0, 0) == 1

if __name__ == "__main__":
    test_add()