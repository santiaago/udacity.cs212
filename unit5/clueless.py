# -----------------
# User Instructions
# 
# Write a strategy function, clueless, that ignores the state and
# chooses at random from the possible moves (it should either 
# return 'roll' or 'hold'). Take a look at the random library for 
# helpful functions.

import random as r

possible_moves = ['roll', 'hold']

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    # your code here
    if (r.random() > 0.5):
        return possible_moves[1]
    else:
        return possible_moves[0]
    #return r.choice(possible_moves)

print clueless(1)
print clueless(1)
print clueless(1)
print clueless(1)
print clueless(1)
print clueless(1)
print clueless(1)
print clueless(1)
print clueless(1)