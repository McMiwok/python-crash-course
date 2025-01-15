if __name__ == "__main__":
    # Two types of loops:
    # old-flick while
    # youngster for

    # While Loops
    # while <expression> (truthy or falsy):
    #    <body of the loop>
    i = 0
    while i < 10:
        # print(i)
        i += 1

    # Python doesn't have do...while loops.
    # But we can add a hack to implement similar behavior
    while True:
        i -= 10
        if i < 0:
            break
        else:  # TODO: why we can do without else
            print("after conditions")

    # Control Flow
    # Python has: break and continue
    i = 0
    while i < 10:
        if i == 5:
            break  # like return but for loops
        # print(i)
        i += 1

    i = 0
    while i < 10:
        if i == 5:
            i += 1
            continue
        # print(i)
        i += 1

    # For loop
    # for..in or for..each
    # for loop uses Iterators implicitly
    stack = [3, 4, 5, 1, 2]
    for v in stack:
        print(v)

    # Design Patterns (OOP)
    # Iterator
    #
    # stack: list = [3, 4, 5, 1, 2]
    # Iterable vs Iterator
    # list, str, dict, set is Iterable
    #
    # Iterator
    # When we pass `stack` to for..in loop. Python does next:
    #
    # iterator = {
    #   ref *stack,
    #   i: int
    # }
    #
    # On every iteration of for loop, Python calls
    # next(iterator) -> iterator { ref *stack, i += 1 }
    _it = iter(stack)
    while True:
        try:
            v = next(_it)
        except StopIteration:
            break
        print(v)

    for c in "aabbcdf":
        print(c)

    # Useful for functions
    # 1. range
    for i in range(10):
        pass

    # 2. enumerate
    stack = [2, 5, 4, 6, 4, 3, 2]
    for i, v in enumerate(stack):
        print(v)

    # 3. zip
    s1 = "dfrty"
    s2 = "kjuyt"
    s3 = "bvgfh"
    for v1, v2, v3 in zip(s1, s2, s3):
        print(v1, v2, v3)
