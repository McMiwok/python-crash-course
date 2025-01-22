# Write a function that returns True if
# the first character of the string `s`
# equals the last character of the string `s`;
# return False otherwise
def same_chars(s: str) -> bool:
    if not s:
        return True
    return s[0] == s[-1]


# Do not change the below's code
if __name__ == "__main__":
    assert same_chars("abba") is True
    assert same_chars("Abba") is False
    assert same_chars("baba") is False
    assert same_chars("cabac") is True
