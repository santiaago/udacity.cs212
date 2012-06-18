# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 
def inverse_mine(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def fn(y):
        high = float(y)
        low = 0.0
        i = 0
        while True:
            i += 1
            x = ( high + low )/2.
            if abs( f( x ) - y ) < y * 10 **( -12)  or i > 399 :
                return float(x)
            elif f(x) < y:
                low = x + 1.0
            elif f(x) > y:
                high = x - 1.0
    return fn
def inverse(f,delta=1/1024.):
    def fn(y):
        lo,hi = find_bound(f,y)
        return bin_search(f,y,lo,hi,delta)
    return fn
def find_bound(f,y):
    x = 1.
    while f(x) <y:
        x = x*2
    lo = 0. if x==1 else x/2.
    return lo,x
def bin_search(f,y,low,high,delta):
    while low<=high:
        x = (low+high)/2.
        if f(x) < y:
            low = x +delta
        elif f(x) >y:
            high = x -delta
        else:
            return x
    return high if f(high)-y <y-f(low) else low
    
def square(x): return x*x
def power10(x): return 10**x

sqrt = inverse(square)
log10 = inverse(power10)
cuberoot = inverse(lambda x:x*x*x)


def test():
    import math
    nums = [2,4,6,8,10,99,100,101,1000,10000,20000,40000,1000000000]
    for n in nums:
        print '............................................................'
        test1(n, 'sqrt',sqrt(n),math.sqrt(n))
        test1(n, 'log',log10(n),math.log10(n))
        test1(n, '3rd',cuberoot(n),n**(1/3.))
def test1(n,name,value,expected):
    diff = abs(value - expected)
    print '%5g: %s = %13.7f (%13.7f actual); %.4f diff; %s'%(
    n,name,value,expected,diff,('ok' if diff <.002 else '**** BAD ****'))
test()