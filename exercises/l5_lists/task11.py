from typing import Any


# Write a function that combines two lists.
# NOTE: function must create a new list.
# Do not modify lists passed as arguments
def combine(l1: list[Any], l2: list[Any]) -> list[Any]:
    return l1 + l2


# Do not change the below's code
if __name__ == "__main__":
    l1, l2 = [1, 2, 3], [4, 5, 6]

    assert combine(l1, l2) == [1, 2, 3, 4, 5, 6]
    assert l1 == [1, 2, 3]
    assert l2 == [4, 5, 6]

    assert combine([1, 2], ["a", "b"]) == [1, 2, "a", "b"]
