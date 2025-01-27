if __name__ == "__main__":
    l = [1, 2, 0, 3]

    s = 0
    for i, v in enumerate(l):
        # Use try...except block to handle the error.
        # If error happens add nothing to `s`, just continue the loop
        s = i / v
