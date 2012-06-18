# -----------------
# User Instructions
# 
# In this problem, you will complete the code for the hold_at(x) 
# function. This function returns a strategy function (note that 
# hold_at is NOT the strategy function itself). The returned 
# strategy should hold if and only if pending >= x or if the 
# player has reached the goal.

def hold_at(x):
    """Return a strategy that holds if and only if 
    pending >= x or player reaches goal."""
    def strategy(state):
        # your code here
        (p,me,you,pending) = state
        if me + pending >=goal:
            return 'hold'
        if pending >= x:
            return 'hold'
        return 'roll'
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy

goal = 50
def test():
    assert hold_at(30)((1, 29, 15, 20)) == 'roll'
    assert hold_at(30)((1, 29, 15, 21)) == 'hold'
    assert hold_at(15)((0, 2, 30, 10))  == 'roll'
    assert hold_at(15)((0, 2, 30, 15))  == 'hold'
    return 'tests pass'

print test()
