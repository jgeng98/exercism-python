import string, regex

def count_words(sentence):
    counts = dict()
    words = regex.split(r'[_ ,\n\t]+', sentence.lower())
    
    
    for word in words:
        word = word.strip(string.punctuation)
        if word in counts:
            counts[word] += 1 
        else:
            counts[word] = 1
    
    if '' in counts.keys():
        return {k: v for k, v in counts.items() if k is not ''}
    else:
        return counts
