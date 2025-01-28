from random import randint


def peekaboo(l: list[str]) -> str:
    i = randint(0, 30)
    try:
        return f"peek {l[i]}"
    except IndexError:
        return "boo"


if __name__ == "__main__":
    l = ["a", "b", "c", "ubu", "baba", "daba", "ububu"]
    for i in range(15):
        print(peekaboo(l))
