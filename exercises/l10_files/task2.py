from pathlib import Path

L10_PATH = Path(__file__).parent

# Use Path class and L10_PATH constant and finish the function.
# The function should create the directory with name `name`
# inside the `L10_PATH` directory
def create_directory(name: str):
    pass


# Do not modify the code below
if __name__ == "__main__":
    name = "tmp"
    path = L10_PATH / name
    assert path.exists() is False

    create_directory(name)
    assert path.exists() is True
    path.rmdir()
