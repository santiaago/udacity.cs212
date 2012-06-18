# -----------------
# User Instructions
# 
# Write a function, readwordlist, that takes a filename as input and returns
# a set of all the words and a set of all the prefixes in that file, in 
# uppercase. For testing, you can assume that you have access to a file 
# called 'words4k.txt'

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename) # opens file
    text = file.read().split()    # gets file into string
    
    wordset = set()
    prefixset = set()
    
    for word in text:   # loop through all words and add them to the set
        wordset.add(word)
        for prefix in prefixes(word):   # loop through all prefixes of each word and add them to the set
            prefixset.add(prefix)
    
    return wordset, prefixset
    
WORDS, PREFIXES = readwordlist('words4k.txt')

def test():
    assert len(WORDS)    == 3892
    assert len(PREFIXES) == 6475
    assert 'UMIAQS' in WORDS
    assert 'MOVING' in WORDS
    assert 'UNDERSTANDIN' in PREFIXES
    assert 'ZOMB' in PREFIXES
    return 'tests pass'

print test()