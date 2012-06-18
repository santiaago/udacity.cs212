# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!
import itertools
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    max_len=0
    max_pal=(0,0)
    possible_pals = [(x,x+1) for x in range(len(text))]
    print possible_pals
    while len(possible_pals)>0:
        pal = possible_pals.pop()
        print pal
        
        left_pal = (pal[0]-1,pal[1])
        middle_pal = (pal[0]-1,pal[1]+1)
        right_pal = (pal[0],pal[1]+1)
        
        if is_pal(left_pal,text):
            print 'left'+str(left_pal)
            possible_pals.append(left_pal)
        if is_pal(middle_pal,text):
            print 'middle'+str(middle_pal)
            possible_pals.append(middle_pal)
        if is_pal(right_pal,text):
            print 'right'+str(right_pal)
            possible_pals.append(right_pal)
        if pal[1]-pal[0]>max_len:
            max_pal = pal
            max_len = pal[1]-pal[0]
            
    return max_pal
        
def is_pal(p,txt):
    if p[0]<0 or p[1]>len(txt):
        return False
    if txt[p[0]].lower() == txt[p[1]-1].lower():
        return True
    return False
    
def test():
    L = longest_subpalindrome_slice
    #print L('racecar')
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()