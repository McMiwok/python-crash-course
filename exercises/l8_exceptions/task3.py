from typing import Any


# Handle exception in the function body the way that this script works without errors
def getter(d: dict[str, Any], key: str) -> Any:
    try:
        return d[key]
    except KeyError:
        return None


# Do not modify the code below
if __name__ == "__main__":
    d = {"a": 42}

    assert getter(d, "a") == 42
    assert getter(d, "senseoflife") is None
