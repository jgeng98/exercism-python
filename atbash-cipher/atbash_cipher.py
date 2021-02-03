import string


def encode(plain_text):
    plain_text = plain_text.lower()

    text = plain_text.translate(
        plain_text.maketrans(
            string.ascii_lowercase,
            string.ascii_lowercase[::-1],
            string.punctuation + string.whitespace,
        )
    )

    return " ".join(text[i : i + 5] for i in range(0, len(text), 5))


def decode(ciphered_text):
    return ciphered_text.translate(
        ciphered_text.maketrans(
            string.ascii_lowercase, string.ascii_lowercase[::-1], " "
        )
    )
