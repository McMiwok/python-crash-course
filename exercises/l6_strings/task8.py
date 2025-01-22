# Write a function that formats a string
# a specific way that passes tests
def you_are(s: str) -> str:
    return f"You are {s}"


# Do not change the below's code
if __name__ == "__main__":
    assert you_are("Jon") == "You are Jon"
    assert you_are("Sansa") == "You are Sansa"
    assert you_are("Cersei") == "You are Cersei"
