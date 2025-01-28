from pathlib import Path

L10_PATH = Path(__file__).parent


# Use Path class and L10_PATH constant to finish the function.
# Function should return True if `p` is file and False otherwise
def is_file(p: Path):
    return p.is_file()


# Do not modify the code below
if __name__ == "__main__":
    path = L10_PATH / "example.txt"
    path.touch()

    assert is_file(path) is True
    assert is_file(L10_PATH) is False

    path.unlink(missing_ok=True)
