from collections import Counter

# Write a body of the function that counts
# a character occurrences in a string and
# returns a dictionary where key is a character
# and value is the amount of this character in a string `s`
#
# For example,
# 1. "aabc" -> {"a": 2, "b": 1, "c": 1}
# 2. "" -> {}
def count_chars(s: str) -> dict[str, int]:
    return dict(Counter(s))


# Do not change the below's code
if __name__ == "__main__":
    assert count_chars("aabc") == {"a": 2, "b": 1, "c": 1}
    assert count_chars("abc") == {"a": 1, "b": 1, "c": 1}
    assert count_chars("") == {}
