import secrets
import string


class Cipher:

    letters = string.ascii_lowercase

    def __init__(self, key=None):
        self.key = (
            key
            if key is not None
            else "".join(secrets.choice(string.ascii_lowercase) for i in range(100))
        )

    def convert_to(self, character, key):
        return Cipher.letters[
            (Cipher.letters.find(character) + Cipher.letters.find(key)) % 26
        ]

    def convert_from(self, character, key):
        return Cipher.letters[
            (Cipher.letters.find(character) - Cipher.letters.find(key)) % 26
        ]

    def encode(self, text):
        coded = []
        if len(self.key) < len(text):
            self.key = self.key * (100 // len(self.key))

        for i in range(len(text)):
            coded.append(self.convert_to(text[i], self.key[i]))

        return "".join(coded)

    def decode(self, text):
        decoded = []
        if len(self.key) < len(text):
            self.key = self.key * (100 // len(self.key))

        for i in range(len(text)):
            decoded.append(self.convert_from(text[i], self.key[i]))

        return "".join(decoded)
