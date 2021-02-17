import string
import numpy as np
import math


def cipher_text(plain_text):
    plain_text = plain_text.translate(
        plain_text.maketrans(
            string.ascii_uppercase,
            string.ascii_lowercase,
            string.punctuation + string.whitespace,
        )
    )

    if 0 < math.modf(np.sqrt(len(plain_text)))[0] < 0.5:
        r = round(np.sqrt(len(plain_text)))
        c = r + 1
    else:
        r = c = round(np.sqrt(len(plain_text)))

    spaces = np.array([" "] * c)

    plain_text = np.array(list(plain_text.ljust(r * c))).reshape(r, c)

    plain_text = np.vstack((plain_text, spaces)).transpose().flatten()

    plain_text = "".join(plain_text)[:-1]

    return plain_text
