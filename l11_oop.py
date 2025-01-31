from collections import Counter
from typing import Self


class Giraffe:
    # Class-level attributes
    type_ = "GIRAFFE"
    stack = []

    # self is reference to the concrete class instance to be used inside of class
    def __init__(self, name: str, age: int = 10):
        # Variable attached to self is called attribute of class
        self.name = name
        self.age = age
        self.self_stack: list[int] = []

    def to_human_age(self) -> int:
        return int(self.age * 3.4)

    def set_age(self, age: int):
        self.age = age

    def __repr__(self):
        return f"Giraffe({self})"

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __call__(self):
        return f"{self} has been called"

    def __add__(self, obj: Self) -> str:
        return Giraffe(self.name, self.age + obj.age)


if __name__ == "__main__":
    # OOP Principles
    # 1. Incapsulation
    s = "Hello World!"  # Complex inner implementation. Simple outer abstraction

    s = "aaabccd"
    c = Counter(s)
    print(c)

    g1 = Giraffe("Jon Snow")
    g2 = Giraffe("Cercei Lannister", 42)

    # print(g1.name, g2.name)
    print(g1)
    s = str(g2)

    g1.to_human_age()
    g2.to_human_age()

    g1.set_age(43)
    print(g1.age)

    Giraffe.set_age(g1, 30)
    print(g1.age)

    print(g1())

    g3 = g1 + g2
    print(g3)
