"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    names =['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
    jobs = ['programmer', 'writer', 'manager', 'designer', 'other' ]
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    devices = ['laptop', 'tablet', 'droid', 'iPhone', 'nothing']
    week = (monday, tuesday, wednesday, thursday, friday) = range(5)
    permutations = list(itertools.permutations(week))
    
    result_set = [[(days[d],
                names[(Hamming, Knuth, Minsky, Simon, Wilkes).index(d)],
                jobs[(programmer, writer, manager, designer, other).index(d)],
                devices[(laptop, tablet, droid, iphone, nothing).index(d)],) for d in week]
              for Hamming, Knuth, Minsky, Simon, Wilkes in permutations
              for laptop, tablet, droid, iphone, nothing in permutations
              for programmer, writer, manager, designer, other in permutations
              if wednesday == laptop
              if programmer != Wilkes
              if set([programmer,droid]) ==set([Wilkes,Hamming])
              if writer != Minsky
              if Knuth != manager and tablet != manager
              if Knuth == Simon + 1
              if thursday != designer
              if friday != tablet
              if designer != droid
              if Knuth  == manager +1
              if monday != writer and set([laptop,Wilkes])==set([monday,writer])
              if tuesday in set([tablet,iphone])
              ]
    result = []
    for r in result_set[0]:
        result.append(r[1])

    return result
