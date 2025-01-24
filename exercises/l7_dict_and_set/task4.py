# Write a body of the function to make it
# return a max value of dictionary `d`
def max_value(d: dict[str, int]) -> int:
    return max(d.values())


# Do not change the below's code
if __name__ == "__main__":
    assert max_value({"a": 3, "b": 5}) == 5
    assert max_value({"a": 10}) == 10
    assert max_value({"a": -1, "b": -1, "default": 1}) == 1
