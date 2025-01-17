# Use `for` loop to count all occurrence of character `c`
# in a string `s`.
def count_char(s: str, c: str) -> int:
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count


# Do not change the below's code
if __name__ == "__main__":
    assert count_char("ababa", "a") == 3
    assert count_char("ababa", "b") == 2
    assert count_char("ababa", "c") == 0
    assert count_char("cccca", "a") == 1
