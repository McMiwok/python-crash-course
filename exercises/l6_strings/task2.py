# Write a function that returns a substring of `s`
# which contains `max(len(s), n)` first characters.
#
# If n <= 0, return an empty string.
#
# For example,
# take("abcd", 3) -> "abc"
def take(s: str, n: int) -> str:
    if n <= 0:
        return ""
    return s[:min(len(s), n)]


# Do not change the below's code
if __name__ == "__main__":
    assert take("abcde", 2) == "ab"
    assert take("bbhj", 3) == "bbh"
    assert take("bjk", 0) == ""
    assert take("bjk", -1) == ""
    assert take("bjk", 100) == "bjk"
