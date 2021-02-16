import regex


def translate(text):
    pig_latin = []
    for word in text.split():
        if word.startswith(("a", "e", "i", "o", "u", "xr", "yt")):  # rule 1
            pig_latin.append(word + "ay")
            continue

        match = regex.match("(^[^aeiou]+)(y.*)", word)  # rule 4
        if match:
            pig_latin.append(match.group(2) + match.group(1) + "ay")
            continue

        match = regex.match("(^[^aeiou]*qu)(.*)", word)
        if match:  # rule 3
            pig_latin.append(match.group(2) + match.group(1) + "ay")
            continue

        match = regex.match("(^[^aeiou]+)(.*)", word)
        if match:
            pig_latin.append(match.group(2) + match.group(1) + "ay")
            continue

    return " ".join(pig_latin)
