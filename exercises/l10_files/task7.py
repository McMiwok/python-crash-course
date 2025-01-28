from pathlib import Path

L10_PATH = Path(__file__).parent


# Finish the function. It should calculate and return the amount
# of line from a file located under `path`
def count_lines(path: Path) -> int:
    with open(path, 'r') as file:
        return len(file.readlines())


# Do not modify the code below
if __name__ == "__main__":
    text = "line\nline\nline\nline"
    path = L10_PATH / "example.txt"

    path.write_text(text)
    assert count_lines(path) == 4
    path.unlink(missing_ok=True)
