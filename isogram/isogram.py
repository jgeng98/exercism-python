def is_isogram(string):
    for i in string:
        if i.isspace() or i == '-':
            continue
        if string.lower().count(i) > 1:
            return False
    return True


