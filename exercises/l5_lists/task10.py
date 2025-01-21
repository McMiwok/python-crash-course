from typing import Any


# Write the function that reverses the list `l`
# NOTE: the function must create a new list.
# Do not modify list `l`.
def reverse(l: list[Any]) -> list[Any]:
    return l[::-1]


# Do not change the below's code
if __name__ == "__main__":
    l = [3, 4, 5]

    assert reverse(l) == [5, 4, 3]
    assert l == [3, 4, 5]

    assert reverse(["c", "b", "a"]) == ["a", "b", "c"]
