import math
from pprint import pprint

# Import alias
import exercises.l2_functions.task6 as task
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
import l2_functions
from l2_functions import factorial


if __name__ == "__main__":
    d = {
        "one": "two",
        "three": [v for v in range(20)]
    }
    print(math.factorial(4))
    print(factorial(4))
    print(__name__)
