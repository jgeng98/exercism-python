import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)

    sentence = set(sentence.lower())

    if sentence >= alphabet:
        return True
    else:
        return False
