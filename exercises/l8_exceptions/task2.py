from random import randint


def peekaboo(l: list[str]) -> str:
    i = randint(0, 30)

    # Use try...except block to handle the exception.
    # If success return the below's line of code, otherwise `return "boo"`
    return f"peek {l[i]}"


if __name__ == "__main__":
    l = ["a", "b", "c", "ubu", "baba", "daba", "ububu"]
    for i in range(15):
        print(peekaboo(l))
