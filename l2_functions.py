# Function is a code unit that can be called as an independent entity.
#
# During function declaration, we set parameters.
#
# Pay attention to type hinting
from typing import Callable


def factorial(n: int) -> int:
    """Calculate factorial of `n`"""
    res = 1
    i = 1
    while i <= n:
        res *= i
        i += 1

    return res


# Despite we annotated as int, we can use arguments of other types
def select_min(a: int, b: int, c: int) -> int:
    v = min(a, b, c)
    return v


# *args is presented as tuple inside function
def fancy_select_min(a: int, b: int, *args: tuple[int]) -> int:
    return min(a, b, *args)


def name_builder(name: str, surname: str, age: int = 18) -> str:
    return f"{name} {surname}; aged {age}"  # f-string


def fancy_name_builder(**kwargs) -> str:
    s = ""
    for k, v in kwargs.items():
        s += f"{k}: {v}"
    return s


def accept(*args, **kwargs):
    print(args, kwargs)


def combination(a: int, b: float = 0, *args, **kwargs):
    pass


# context can be either "BIG" or "SMALL"
# wall is closed variable; overall this is called closures
def builder(context: str) -> Callable[[], bool] | None:
    wall = 10

    def big() -> bool:
        print(f"big. {wall}")
        return True

    def small() -> bool:
        print(f"small {wall}")
        return False

    if context == "BIG":
        return big
    if context == "SMALL":
        return small

    # If we don't return anything from the function,
    # Python implicitly returns None
    # return None


if __name__ == "__main__":
    n = 9
    # 3!
    # 4! = 1 * 2 * 3 * 4
    # 5!
    # 6!
    # When we call function, we pass arguments
    factorial(3)

    # From combinatorics
    # n! * m!
    n = factorial(4)
    m = factorial(5)
    print(n * m)

    # Or as a single line.
    # Python saves the calculation results into Stack implicitly
    print(factorial(4) * factorial(5))

    # Use any expression as a parameter
    factorial(n**2 // 2)

    # Sequence of operations:
    # 1. Evaluate all arguments
    # 2. Call function
    # 3. Store returned value into Stack
    # 4. Use the last value from Stack as argument of print
    # 5. Call function
    print(select_min(2 + 1, 5, factorial(3)))

    print(name_builder("Jon", "Snow"))
    print(name_builder(surname="Stark", name="Sansa", age=10))

    # "Boy" is nameless then we use it as positional parameter
    # "Stark" has a name and will be assigned to the parameter with the appropriate name
    print(name_builder("Boy", age=30, surname="Stark"))

    print(fancy_select_min(2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4))

    print(
        fancy_name_builder(
            name="Sansa", surname="Stark", age=30, eye_color="Green", blabla="bubu"
        )
    )
    accept(3, 4, 5, five=6, six="seven")

    # Closures example
    f = builder("BIG")  # f is an alias to function big
    res = f()
    print(res)

    # REPL - Read-Eval-Print-Loop
    # CTRL+SHIFT+P
    # > Python: Start Native Python REPL
    #
    # Python Console tab in PyCharm
