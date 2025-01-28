if __name__ == "__main__":
    l = [1, 2, 0, 3]

    s = 0
    for i, v in enumerate(l):
        try:
            s += i / v
        except ZeroDivisionError:
            continue
    print(s)
