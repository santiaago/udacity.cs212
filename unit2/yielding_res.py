#generator functions
def ints(s,e=None):
    i = s
    while i <e or not e:
        yield i
        i = i+1
#test 1
L = ints(0,10)
print next(L)
print next(L)
#test 2 infinite loop
L = ints(0)
print next(L)