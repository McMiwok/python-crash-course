from typing import Any


# Write a function that joins all elements
# from list `l` with a separator `, `.
# It is guaranteed that all elements from list `l`
# can be converted to string
def proxy_join(l: list[Any]) -> str:
    if not l:
        return ""
    return ", ".join(map(str, l))


# Do not change the below's code
if __name__ == "__main__":
    assert proxy_join([1, 4, 3]) == "1, 4, 3"
    assert proxy_join(["Jon", "Arya", "Rob"]) == "Jon, Arya, Rob"
    assert proxy_join([]) == ""
