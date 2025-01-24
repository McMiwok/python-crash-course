# Declare and write the body of the function named `my_len`.
# This function should accept an Iterable as a parameter
# and return its length

def my_len(i) -> int:
    return len(i)


# Do not change the below's code
if __name__ == "__main__":
    assert my_len([3, 4, 5]) == 3
    assert my_len("abv") == 3
    assert my_len({"a": 1, "b": 3}) == 2
    assert my_len((3, 4, 5)) == 3
