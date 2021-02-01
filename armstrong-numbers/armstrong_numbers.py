import numpy as np

def is_armstrong_number(number):
    num = np.array(list(str(number))).astype(int)

    if sum(num**len(num)) == int(number):
        return True
    else:
        return False
