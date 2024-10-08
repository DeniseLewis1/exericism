def find_anagrams(word, candidates):
    anagrams = []
    
    word = word.lower()

    for candidate in candidates:
        if word != candidate.lower() and sorted(word) == sorted(candidate.lower()):
            anagrams.append(candidate)

    return anagrams
