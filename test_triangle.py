from triangle import triangle 
def test_invalid1():
    assert triangle(-1, 0, 1) == -1

def test_equilateral():
    assert triangle(3, 3, 3) == 1

def test_invalid2():
    assert triangle(1, 1, 2) == 1
