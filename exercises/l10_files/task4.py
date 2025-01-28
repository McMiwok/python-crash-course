from pathlib import Path

L10_PATH = Path(__file__).parent

# Write the function. It should read the content of a file
# under path and return the content as a string
def read(path: Path) -> str:
    with open(path, 'r') as f:
        return f.read()


# Do not modify the code below
if __name__ == "__main__":
    text = "Hello World!"
    path = L10_PATH / "example.txt"
    path.write_text(text)

    assert read(path) == text

    path.unlink(missing_ok=True)
