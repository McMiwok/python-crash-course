from pathlib import Path

L10_PATH = Path(__file__)


# Use Path class and L10_PATH constant to finish the function.
# Function should return True if passed path exists and False otherwise
#
# HINT. Search for joinpath method or / operator (in context of Path)
def path_exists(path: str) -> bool:
    return L10_PATH.joinpath(path).exists()


if __name__ == "__main__":
    assert path_exists(".") is True
    assert path_exists("../__init__.py") is True
    assert path_exists("../task1.py") is True
    assert path_exists("../wrong.txt") is False
    assert path_exists("/wrong/path") is False
