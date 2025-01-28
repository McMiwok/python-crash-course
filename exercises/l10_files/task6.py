from pathlib import Path

L10_PATH = Path(__file__).parent


# Finish the function. It should write the `content`
# into the file located in `path`
def write(path: Path, content: str):
    with open(path, 'w') as file:
        file.write(content)


# Do not modify the code below
if __name__ == "__main__":
    text = "Hello World!"
    path = L10_PATH / "example.txt"

    assert path.exists() is False
    write(path, text)
    assert path.exists() is True
    assert path.read_text() == text

    path.unlink(missing_ok=True)
