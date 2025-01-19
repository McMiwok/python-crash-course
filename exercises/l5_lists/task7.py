def proxy_pop(l: list[int]) -> int:
    return l.pop()


# Do not change the below's code
if __name__ == "__main__":
    l = [3, 6, 1, 2]

    assert proxy_pop(l) == 2
    assert proxy_pop(l) == 1
    assert proxy_pop(l) == 6
    assert proxy_pop(l) == 3
