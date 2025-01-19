from typing import Any


# Write the body of the function that returns
# the last element from the list `l`
def last(l: list[Any]) -> Any:
    return l[-1]


# Do not change the below's code
if __name__ == "__main__":
    assert last([1, 5, 4]) == 4
    assert last(["a", "b", "c"]) == "c"
    assert last([True, False]) == False
