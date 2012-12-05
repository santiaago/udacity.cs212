"""
UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating 
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

    >>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    300

The rules of bowling are as follows:

(1) A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll one, two, or three.  Your total
score is the sum of your scores for the ten frames.
(2) If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, bowling([8, 1, 7, ...]) means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
(3) If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, bowling([8, 2, 7, ...]) means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
(4) If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, bowling([10, 7, 3, ...]) means that you get a strike, you score
10 + 7 + 3 = 20 in the first frame; the second frame starts with the 7.

[[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]]
Frame 1:
hit 10 + score ball2 + score ball3
score 10(f1)
Frame 2: [f1,f1]
hit 10
score 10 + 10(f1) + 10(f2)  = 30
Frame 3 [f1,f2,f2]
hit 10
score 30 + 10(f1) + 10(f2) + 10(f3) = 60
Frame 4:[f2,f3,f3]
hit 10
score 60 + 10(f2) + 10(f3) + 10(f4) = 90
Frame 5:[f3,f4,f4]
hit 10
score 90 + 10(f3) + 10(f4) + 10(f5) = 120
Frame 6:[f4,f5,f5]
hit 10
score 120 + 10(f4) + 10(f5) + 10(f6) = 150
Frame 7:[f5,f6,f6]
hit 10
score 150 + 10(f5) + 10(f6) +10(f7) = 180
Frame 8:[f6,f7,f7]
hit 10
score 180 + 10(f6) + 10(f7) + 10(f8) = 210
Frame 9:[f7,f8,f8]
hit 10
score 210 + 10(f7) + 10(f8) + 10(f9) = 240
Frame 10:[f8,f9,f9]
hit 10
score 240 + 10(f8) + 10(f9) + 10(f10) = 270
hit 10 [f9,f10,f10]
score 270 + 10(f9) + 10(f10) = 290
hit 10 [f10]
score 290 + 10(f10)
score 300
"""
# v for Verbose
# stop to walk frame by frame
v = True
stop = False
def verbose_frame(f,frame_id,strikes_left,sparse_left):
    if v:
        print '--------------------------------------------------'
        print 'frame # '+str(frame_id)
        print f
        print 'strikes_left:'+str(strikes_left)
        print 'sparse_left:'+str(sparse_left)
        if stop: raw_input()

def bowling(balls):
    "Compute the total score for a player's game of bowling."
    ## bowling([int, ...]) -> int
    ## your code here
    frames = build_frames(balls)
    if v: print 'frames: '+str(frames)
    score = build_score(frames)
    return score

def isStrike(f):
    return len(f)==1
def isNormal(f):
    return len(f)==2
def isSparse(f):
    return isNormal(f) and sum(f)==10
def isLastFrame(f):
    return len(f)==3

def build_score(frames):
    'build the score of the game for a list of frames'
    score = 0
    has_spare = False
    has_strike = False
    strikes_left = {}
    sparse_left = {}
    frame_id= 0

    for f in frames:
        frame_id = frame_id + 1
        strikes_left[frame_id] = [ ]
        sparse_left[frame_id] = [ ]

        verbose_frame(f,frame_id,strikes_left,sparse_left)
        
        if isStrike(f):
            if v: print 'strike'
            score = score + build_score_strike(f,frame_id,strikes_left,sparse_left)
         
        elif isNormal(f):
            if v: print 'normal'
            score = score + build_score_normal(f,frame_id,strikes_left,sparse_left)
            
        if isLastFrame(f):# last frame
            if v: print 'last frame'
            score = score + build_score_lastFrame(f,frame_id,strikes_left,sparse_left)
            
        if v:
            print 'curent score:'
            print score
            print 'current strikes left: '+ str(strikes_left)
        
    if v: print score
    return score  

def build_score_strike(f,frame_id,strikes_left,sparse_left):
    'build score when frame is a strike, add bonus for future balls of player in dictionary and compute previous bonus if necesary'
    score = 10
    # handle bonus
    score = score + get_bonus(frame_id-1,strikes_left,10)
    score = score + get_bonus(frame_id-2,strikes_left,10)

    score = score + get_bonus(frame_id-1,sparse_left,10)
    
    strikes_left[frame_id].append(frame_id)
    strikes_left[frame_id].append(frame_id)
    return score

def get_bonus(frame_id,dictionary,bonus):
    'return the bonus to be added to the score if condition on dictionary is satisfied'
    score = 0
    try:
        if len(dictionary[frame_id])>0:
            dictionary[frame_id].pop()
            score = score + bonus
    except:
        None
    return score
        
def build_score_normal(f,frame_id,strikes_left,sparse_left):
    'build the score when hit to balls hence: no strike, pass frame, frame_id, and dictionaries for bonus strikes and bonus sparse'
    score = 0
    if isSparse(f):
        if v: print 'sparse'
        sparse_left[frame_id].append(frame_id)
        
    score = score + get_bonus(frame_id-1,sparse_left,f[0])
    
    score = score + get_bonus(frame_id-1,strikes_left,f[0])
    score = score + get_bonus(frame_id-1,strikes_left,f[1])
    
    score = score + get_bonus(frame_id-2,strikes_left,f[0])
    
    score = score + f[0]
    score = score + f[1]
    return score
def build_score_lastFrame(f,frame_id,strikes_left,sparse_left):
    'build the score for last frame, pass frame, frame_id, and dictionaries for bonus in strikes and sparse'
    score = 0
    first = True
    for ball in f:
        score = score + ball
        score = score + get_bonus(frame_id-1,strikes_left,ball)
        score = score + get_bonus(frame_id-2,strikes_left,ball)

        if first:
            #case for first ball and spare bonus left
            score = score + get_bonus(frame_id-1,sparse_left,ball)

        if first and ball == 10  and len(strikes_left[frame_id])==0:#strike for the last frame
            strikes_left[frame_id].append(frame_id)
            strikes_left[frame_id].append(frame_id)
            first = False
    return score
def build_frames(balls):
    ' create a list of the frames in the game, each item is a frame'
    count = 0
    memory = 0
    first_ball = True
    last_frame = False
    frames = []
    for b in balls:
        if b == 10 and count <9:
            if first_ball == False:
                frames.append([memory,b])
                memory = 0
                first_ball= True
                count = count+1
            else:
                first_ball = True
                frames.append([b])
                count = count + 1
        else:
            if count == 9:
                if not last_frame:
                    frames.append([])
                    last_frame = True
                frames[9].append(b)
            elif (memory == 0) and first_ball:
                first_ball = False
                memory = b
            elif (memory == 0) and not first_ball:
                frames.append([memory,b])
                memory = 0
                first_ball = True
                count = count + 1
            elif (memory + b) == 10: #spare
                first_ball = True
                frames.append([memory,b])
                count = count + 1
                memory = 0
            else:
                first_ball = True
                frames.append([memory,b])
                count = count + 1
                memory = 0
    if v: print frames
    return frames
            
def test_build_frames():
    assert 10 == len(build_frames([0]*20))
    assert 10 == len(build_frames([1] * 20))
    assert 10 == len(build_frames([4] * 20))
    assert 10 == len(build_frames([9,1] * 10 + [9]))
    assert 10 == len(build_frames([10] * 12))
    assert 10 == len(build_frames([10, 5,5] * 5 + [10]))
    assert 10 == len(build_frames([0,0] * 9 + [10,1,0]))
    assert 10 == len(build_frames([0,0] * 8 + [10, 1,0]))
    print 'all tests pass'

def test_bowling():
    assert   0 == bowling([0] * 20)
    assert  20 == bowling([1] * 20)
    assert  80 == bowling([4] * 20)
    assert 190 == bowling([9,1] * 10 + [9])
    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5,5] * 5 + [10])
    assert  11 == bowling([0,0] * 9 + [10,1,0])
    assert  12 == bowling([0,0] * 8 + [10, 1,0])
    bowling([9, 1, 0, 10, 10, 10, 6, 2, 7, 3, 8, 2, 10, 9, 0, 9, 1, 10])
    print 'all tests pass'

