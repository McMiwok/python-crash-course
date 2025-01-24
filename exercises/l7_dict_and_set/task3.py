if __name__ == "__main__":
    # Do not modify the line below
    a, b = {"a", "b", "c", "d"}, {"a", "b", "n", "m"}

    # Use sets `a` and `b` to modify a value of `c` to make the script
    # work without errors.
    # `c` should contain a union of `a` and `b`
    c = a.union(b)

    # Do not modify the line below
    assert c == {"a", "b", "c", "d", "n", "m"}
