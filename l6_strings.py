if __name__ == "__main__":
    # UTF-8. Dynamic-size characters
    s = "Hello world!"
    h = "h"  # 1 byte
    # a - 00000001
    # b - 00000010
    # c - 00000011
    # ...
    # We can encode 256 characters with 1 byte
    d = "Д"  # 2 bytes
    u = "ü"  # 2 bytes
    print(len(d.encode("utf-8")))

    # String under the hood
    # Roughly speaking string is an array of bytes that are stored on the heap
    # l = [b"h", b"e", b"l", ...]
    # Strings in Python are immutable

    # How to create a string
    # 1. Use ""
    s = "I don't care"

    # 2. Use ''
    s = "I don't care"  # escape character

    # 3. """ """. This is multiline string
    s = """I

    care

    too

    much
    """

    # Python supports str indexing and slicing like in any other collection
    slice1 = s[:3]
    char1 = s[1]

    # Concatenation
    a = "hello"
    b = "world"

    c = a + " " + b

    # For loop supports strings out of the box
    for c in s:
        print(c)

    # Important string methods

    # 1. Split
    s = "Hello an amazing super world"
    l = s.split()

    # 2. Join
    l = ["Jon", "Arya", "Rob", "Tirion", "Cercei"]

    # "Jon, Arya, Rob, Tirion, Cercei"
    names = ", ".join(l)

    # Str functions
    l = len(s)  # Returns an amount of character
    o = ord("a")

    # Legacy old formatting of strings
    formatted = "value %s" % s
    print(formatted)

    # Method .format
    s = "Jon"
    s2 = "Snow"
    formatted = "Name: {1} {0}".format(s, s2)

    # f-string
    formatted = f"Name: {s} {s2}. Age: {10 + 2 + 5}"
    print(formatted)
