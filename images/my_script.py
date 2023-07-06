import numpy as np

def log_function(number, word='hello', word_2='world'):
    z = np.log(number)
    print(word, word_2)
    print(f"The log of {number} is {z}.")
    return z