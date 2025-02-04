# Modify the class Person to make the script work without errors.
#
# HINT: use property
class Person:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


# Do not change the code below
if __name__ == "__main__":
    p = Person("Jon", "Doe")

    assert p.full_name == "Jon Doe"
    assert isinstance(Person.full_name, property)
    assert "full_name" not in p.__dict__
