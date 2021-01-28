def response(hey_bob):
    # yelling a question at him
    if hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    # yelling a statement at him
    elif hey_bob.isupper() and not hey_bob.endswith('?'): 
        return "Whoa, chill out!"
    # address him without saying anything
    # ie. empty string or only whitespace characters 
    elif hey_bob.isspace() or not hey_bob:
        return "Fine. Be that way!"
    # ask him a question (trimming off whitespace)
    elif hey_bob.strip().endswith('?'):
        return "Sure."
    # any other case 
    else:
        return "Whatever."
