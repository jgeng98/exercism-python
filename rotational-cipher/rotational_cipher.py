def rotate(text, key):
    rotated = [convert(char, key) for char in list(text)]
    return ''.join(rotated)


def convert(character, key):
    if character.islower():
        return chr((ord(character) - 97 + key) % 26 + 97)
    elif character.isupper(): 
        return chr((ord(character) - 65 + key) % 26 + 65)
    else:
        return character


