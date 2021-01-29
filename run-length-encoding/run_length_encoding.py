from itertools import groupby

def decode(string):
    num = 0
    decoded = ""
    
    for letter in string:
        if letter.isdigit():
            num = 10*num + int(letter)
        else:
            if num == 0:
                decoded += letter
            else:
                decoded += num*letter
                num = 0
        
    return decoded



def encode(string):
    counts = [[k, len(list(g))] for k, g in groupby(string)]
    coded = ""

    for pair in counts:
        if pair[1] == 1:
            coded += pair[0]
        else:
            coded += str(pair[1]) + pair[0]

    return coded
