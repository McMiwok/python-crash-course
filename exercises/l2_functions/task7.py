# Declare the function named `greet` and write its body
# the way that it fixes all errors in the script

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Do not change the below's code
if __name__ == "__main__":
    assert greet("Jon") == "Hello, Jon!"
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Baba") == "Hello, Baba!"
