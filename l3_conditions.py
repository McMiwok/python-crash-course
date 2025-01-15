def is_true() -> bool:
    """Magically returns True or False"""


def generate_number(start: int, end: int) -> int:
    """Magically returns a number from [start; end] interval"""


if __name__ == "__main__":
    # if-statement
    # if <expression>:
    #     <body of if>
    # else:
    #     <body of else>
    if is_true():
        print("I'm inside `if`")
    else:
        print("I'm inside `else`")

    if generate_number() == 0:
        print("This is 0")
    elif generate_number() == 1:  # optional
        print("This is 1")
    elif generate_number() == 2:  # optional
        print("This is 2")
    else:  # optional
        print("This is anything else")

    # Comparison Operators
    i = 5

    a = 10 == 10
    a = 10 != 10
    a = 10 > 10  # <, <=, >=

    # Two equivalent forms
    b = 0 <= i <= 10
    b = i >= 0 and i <= 10

    b = i > 2 and i != 0
    b = i > 4 or i != 2
    b = not (i > 4)

    # Thuthy and Falsy
    # 1. Expression is True or False
    # 2. <expression> is not None
    # 3. if simple type: <expression> != 0
    # 4. len(<expression>) != 0

    s = ""
    if s:
        print("tada")
    else:
        print("NOT tada")

    # Real example
    stack = [2, 3, 4]
    while stack:  # desugaring into `while len(stack) != 0`
        pass

    # is check that left-hand operand is EXACT object that is in right-hand operand
    # obj1 is obj2. If true these are two same object that point to the same memory location

    i = 10  # 256
    j = 10

    # Python pre-allocation memory on small values and
    # assign a reference to the variable when creating
    i = True
    i = 10
    i = None
    i = ()

    # in works with all collections:
    #  - str
    #  - list
    #  - dict
    #  - set
    if 3 in stack:
        print("tada")

    s = "abcd"
    if "bc" in s:
        print("tada")

    # Use isinstance to check the type of the variable
    # DO NOT use type to check the type of the variable
    if isinstance(s, str):
        pass

    # Python3.10 was shipped with pattern matching
    s = "c"
    match s + "g":
        case "a":
            print("a")
        case "b" | "c" | "d":
            print("b,c,d")
        case _:
            print(f"anything {s}")
