# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

from functools import update_wrapper
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x,n_ary_f(*args))
    #this line let you show the real function signarute of the decorate function
    #to see this take place type >>>help(seq)
    #you will see seq(x,*args) instead of n_ary_f(x,*args)
    #update_wrapper(n_ary_f,f)
    return n_ary_f

# DECORATOR
@n_ary
def seq(x,y):
    return ('seq',x,y)


#seq = n_ary(seq)
print seq(1)
print seq(1,2)
print seq(1,2,3)