from dataclasses import dataclass
from pprint import pprint


@dataclass
class Meta:
    name: str
    type: str


if __name__ == "__main__":
    # TBY0938374652 - 0
    # TBY0938374612 - 1
    # TBY0938274612 - 2
    # ...
    # TBY0921274612 - {"name": "Super book", "type": "book"}
    # K - 1,000,000
    # U - 1,000,000,000,000,000
    # NO TO ARRAY l = []
    d = {
        "TBY0938374652": Meta("Linux", "book"),
        "TBY0938374612": Meta("Secret stuff", "secret"),
        "TBY0921274612": Meta("Embarrassing stuff", "embarrassing"),
        "TBY0938374612": Meta("Secret stuff", "secret"),
    }
    # Keys are unique
    # Dict is mutable
    # Dictionary; Hash Map, Hash Table
    # hash function
    d["NEW"] = Meta("New", "new")
    # d["NEW"] = Meta("REPLACED", "REPLACED")

    # Delete from dict
    # del d["NEW"]
    # pprint(d)

    # Dict uses Linked List to preserve input ordering

    # Loops
    # 1. Loop over keys of dict
    print("\n1. Loop over keys")
    for k in d:
        print(k)

    # 2. Loop over keys of dict
    print("\n1. Loop over keys")
    for k in d.keys():
        print(k)

    # 3. Loop over values of dict
    print("\n1. Loop over values")
    for v in d.values():
        print(v)

    # 4. Loop over keys and value of dict
    print("\n1. Loop over items")
    for k, v in d.items():
        print(k, v)

    if "TBY0921274612" in d:
        print("\nTHEY KEY IS PRESENT IN DICTIONARY")

    # Hash Set
    # set
    s = {"a", "b", "c", "m"}
    print(s, type(s))
    s = set()
