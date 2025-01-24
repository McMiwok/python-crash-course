from typing import Any


# Write a body of the function. It should merge to dictionaries d1 and d2.
# NOTE: the function should create a new dictionary. Do not modify dictionaries
# passed to the function as arguments
def merge(d1: dict[Any, Any], d2: dict[Any, Any]) -> dict[Any, Any]:
    new_dict = d1.copy()  # Create a copy of d1
    new_dict.update(d2)  # Update the copy with d2
    return new_dict


# Do not change the below's code
if __name__ == "__main__":
    assert merge({"a": 1, "b": 2}, {"c": 3, "d": 4}) == {"a": 1, "b": 2, "c": 3, "d": 4}

    d1, d2 = {"a": 1}, {"b": 1}
    assert merge(d1, d2) == {"a": 1, "b": 1}
    assert d1 == {"a": 1}
    assert d2 == {"b": 1}
