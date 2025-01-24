# Write the body of the function to make the script
# work without errors.
#
# HINT: Use `set`
def unique(l: list[int]) -> list[int]:
    return list(set(l))


if __name__ == "__main__":
    res = unique([1, 1, 1, 2, 2, 2, 3])

    assert len(res) == 3
    assert list(sorted(res)) == [1, 2, 3]

    res = unique([1, 1, 1, 1])
    assert len(res) == 1
    assert res == [1]

    res = unique([])
    assert len(res) == 0
