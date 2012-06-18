# ---------------
# User Instructions
#
# Write a function, findtags(text), that takes a string of text
# as input and returns a list of all the html start tags in the 
# text. It may be helpful to use regular expressions to solve
# this problem.

import re

def findtags(text):
    # your code here
    p = re.compile('< *[a-zA-Z]+ *(?: *[a-z_\-A-Z]+(?:="[^"]*")?)* *>')
    res = p.findall(text)
    print '.................'
    for r in res:
        print r
    return res
def findtags_correction(text):
    params = '(\w+\s*=\s*"[^"]*"\s*)*'
    tags = '(<\s*\w+\s*'+params+'\s*/?>)'
    return re.findall(tags,text)
    

testtext1 = """
My favorite website in the world is probably 
<a href="www.udacity.com">Udacity</a>. If you want 
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

testtext2 = """
Okay, so you passed the first test case. <let's see> how you 
handle this one. Did you know that 2 < 3 should return True? 
So should 3 > 2. But 2 > 3 is always False.
"""

testtext3 = """
It's not common, but we can put a LOT of whitespace into 
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I 
don't know why you would ever want to.
"""

def test():
    t1 =  findtags(testtext1) == ['<a href="www.udacity.com">', 
                                   '<b>', 
                                   '<a href="www.udacity.com"target="_blank">']
    print t1
    t2 =   findtags(testtext2) == []
    print t2
    t3 =   findtags(testtext3) == ['<         b           >']
    print t3
    print  'tests pass' if t1 and t2 and t3 else 'errors'
    t1 =  findtags_correction(testtext1) == ['<a href="www.udacity.com">', 
                                   '<b>', 
                                   '<a href="www.udacity.com"target="_blank">']
    print t1
    t2 =   findtags_correction(testtext2) == []
    print t2
    t3 =   findtags_correction(testtext3) == ['<         b           >']
    print t3
    print  'tests pass' if t1 and t2 and t3 else 'errors'
    

print test()