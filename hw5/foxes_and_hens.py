# -----------------
# User Instructions
# 
# This problem deals with the one-player game foxes_and_hens. This 
# game is played with a deck of cards in which each card is labelled
# as a hen 'H', or a fox 'F'. 
# 
# A player will flip over a random card. If that card is a hen, it is
# added to the yard. If it is a fox, all of the hens currently in the
# yard are removed.
#
# Before drawing a card, the player has the choice of two actions, 
# 'gather' or 'wait'. If the player gathers, she collects all the hens
# in the yard and adds them to her score. The drawn card is discarded.
# If the player waits, she sees the next card. 
#
# Your job is to define two functions. The first is do(action, state), 
# where action is either 'gather' or 'wait' and state is a tuple of 
# (score, yard, cards). This function should return a new state with 
# one less card and the yard and score properly updated.
#
# The second function you define, strategy(state), should return an 
# action based on the state. This strategy should average at least 
# 1.5 more points than the take5 strategy.

import random
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
            # some element of args refuses to be a dict key
            return f(args)
    _f.cache = cache
    return _f
def foxes_and_hens(strategy, foxes=7, hens=45):
    """Play the game of foxes and hens."""
    # A state is a tuple of (score-so-far, number-of-hens-in-yard, deck-of-cards)
    state = (score, yard, cards) = (0, 0, 'F'*foxes + 'H'*hens)
    while cards:
        action = strategy(state)
        state = (score, yard, cards) = do(action, state)
    return score + yard

def do(action, state, cardtodo=None):
    (score, yard, cards) = state
    if cardtodo != None:
        curcard = cardtodo
    else:
        curcard = random.choice(cards)
    newcards = cards.replace(curcard,'',1)

    if action == 'wait':
        return (score,yard+1,newcards) if curcard == 'H' else (score,0,newcards)
    elif action == 'gather':
        return (score+yard,0,newcards)
    
def take5(state):
    "A strategy that waits until there are 5 hens in yard, then gathers."
    (score, yard, cards) = state
    if yard < 5:
        return 'wait'
    else:
        return 'gather'

def average_score(strategy, N=1000):
    return sum(foxes_and_hens(strategy) for _ in range(N)) / float(N)

def superior(A, B=take5):
    "Does strategy A have a higher average score than B, by more than 1.5 point?"
    return average_score(A) - average_score(B) > 1.5
def pactions(state):
    return ['wait', 'gather']

def strategy(state):
    (score, yard, cards) = state
    # your code here
    return bestaction(state, pactions, Q,U2)

def Q(state, action, U):
    (score,yard,cards) = state
    foxcount = cards.count("F")
    hencount = cards.count("H")
    numcards = len(cards)

    res = None
    if foxcount == 0:
        res = float(U(do(action, state, 'H')))
    elif hencount == 0:
        res = float(U(do(action, state, 'F')))
    else:
        res =  float(foxcount*(U(do(action, state, 'F')))
                     + hencount*(U(do(action, state, 'H'))))/numcards
    if res == None:
        raise ValueError    
    return res
@memo
def U2(state):
    """The utility of a state"""
    (score,yard,cards) = state
    if len(cards) == 0:
        return score+yard
    else:
        return max(Q(state, action, U2)
                   for action in pactions(state))

def bestaction(state, actions, Q, U):
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)

def test():
    gather = do('gather', (4, 5, 'F'*4 + 'H'*10))
    assert (gather == (9, 0, 'F'*3 + 'H'*10) or 
            gather == (9, 0, 'F'*4 + 'H'*9))
    
    wait = do('wait', (10, 3, 'FFHH'))
    assert (wait == (10, 4, 'FFH') or
            wait == (10, 0, 'FHH'))
    
    assert superior(strategy)
    return 'tests pass'

print test()   


