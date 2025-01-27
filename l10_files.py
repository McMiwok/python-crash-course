from pathlib import Path


BASE_PATH = Path(__file__).parent


if __name__ == "__main__":
    # Get file path
    # print(__file__)

    # Join path. Old way
    filepath = BASE_PATH.joinpath(".data/h.txt")
    print(filepath)

    # Join path. New way
    filepath = BASE_PATH / ".data/h.txt"
    print(filepath)

    # Open files
    f = open(filepath, mode="r")  # File Handle
    print(f.read())
    f.close()

    print(filepath.read_text())
    writepath = BASE_PATH / ".data/w.txt"

    f = open(writepath, mode="a")
    f.write("my third file write (append)")
    f.close()

    writepath.write_text("my text")

    # Context Manager
    # <implicit code before context manager body>
    # <run your body>
    # <implicit code when leaving context manager body>
    with open(filepath) as f:
        print(f"Inside context manager: {f.read()}")

    # i = random()  # uniform random float from (0, 1)
    # if i < 0.5:
    #     impl = "feuwhfw"
    # print(impl)
    print(f"f is closed: {f.closed}")

    # TODO: research json package
