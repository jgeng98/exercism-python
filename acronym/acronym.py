import string 

def abbreviate(words):
    # delete apostrophe characters and replace all other punctuation with white space characters
    words = words.translate(str.maketrans(string.punctuation,' '*len(string.punctuation), '\''))
    
    # split the sentence into words
    words = words.split()
    abb = ""

    # concatenate the first letter of every word to the abbreviation
    for word in words:
        abb += word[0].upper()

    return abb
