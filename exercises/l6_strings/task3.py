# Use a solution from the previous task and
# modify the function `take`.
#
# Now, it accepts additional `last` parameter. If it's
# False, the function works as in task2. If it's True
# the function should take `max(len(s), take)` characters
# from end of the string.
#
# For example,
# take("abcd", 2, True) -> "cd"
def take(s: str, n: int, last: bool = False) -> str:
    if n <= 0:
        return ""
    if last:
        return s[max(0, len(s) - min(len(s), n)):]
    else:
        return s[:min(len(s), n)]


# Do not change the below's code
if __name__ == "__main__":
    assert take("abcde", 2) == "ab"
    assert take("bbhj", 3) == "bbh"
    assert take("bjk", 0) == ""
    assert take("bjk", -1) == ""

    assert take("abcd", 2, True) == "cd"
    assert take("agfd", 4, True) == "agfd"
    assert take("df", 10, True) == "df"
    assert take("fff", -1, True) == ""
