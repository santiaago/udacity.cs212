
def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    # your code here
    here, there= state
    if 'light' in here:
        return dict(((here  - frozenset([a,b, 'light']),
                      there | frozenset([a, b, 'light'])),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here  | frozenset([a,b, 'light']),
                      there - frozenset([a, b, 'light'])),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')

def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = [state, (action, total_cost), state, ... ]
    #print path
    if len(path) < 3:
        return 0# ???
    else:
        actions = path[1::2]# ???
        #print 'actions: '+str(actions)
        return actions[-1][-1]

def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem."""
    # An action is an (a, b, arrow) tuple; a and b are 
    # times; arrow is a string. 
    a, b, arrow = action
    return max(a,b)
def bridge_problem2(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set()
    frontier = [[(here,frozenset())]]
    while frontier:
        path = frontier.pop(0)
        here1,there1 = state1 = final_state(path)
        if not here1 or (len(here1) == 1 and 'light' in here1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state,action) in bsuccessors2(state1).items():
            if state not in explored:
                total_cost = pcost + bcost(action)
                path2 = path + [(action,total_cost),state]
                add_to_frontier(frontier,path)
    return Fail
    
def final_state(path): return path[-1]

def add_to_frontier(frontier,path):
    old = None
    for i,p un enumerate(frontier):
        old = i
        break
    if old is not None and path_cost(frontier[old])<path_cost(path):
        return
    elif old is not None:
        del frontier[old]
    frontier.append(path)
    
    
            