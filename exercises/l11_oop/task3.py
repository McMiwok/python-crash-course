# Add required methods to the class Vehicle
class Vehicle:
    def is_truck(self):
        return True


if __name__ == "__main__":
    # Assign the needed value to the variable `c`
    # to make the script work without errors
    c = Vehicle()

    assert isinstance(c, Vehicle)
    assert c.is_truck() is True
