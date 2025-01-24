from typing import Any


# Write a body of the function that returns
# True is `key` exists in dictionary `d`
# and False otherwise
def exists(d: dict[Any, Any], key: Any) -> bool:
    return key in d


# Do not change the below's code
if __name__ == "__main__":
    assert exists({"a": 1, "b": 2}, "b") is True
    assert exists({"a": 1, "b": 2}, "c") is False
