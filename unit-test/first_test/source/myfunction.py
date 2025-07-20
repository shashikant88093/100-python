def add(a,b):
    return a + b

print(add(1,2))


def test_add():
    result = add(1,2)
    assert result == 3