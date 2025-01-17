# Use `while` loop to calculate the number
# of digits in a number `n`
def count_digits(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


# Do not change the below's code
if __name__ == "__main__":
    assert count_digits(0) == 1
    assert count_digits(134) == 3
    assert count_digits(54) == 2
    assert count_digits(55678) == 5
