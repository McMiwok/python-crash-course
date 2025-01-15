
# Finish the function `is_even` to fix the script the
# way it works without errors
def is_even(n: int) -> bool:
    return n % 2 == 0


# Do not change the below's code
if __name__ == "__main__":
    assert is_even(2) is True
    assert is_even(1) is False
    assert is_even(3) is False
    assert is_even(4) is True
