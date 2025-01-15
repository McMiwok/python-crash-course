Number = int | float | complex


# Write the body of the function to make the script
# work without errors
def sqr(n: Number) -> Number:
    return n * n


if __name__ == "__main__":
    # Do not change the below asserts
    assert sqr(2) == 4
    assert sqr(4.0) == 16
    assert sqr(3 + 2j) == 5 + 12j
