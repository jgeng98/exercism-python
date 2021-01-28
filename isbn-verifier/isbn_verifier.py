import regex 

def is_valid(isbn):
    # verify that if a check digit exists, it must be in the correct spot
    if 'X' in isbn and not isbn.endswith('X'):
        return False
    
    # substitute everything that isn't a digit or a 'X' with nothing
    isbn = regex.sub(r'[^0-9X]', '', isbn)

    # if the resulting string length isn't 10, immediately return false
    if len(isbn) != 10:
        return False

    index = 0
    sum = 0 

    for digit in isbn:
        # replace check digit with 10 in the sum
        if digit == 'X':
            index += 10
            sum += index
            continue
        index += int(digit)
        sum += index
    
    if sum % 11 == 0:
        return True
    else:
        return False
