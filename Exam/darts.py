# Unit 5: Probability in the game of Darts

"""
In the game of darts, players throw darts at a board to score points.
The circular board has a 'bulls-eye' in the center and 20 slices
called sections, numbered 1 to 20, radiating out from the bulls-eye.
The board is also divided into concentric rings.  The bulls-eye has
two rings: an outer 'single' ring and an inner 'double' ring.  Each
section is divided into 4 rings: starting at the center we have a
thick single ring, a thin triple ring, another thick single ring, and
a thin double ring.  A ring/section combination is called a 'target';
they have names like 'S20', 'D20' and 'T20' for single, double, and
triple 20, respectively; these score 20, 40, and 60 points. The
bulls-eyes are named 'SB' and 'DB', worth 25 and 50 points
respectively. Illustration (png image): http://goo.gl/i7XJ9

There are several variants of darts play; in the game called '501',
each player throws three darts per turn, adding up points until they
total exactly 501. However, the final dart must be in a double ring.

Your first task is to write the function double_out(total), which will
output a list of 1 to 3 darts that add up to total, with the
restriction that the final dart is a double. See test_darts() for
examples. Return None if there is no list that achieves the total.

Often there are several ways to achieve a total.  You must return a
shortest possible list, but you have your choice of which one. For
example, for total=100, you can choose ['T20', 'D20'] or ['DB', 'DB']
but you cannot choose ['T20', 'D10', 'D10'].
"""

def test_darts():
    "Test the double_out function."
    assert double_out(170) == ['T20', 'T20', 'DB']
    assert double_out(171) == None
    assert double_out(100) in (['T20', 'D20'], ['DB', 'DB'])

"""
My strategy: I decided to choose the result that has the highest valued
target(s) first, e.g. always take T20 on the first dart if we can achieve
a solution that way.  If not, try T19 first, and so on. At first I thought
I would need three passes: first try to solve with one dart, then with two,
then with three.  But I realized that if we include 0 as a possible dart
value, and always try the 0 first, then we get the effect of having three
passes, but we only have to code one pass.  So I creted ordered_points as
a list of all possible scores that a single dart can achieve, with 0 first,
and then descending: [0, 60, 57, ..., 1].  I iterate dart1 and dart2 over
that; then dart3 must be whatever is left over to add up to total.  If
dart3 is a valid element of points, then we have a solution.  But the
solution, is a list of numbers, like [0, 60, 40]; we need to transform that
into a list of target names, like ['T20', 'D20'], we do that by defining name(d)
to get the name of a target that scores d.  When there are several choices,
we must choose a double for the last dart, but for the others I prefer the
easiest targets first: 'S' is easiest, then 'T', then 'D'.
"""
ordered_points = sorted(set(range(0,21) + range(22,42,2) + range(21,63,3) + [25,50]))


def double_out(total):
    """Return a shortest possible list of targets that add to total,
    where the length <= 3 and the final element is a double.
    If there is no solution, return None."""
    # your code here
    #ordered_points = sorted(set(range(0,21) + range(22,42,2) + range(21,63,3)))
    #print ordered_points
    for dart1 in ordered_points:
        for dart2 in ordered_points:
            dart3 = total - (dart1 + dart2)
            if (dart3%2)==0 and dart3 in ordered_points and name_lastdart(dart3) != None:
                sol = [name(dart1),name(dart2),name_lastdart(dart3)]
                if dart1 == 0 and dart2 == 0:
                    return [sol[-1]]
                elif dart1 == 0:
                    return sol[1:]
                else:
                    return sol
    #print 'None'
    return None

def name(dart):
    if dart <= 20:
        return 'S'+str(dart)
    elif dart == 50:
        return 'DB'
    elif dart == 25:
        return 'SB'
    elif dart <=40:
        if (dart%2)==0:
            return 'D'+str(dart/2)
        else:
            return 'T'+str(dart/3)
    elif dart <=60:
        return 'T'+str(dart/3)
    #print 'name Warning - dart: %s'%(dart)

def name_lastdart(dart):
    'last dart is already: dart%2 == 0'
    if 0 < dart <= 20:
        return 'D'+str(dart/2)
    elif dart == 50:
        return 'DB'
    elif 20 < dart <= 40:
        return 'D'+str(dart/2)
    #print 'name_lastdart Warning - dart: %s'%(dart)
    return None

"""
It is easy enough to say "170 points? Easy! Just hit T20, T20, DB."
But, at least for me, it is much harder to actually execute the plan
and hit each target.  In this second half of the question, we
investigate what happens if the dart-thrower is not 100% accurate.

We will use a wrong (but still useful) model of inaccuracy. A player
has a single number from 0 to 1 that characterizes his/her miss rate.
If miss=0.0, that means the player hits the target every time.
But if miss is, say, 0.1, then the player misses the section s/he
is aiming at 10% of the time, and also (independently) misses the thin
double or triple ring 10% of the time. Where do the misses go?
Here's the model:

First, for ring accuracy.  If you aim for the triple ring, all the
misses go to a single ring (some to the inner one, some to the outer
one, but the model doesn't distinguish between these). If you aim for
the double ring (at the edge of the board), half the misses (e.g. 0.05
if miss=0.1) go to the single ring, and half off the board. (We will
agree to call the off-the-board 'target' by the name 'OFF'.) If you
aim for a thick single ring, it is about 5 times thicker than the thin
rings, so your miss ratio is reduced to 1/5th, and of these, half go to
the double ring and half to the triple.  So with miss=0.1, 0.01 will go
to each of the double and triple ring.  Finally, for the bulls-eyes. If
you aim for the single bull, 1/4 of your misses go to the double bull and
3/4 to the single ring.  If you aim for the double bull, it is tiny, so
your miss rate is tripled; of that, 2/3 goes to the single ring and 1/3
to the single bull ring.

Now, for section accuracy.  Half your miss rate goes one section clockwise
and half one section counter-clockwise from your target. The clockwise 
order of sections is:

    20 1 18 4 13 6 10 15 2 17 3 19 7 16 8 11 14 9 12 5

If you aim for the bull (single or double) and miss on rings, then the
section you end up on is equally possible among all 20 sections.  But
independent of that you can also miss on sections; again such a miss
is equally likely to go to any section and should be recorded as being
in the single ring.

You will need to build a model for these probabilities, and define the
function outcome(target, miss), which takes a target (like 'T20') and
a miss ration (like 0.1) and returns a dict of {target: probability}
pairs indicating the possible outcomes.  You will also define
best_target(miss) which, for a given miss ratio, returns the target 
with the highest expected score.

If you are very ambitious, you can try to find the optimal strategy for
accuracy-limited darts: given a state defined by your total score
needed and the number of darts remaining in your 3-dart turn, return
the target that minimizes the expected number of total 3-dart turns
(not the number of darts) required to reach the total.  This is harder
than Pig for several reasons: there are many outcomes, so the search space 
is large; also, it is always possible to miss a double, and thus there is
no guarantee that the game will end in a finite number of moves.
"""


def outcome(target, miss):
    "Return a probability distribution of [(target, probability)] pairs."
    #your code here
    dicto = {}
    if isTriple(target):
        #p1 <=> ring accuracy ok section accuracy ko or ok
        #p2 <=> ring accuracy ko section accuracy ko or ok
        
        p1 = 1 - miss
        p2 = miss

        # keep ring accuracy calculate section accuracy (clockwise and counterclockwise)        
        p11 = p1 * miss * 0.5
        p12 = p1 * miss * 0.5
        p10 = p1 - (p11 + p12)

        key_Tcw = 'T' + str(cwTarget(target))
        key_Tccw = 'T' + str(ccwTarget(target))
        ket_T = target
        
        dicto[ket_T] = p10
        dicto[key_Tcw] = p11
        dicto[key_Tccw] = p12

        # keep ring accuracy ko calculate section accuracy (clockwise and counterclockwise)
        p21 = p2 * miss * 0.5
        p22 = p2 * miss * 0.5
        p20 = p2 - (p21 + p22)

        key_Scw = 'S' + str(cwTarget(target))
        key_Sccw = 'S' + str(ccwTarget(target))
        key_S = 'S' + target[1:]

        dicto[key_S] = p20
        dicto[key_Scw] = p21
        dicto[key_Sccw] = p22

    elif isDouble(target):
        hit = 1 - miss
        # hit ring accuracy hit or miss section
        pD = hit * hit
        pDcw = hit * miss * 0.5
        pDccw = hit * miss * 0.5
        # miss ring acc hit or miss section
        pOFF = miss * 0.5
        pS = miss * 0.5 * hit
        pScw = miss * 0.5 * miss * 0.5
        pSccw = miss * 0.5 * miss * 0.5
        #keys
        key_Dcw = 'D' +str(cwTarget(target))
        key_Dccw = 'D' +str(ccwTarget(target))
        key_D = target
        key_Scw = 'S' +str(cwTarget(target))
        key_Sccw = 'S' +str(ccwTarget(target))
        key_S = 'S' + target[1:]
        
        dicto[key_D] = pD
        dicto[key_Dcw] = pDcw
        dicto[key_Dccw] = pDccw
        
        dicto['OFF'] = pOFF
        
        dicto[key_S] = pS
        dicto[key_Scw] = pScw
        dicto[key_Sccw] = pSccw

    elif isSingle(target):
        miss = miss/5.
        hit = 1 - miss
        # hit ring accuracy
        pS = hit * hit
        pScw = hit * miss * 0.5
        pSccw = hit * miss * 0.5
        # miss ring accuracy .5 to double .5 to triple
        pD = miss * 0.5 * hit
        pDcw = miss * 0.5 * miss * 0.5
        pDccw = miss * 0.5 * miss * 0.5
        
        pT = miss * 0.5 * hit
        pTcw = miss * 0.5 * miss * 0.5
        pTccw = miss * 0.5 * miss * 0.5
        #keys
        key_S = target
        key_Scw = 'S' + str(cwTarget(target))
        key_Sccw = 'S' + str(ccwTarget(target))
        
        key_D = 'D' + target[1:]
        key_Dcw = 'D' + str(cwTarget(target))
        key_Dcc = 'D' + str(ccwTarget(target))

        key_T = 'T' + target[1:]
        key_Tcw = 'T' + str(cwTarget(target))
        key_Tccw = 'T' + str(ccwTarget(target))
        
        dicto[key_S] = pS
        dicto[key_Scw] = pScw
        dicto[key_Sccw] = pSccw

        dicto[key_D] = pD
        dicto[key_Dcw] = pDcw
        dicto[key_Dccw] = pDccw

        dicto[key_T] = pT
        dicto[key_Tcw] = pTcw
        dicto[key_Tccw] = pTccw
        
    elif isSingleBull(target):
        hit = 1 - miss
        # hit ring accuracy
        pSB = hit * hit
        pS01 = hit * miss
        # miss ring accuracy
        #1/4 goes to DB 3/4 goes to S
        pDB = miss * 0.25 * hit
        pS02 = miss * 0.25 * miss

        pS03 = miss * 0.75 * hit
        pS04 = miss * 0.75 * miss
        
        pS = pS01 + pS02 + pS03 + pS04
        
        pS_unit = pS/20.
        for d in dart_board:
            dicto['S'+str(d)] = pS_unit
        dicto['SB'] = pSB
        dicto['DB'] = pDB
        
    elif isDoubleBull(target):
        hit = 1 - miss
        #3 times less hits
        hit = hit / 3.
        miss = 1 - hit
        # hit ring accuracy
        pDB = hit * hit
        pS01 = hit * miss
        # miss ring accuracy
        # 1/3 goes to SB or S; 2/3 goes to S or S
        pS02 = miss * (2/3.) * hit
        pS03 = miss * (2/3.) * miss

        pSB = miss * (1/3.) * hit
        pS04 = miss * (1/3.) * miss
        
        pS = pS01 + pS02 + pS03 + pS04
        pS_unit = pS/20.
        for d in dart_board:
            dicto['S'+str(d)] = pS_unit
        dicto['DB'] = pDB
        dicto['SB'] = pSB

    else:
        print 'Error'

    return dicto

dart_board =  [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
def cwTarget(target):
    'next ClockWise target'
    index = int(target[1:])
    cw = 0
    for i in range(len(dart_board)):
        if dart_board[i] == index:
            if i + 1 >= len(dart_board):
                cw  = dart_board[0]
                break
            else:
                cw = dart_board[i+1]
                break
    return cw
def ccwTarget(target):
    'next CounterClockWise target'
    index = int(target[1:])
    ccw = 0
    for i in range(len(dart_board)):
        if dart_board[i] == index:
            ccw = dart_board[i-1]
            break
    return ccw
def isTriple(target):
    return target[0] == 'T'
def isDouble(target):
    return target != 'DB' and target[0] == 'D'
def isSingle(target):
    return target[0] == 'S' and not isSingleBull(target)
def isDoubleBull(target):
    return target == 'DB'
def isSingleBull(target):
    return target == 'SB'

def best_target(miss):
    "Return the target that maximizes the expected score."
    #your code here
    
def same_outcome(dict1, dict2):
    "Two states are the same if all corresponding sets of locs are the same."
    return all(abs(dict1.get(key, 0) - dict2.get(key, 0)) <= 0.0001
               for key in set(dict1) | set(dict2))

def test_darts2():
    assert best_target(0.0) == 'T20'
    assert best_target(0.1) == 'T20'
    assert best_target(0.4) == 'T19'
    assert same_outcome(outcome('T20', 0.0), {'T20': 1.0})
    assert same_outcome(outcome('T20', 0.1), 
                        {'T20': 0.81, 'S1': 0.005, 'T5': 0.045, 
                         'S5': 0.005, 'T1': 0.045, 'S20': 0.09})
    assert (same_outcome(
            outcome('SB', 0.2),
            {'S9': 0.016, 'S8': 0.016, 'S3': 0.016, 'S2': 0.016, 'S1': 0.016,
             'DB': 0.04, 'S6': 0.016, 'S5': 0.016, 'S4': 0.016, 'S20': 0.016,
             'S19': 0.016, 'S18': 0.016, 'S13': 0.016, 'S12': 0.016, 'S11': 0.016,
             'S10': 0.016, 'S17': 0.016, 'S16': 0.016, 'S15': 0.016, 'S14': 0.016,
             'S7': 0.016, 'SB': 0.64}))

def test_identifiers():
    assert isTriple('T20')
    assert not isDouble('T20')
    assert isDouble('D15')
    assert isSingle('S3')
    assert not isSingle('T2')
    assert isSingleBull('SB')
    assert not isSingleBull('DB')
    assert isDoubleBull('DB')
    assert not isDoubleBull('D20')
    print 'all identifier tests passed!'

def test_clock():
    assert cwTarget('T20') == 1
    assert ccwTarget('T20') == 5
    assert cwTarget('D16') == 8
    assert ccwTarget('D16') == 7
    assert cwTarget('S5') == 20
    assert ccwTarget('S5') == 12
    print 'all clock tests passed!'

def test_outcomes():
    assert same_outcome(outcome('D20',0.1),
                        {'D20': 0.81, 'S1': 0.0025, 'D5': 0.045, 
                         'S5': 0.0025, 'D1': 0.045, 'S20': 0.045, 'OFF': 0.05})
    assert (same_outcome(outcome('DB',0.2),
                        {'S9': 0.0432, 'S8': 0.0432, 'S3': 0.0432, 'S2': 0.0432, 'S1': 0.0432,
                         'DB': 0.0711, 'S6': 0.0432, 'S5': 0.0432, 'S4': 0.0432, 'S20': 0.0432,
                         'S19': 0.0432, 'S18': 0.0432, 'S13': 0.0432, 'S12': 0.0432, 'S11': 0.0432,
                         'S10': 0.0432, 'S17': 0.0432, 'S16': 0.0432, 'S15': 0.0432, 'S14': 0.0432,
                         'S7': 0.0432, 'SB': 0.0651}))
    print 'all tests passed!'
                        
                       
                        
