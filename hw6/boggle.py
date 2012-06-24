# -----------------
# User Instructions
# 
# In this problem, you will define a function, boggle_words(), 
# that takes a board as input and returns a set of words that
# can be made from the board according to the rules of Boggle.
import math
from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

def boggle_words(board, minlength=3):
    "Find all the words on this Boggle board; return as a set of words."
    # your code here
    def build_words(i,N,str_candidate='',visited_i=set(),results=set()):
        """
        Find all words on this Boggle board, starting at position i
        with the current string candidate and with a list of already visited cells"""
        
        # check that we havent dealt with this index
        # in that case return curent results
        if i[0] in visited_i:
            return results
            
        # if not, add it to the visited set
        visited_in_current_scope = set()
        visited_in_current_scope = visited_i.copy()
        visited_in_current_scope.add(i[0])
        
        # if the current string is a word: 
        # add it to the result and keep on searching
        if str_candidate in WORDS and len(str_candidate)>=minlength:
            results.add(str_candidate)
            
        # get all neighbors of the current i_th
        neighbors_of_i = neighbors(i[0],N)
        
        # loop through all neighbors searching for words
        for n in neighbors_of_i:
            if board[n] != '|':
                # if it is a word and respects rules add it
                if str_candidate+board[n] in WORDS:
                    if len(str_candidate+board[n])>=minlength:
                        if n not in visited_in_current_scope:
                            results.add(str_candidate+board[n])
                # if it is in PREFIXES search for words
                if str_candidate+board[n] in PREFIXES:
                    t = (n,board[n])
                    build_words(t,N,str_candidate+board[n],visited_in_current_scope)
        return results
    # initialize
    N = int(math.sqrt(len(board)))  # N: the length of the board (suppose it is a square)
    res = set() 
    
    for i in enumerate(board):
        if i[1] != '|':
            words = build_words(i,N,i[1],set())
            for w in words:
                res.add(w)
    return res
    
def test():
    b = Board('XXXX TEST XXXX XXXX')
    assert b == '|||||||XXXX||TEST||XXXX||XXXX|||||||'
    print 'pass test 1'
    assert display(b) == """
||||||
|XXXX|
|TEST|
|XXXX|
|XXXX|
||||||""".strip()
    print 'pass test 2'
    assert boggle_words(b) == set(['SET', 'SEX', 'TEST'])
    print 'pass test 3'
    assert neighbors(20, 6) == (13, 14, 15, 19, 21, 25, 26, 27)
    print 'pass test 4'
    assert len(boggle_words(Board('TPLER ORAIS METND DASEU NOWRB'))) == 317
    print 'pass test 5'
    assert boggle_words(Board('PLAY THIS WORD GAME')) == set([
        'LID', 'SIR', 'OAR', 'LIS', 'RAG', 'SAL', 'RAM', 'RAW', 'SAY', 'RID', 
        'RIA', 'THO', 'HAY', 'MAR', 'HAS', 'AYS', 'PHI', 'OIL', 'MAW', 'THIS', 
        'LAY', 'RHO', 'PHT', 'PLAYS', 'ASIDE', 'ROM', 'RIDE', 'ROT', 'ROW', 'MAG', 
        'THIRD', 'WOT', 'MORE', 'WOG', 'WORE', 'SAID', 'MOR', 'SAIL', 'MOW', 'MOT', 
        'LAID', 'MOA', 'LAS', 'MOG', 'AGO', 'IDS', 'HAIR', 'GAME', 'REM', 'HOME', 
        'RED', 'WORD', 'WHA', 'WHO', 'WHOM', 'YID', 'DRAW', 'WAG', 'SRI', 'TOW', 
        'DRAG', 'YAH', 'WAR', 'MED', 'HIRE', 'TOWARDS', 'ORS', 'ALT', 'ORE', 'SIDE', 
        'ALP', 'ORA', 'TWA', 'ERS', 'TOR', 'TWO', 'AIS', 'AIR', 'AIL', 'ERA', 'TOM', 
        'AID', 'TOG', 'DIS', 'HIS', 'GAR', 'GAM', 'HID', 'HOG', 'PLAY', 'GOA', 'HOW', 
        'HOT', 'WARM', 'GOT', 'IRE', 'GOR', 'ARS', 'ARM', 'ARE', 'TOWARD', 'THROW'])    
    print 'pass test 6'

    return 'tests pass'

    
def Board(text):
    """Input is a string of space-separated rows of N letters each;
    result is a string of size (N+2)**2 with borders all around."""
    rows = text.split()
    N = len(rows)
    rows = [BORDER*N] + rows + [BORDER*N]
    return ''.join(BORDER + row + BORDER for row in rows)

def size(board): return int(len(board)**0.5)

def neighbors(i, N):
    return (i-N-1, i-N, i-N+1, i-1, i+1, i+N-1, i+N, i+N+1)

BORDER = '|'

def display(board):
    "Return a string representation of board, suitable for printing."
    N = size(board)
    return '\n'.join(board[i:i+N] for i in range(0, N**2, N))

# ------------
# Helpful functions
# 
# You may find the following functions useful. These functions
# are identical to those we defined in lecture. 

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

print test()

