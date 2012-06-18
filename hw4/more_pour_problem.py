# -----------------
# User Instructions
# 
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes 
# as input capacities, goal, and (optionally) start. This function should 
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the 
# volume of a glass. 
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i), 
# ('empty', i), ('pour', i, j) where i and j are indices indicating the 
# glass number. 


from itertools import *
def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""
    # your code here
    def successors(state):
        dicc = {}
        for i in range(len(state)):
            # fill
            t = list(state)
            t[i] = capacities[i]
            dicc[tuple(t)] = ('fill',i)
            # empty
            t = list(state)
            t[i] = 0 
            dicc[tuple(t)] = ('empty',i)
            #pour
            for j in range(len(state)):
                t = list(state)
                if state[j]+ state[i] <=capacities[j]:
                    t[j] = state[j]+ state[i]
                    t[i] = 0
                else:
                    t[j] = state[j] + (capacities[j]-state[j])
                    t[i] = state[i] - (capacities[j]-state[j])
                dicc[tuple(t)] = ('pour',i,j)
        # pour
        #for i, j in permutations(range(len(state)),2):
        #    t = list(state)
        #    if state[j]+ state[i] <=capacities[j]:
        #        t[j] = state[j]+ state[i]
        #        t[i] = 0
        #    else:
        #        t[j] = state[j] + (capacities[j]-state[j])
        #        t[i] = state[i] - (capacities[j]-state[j])
        #    dicc[tuple(t)] = ('pour',i,j)
        return dicc
    def is_goal(s):
        if goal in s:
            return True
        return False
    if start is None:
        start = (0,)*len(capacities)
    return shortest_path_search(start, successors,is_goal)

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [ [start] ] 
    while frontier:
        path = frontier.pop(0)
        if v: print 'path:'+str(path)
        if v: print 'path[-1]:'+str(path[-1])
        
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []
    
def test_more_pour():
    #print more_pour_problem((1, 2, 4, 8), 4) == [
    #    (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    #print more_pour_problem((1, 2, 4), 3) == [
    #        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)]
    #print more_pour_problem((1, 2, 4), 3)
    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
    return 'test_more_pour passes'

print test_more_pour()