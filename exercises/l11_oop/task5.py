
# Modify the class IntMath to make the script work without errors.
#
# HINT: research static methods
class IntMath:

    def pow(v: int, p: int) -> int:
        return v**p


# Do not change the code below
if __name__ == "__main__":
    assert IntMath.pow(2, 2) == 4
    assert IntMath().pow(2, 2) == 4