from collections import Counter

def find_anagrams(word, candidates):
    word_count = Counter(word.lower())
    anagrams = []

    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue 
        if Counter(candidate.lower()) == word_count:
            anagrams.append(candidate)
    
    return anagrams
