
# Modify this function to make the script work without errors.
def multiply(a: int, b: int = 0) -> int:
    return a * b


# Do not change the below's code
if __name__ == "__main__":
    assert multiply(2, 2) == 4
    assert multiply(2) == 0