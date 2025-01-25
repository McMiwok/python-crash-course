def getter(l: list[int], i: int) -> int:
    return l[i] / i


def query(s: str):
    print(f"QUERY DB: {s}")


def close_connection():
    print("Closing connection")


if __name__ == "__main__":
    # Exceptions
    l = [1, 3, 0, 2, 1]
    # print(getter(l, 0))

    for i in range(15):
        try:
            print(getter(l, i))
        except ZeroDivisionError as e:
            print(f"Zero division error {e}. Continue loop")
        except IndexError as e:
            print(f"Index error {e}. Breaking loop")
            break

    # Exceptions are handled in try...except block
    #
    # try:
    #   <potentially erroneous code>
    # except (Exception)+ [as error]:
    #   <handle error here>
    # [
    # except (Exception)+ [as error]:
    #   <handle error here>
    # ]
    # [
    # finally:
    #   <code to execute despite whether the error happened or not>
    # ]
    # or
    # [
    # else:
    #   <???>   
    # ]
    #

    try:
        query("SELECT * FROM db")
    except Exception:
        print("Error when querying DB")
    finally:
        close_connection()

    print("IMPORTANT CODE AFTER ERROR")
