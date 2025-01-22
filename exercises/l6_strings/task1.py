# Write a function that returns True if
# string `s` contains character `char`
# and False otherwise
def contains_char(s: str, char: str) -> bool:
    return char in s


# Do not change the below's code
if __name__ == "__main__":
    assert contains_char("abcv", "v") is True
    assert contains_char("abcv", "g") is False
    assert contains_char("abccc", "c") is True
