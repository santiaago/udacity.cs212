# -----------------
# User Instructions
# 
# Write the two action functions, hold and roll. Each should take a
# state as input, apply the appropriate action, and return a new
# state. 
#
# States are represented as a tuple of (p, me, you, pending) where
# p:       an int, 0 or 1, indicating which player's turn it is.
# me:      an int, the player-to-move's current score
# you:     an int, the other player's current score.
# pending: an int, the number of points accumulated on current turn, not yet scored
p = 0
me = 1
you = 2
pending = 3
def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    # your code here
    newstate = list(state)
    newstate[p] = 0 if newstate[p] == 1 else 1
    temp = newstate[you]
    newstate[you] = newstate[me] + newstate[pending]
    newstate[me] = temp
    newstate[pending] = 0
    return tuple(newstate)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    # your code here
    newstate = list(state)
    if d == 1 :
        newstate[p] = 0 if newstate[p] == 1 else 1
        temp = newstate[you]
        newstate[you] = newstate[me] +1
        newstate[me] = temp
        newstate[pending] = 0
    else:
        newstate[pending] = newstate[pending]+ d
    return tuple(newstate)
    
def test():    
    assert hold((1, 10, 20, 7))    == (0, 20, 17, 0)
    assert hold((0, 5, 15, 10))    == (1, 15, 15, 0)
    assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
    assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
    return 'tests pass'

print test()