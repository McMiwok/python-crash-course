# Write two functions that calculate the factorial of `n`
#
# - `factorial_while` must use while loop;
# - `factorial_for` must use for loop.
def factorial_while(n: int) -> int:
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f


def factorial_for(n: int) -> int:
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


# Do not change the below's code
if __name__ == "__main__":
    assert factorial_while(2) == 2
    assert factorial_while(3) == 6
    assert factorial_while(4) == 24
    assert factorial_while(5) == 120
    assert factorial_while(6) == 720

    assert factorial_for(2) == 2
    assert factorial_for(3) == 6
    assert factorial_for(4) == 24
    assert factorial_for(5) == 120
    assert factorial_for(6) == 720
