import string
from collections import Counter

def count_words(sentence):
    punc_without_apostrophe = string.punctuation.replace("\'","")

    # deletes all non-apostrophe punctuation
    sentence = sentence.translate(str.maketrans(punc_without_apostrophe,' '*len(punc_without_apostrophe)))
    
    # count words in split sentence, trimming off the apostrophe characters from the start and end if they exist 
    counts = Counter([word.strip("'") for word in sentence.lower().split()])

    return counts
