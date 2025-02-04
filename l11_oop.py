from collections import Counter
from dataclasses import dataclass
from typing import Self


# These only three classes needed for DSA
class Node:

    def __init__(self, val: int):
        self.val = val
        self.next: Self | None = None


class TreeNode:

    def __init__(self, val: int):
        self.val = val
        self.left: Self | None = None
        self.right: Self | None = None


class Trie:

    def __init__(self, val: str):
        self.val = val
        self.children = []


class Zoo:

    def __init__(self, zoo_name: str):
        print("in zoo")
        self.zoo = zoo_name


class Animal:  # Superclass (or parent class)

    def __init__(self, name: str, age: int = 10):
        # Variable attached to self is called attribute of class
        self.name = name
        self.age = age
        self.self_stack: list[int] = []

    def to_human_age(self) -> int:
        return int(self.age * 3.4)

    def set_age(self, age: int):
        self.age = age

    def get_age(self) -> int:
        return self.age

    def __str__(self):
        return f"{self.name}, {self.age}"


class Giraffe(Animal):
    # Class-level attributes
    type_ = "GIRAFFE"
    stack = []

    def __call__(self):
        return f"{self} has been called"

    def __add__(self, obj: Self) -> str:
        return Giraffe(self.name, self.age + obj.age)

    def __repr__(self):
        return f"Giraffe({self})"


class Elephant(Animal, Zoo):

    def __init__(self, name, age=10):
        super().__init__(name, age)

    def __repr__(self):
        return f"Giraffe({self})"

    def get_age(self) -> int:
        age = super().get_age()
        return age


class Math:

    @staticmethod
    def pow(a1: int, n: int) -> int:
        return a1**n


class Person:
    """_summary_

    Args:
        name (str): _description_
        surname (str): _description_
    """

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    @property
    def fullname(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"{self.name} {self.surname}"


@dataclass
class PersonData:
    name: str
    surname: str
    age: int = 20


def animal_age_to_cosmic(animal: Animal) -> int:
    """Converts animal age to cosmic age to be used in Mars

    Args:
        animal (Animal): animal instance

    Returns:
        int: cosmic age
    """
    return animal.get_age() * animal.to_human_age() ** 0.3


if __name__ == "__main__":
    # OOP Principles
    # 1. Encapsulation
    # 2. Inheritance
    # 3. Polymorphism
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

    e1 = Elephant("Sansa Stark", 18)
    e1.to_human_age()
    print(animal_age_to_cosmic(g1))
    print(animal_age_to_cosmic(e1))

    print(Math().pow(2, 3))

    p = Person("Jon", "Snow")
    print(p.fullname)

    pd = PersonData("Jon", "Snow")
    print(pd)
