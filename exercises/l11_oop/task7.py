# Modify the class Point to make the script work without errors.
#
# HINT: research magic methods
class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# Do not change the code below
if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(2, 3)

    p3 = p1 + p2
    assert p3.x == 3
    assert p3.y == 4
