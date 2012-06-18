# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    # your code here  
    dicc = {}
    if 'light' in here:
        for a in here:
            if a is not 'light':
                for b in here:
                    if b is not 'light':
                        # create (here, there, time)
                        leftside =  (   here - frozenset([a,b,'light']),
                                        there |frozenset([a,b,'light']),
                                        t+max(a,b)
                                    )
                        # create action
                        rightside = (a,b,'->')
                        dicc[leftside] = rightside
    else:
        for a in there:
             if a is not 'light':
                for b in there:
                    if b is not 'light':
                        # create (here, there, time)
                        leftside =  (   here | frozenset([a,b,'light']),
                                        there -frozenset([a,b,'light']),
                                        t+max(a,b)
                                    )
                        # create action
                        rightside = (a,b,'<-')
                        dicc[leftside] = rightside
    return dicc

def test():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}
    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()