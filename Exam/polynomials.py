
"""
UNIT 3: Functions and APIs: Polynomials

A polynomial is a mathematical formula like:

    30 * x**2 + 20 * x + 10

More formally, it involves a single variable (here 'x'), and the sum of one
or more terms, where each term is a real number multiplied by the variable
raised to a non-negative integer power. (Remember that x**0 is 1 and x**1 is x,
so 'x' is short for '1 * x**1' and '10' is short for '10 * x**0'.)

We will represent a polynomial as a Python function which computes the formula
when applied to a numeric value x.  The function will be created with the call:

    p1 = poly((10, 20, 30))

where the nth element of the input tuple is the coefficient of the nth power of x.
(Note the order of coefficients has the x**n coefficient neatly in position n of 
the list, but this is the reversed order from how we usually write polynomials.)
poly returns a function, so we can now apply p1 to some value of x:

    p1(0) == 10

Our representation of a polynomial is as a callable function, but in addition,
we will store the coefficients in the .coefs attribute of the function, so we have:

    p1.coefs == (10, 20, 30)

And finally, the name of the function will be the formula given above, so you should
have something like this:

    >>> p1
    <function 30 * x**2 + 20 * x + 10 at 0x100d71c08>

    >>> p1.__name__
    '30 * x**2 + 20 * x + 10'

Make sure the formula used for function names is simplified properly.
No '0 * x**n' terms; just drop these. Simplify '1 * x**n' to 'x**n'.
Simplify '5 * x**0' to '5'.  Similarly, simplify 'x**1' to 'x'.
For negative coefficients, like -5, you can use '... + -5 * ...' or
'... - 5 * ...'; your choice. I'd recommend no spaces around '**' 
and spaces around '+' and '*', but you are free to use your preferences.

Your task is to write the function poly and the following additional functions:

    is_poly, add, sub, mul, power, deriv, integral

They are described below; see the test_poly function for examples.
"""

v = False    
def poly(coefs):
    """Return a function that represents the polynomial with these coefficients.
    For example, if coefs=(10, 20, 30), return the function of x that computes
    '30 * x**2 + 20 * x + 10'.  Also store the coefs on the .coefs attribute of
    the function, and the str of the formula on the .__name__ attribute.'"""
    # your code here (I won't repeat "your code here"; there's one for each function)
    def polynomials(x):
        
        res = 0
        n = 0
        for c in coefs:
            res = res + c * x**n
            n = n + 1
        return res
    def poly_to_string(coefs):
        s = ''
        l = list(range(len(coefs)))
        l.reverse()
        for i in l:
            s = s + str(coefs[i])+' * '+'x**'+str(i) + ' + '
        if v: print s
        s = poly_clean(s)
        return s
    def poly_clean(s):
        if v:
            print '----------------------------------------'
            print 'poly clean'
            print '----------------------------------------'
            print s
        s = s.replace('* x**0 ','')
        if v :print s
        s = s.replace('x**1 ','x ')
        if v: print s
        s = s.replace('+-','-')
        if v: print s
        s = s.replace(' 1 * x', 'x')
        if v: print s
        if s.find('1 * x',0) != -1:
            s = s[4:]
        if v: print s
        s = remove_zeros(s)
        if v: print s
        # this removes the trailing ' + ' at the end
        s = s[:len(s)-3]
        if v: print s
        return s
    def remove_zeros(s):
        if v:
            print '-----------------'
            print 'remove zeros'
            print '-----------------'
        str_zero = ' 0 * '
        str_plus = '+'

        while( s.find(str_zero) != -1):
            if v: print s
            first_zero = s.find(str_zero)
            next_plus = s.find(str_plus,first_zero)
            if next_plus == -1:
                s = s[:first_zero]
            s = s[:first_zero] + s[next_plus +1:]

        s = s.replace('+ 0 ','')
        return s
    polynomials.__name__ = '%s' % poly_to_string(coefs)
    polynomials.coefs = coefs
    return polynomials

def test_poly():
    global p1, p2, p3, p4, p5, p9 # global to ease debugging in an interactive session

    p1 = poly((10, 20, 30))
    assert p1(0) == 10
    for x in (1, 2, 3, 4, 5, 1234.5):
        assert p1(x) == 30 * x**2 + 20 * x + 10
    assert same_name(p1.__name__, '30 * x**2 + 20 * x + 10')

    assert is_poly(p1)
    assert not is_poly(abs) and not is_poly(42) and not is_poly('cracker')

    p3 = poly((0, 0, 0, 1))
    assert p3.__name__ == 'x**3'
    p9 = mul(p3, mul(p3, p3))
    assert p9(2) == 512
    p4 =  add(p1, p3)
    assert same_name(p4.__name__, 'x**3 + 30 * x**2 + 20 * x + 10')

    assert same_name(poly((1, 1)).__name__, 'x + 1')
    assert same_name(power(poly((1, 1)), 10).__name__,
            'x**10 + 10 * x**9 + 45 * x**8 + 120 * x**7 + 210 * x**6 + 252 * x**5 + 210' +
            ' * x**4 + 120 * x**3 + 45 * x**2 + 10 * x + 1')

    assert add(poly((10, 20, 30)), poly((1, 2, 3))).coefs == (11,22,33)
    assert sub(poly((10, 20, 30)), poly((1, 2, 3))).coefs == (9,18,27) 
    assert mul(poly((10, 20, 30)), poly((1, 2, 3))).coefs == (10, 40, 100, 120, 90)
    assert power(poly((1, 1)), 2).coefs == (1, 2, 1) 
    assert power(poly((1, 1)), 10).coefs == (1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1)

    assert deriv(p1).coefs == (20, 60)
    assert integral(poly((20, 60))).coefs == (0, 20, 30)
    p5 = poly((0, 1, 2, 3, 4, 5))
    assert same_name(p5.__name__, '5 * x**5 + 4 * x**4 + 3 * x**3 + 2 * x**2 + x')
    assert p5(1) == 15
    assert p5(2) == 258
    assert same_name(deriv(p5).__name__,  '25 * x**4 + 16 * x**3 + 9 * x**2 + 4 * x + 1')
    assert deriv(p5)(1) == 55
    assert deriv(p5)(2) == 573


def same_name(name1, name2):
    """I define this function rather than doing name1 == name2 to allow for some
    variation in naming conventions."""
    def canonical_name(name): return name.replace(' ', '').replace('+-', '-')
    return canonical_name(name1) == canonical_name(name2)

def is_poly(x):
    "Return true if x is a poly (polynomial)."
    ## For examples, see the test_poly function
    try:
        coefs = x.coefs
    except:
        return False
    for c in x.coefs:
        if not str(c).isdigit():
            return False
    return True
def add(p1, p2):
    "Return a new polynomial which is the sum of polynomials p1 and p2."
    res_coefs = ()
    i_max = max(len(p1.coefs),len(p2.coefs))

    for i in range(i_max):
        if i < len(p1.coefs) and i < len(p2.coefs):
            res_coefs = res_coefs + (p1.coefs[i]+p2.coefs[i],)
        elif i < len(p1.coefs):
            res_coefs = res_coefs + (p1.coefs[i],)
        elif i< len(p2.coefs):
            res_coefs = res_coefs + (p2.coefs[i],)        
    return poly(res_coefs)


def sub(p1, p2):
    "Return a new polynomial which is the difference of polynomials p1 and p2."
    res_coefs = ()
    i_max = max(len(p1.coefs),len(p2.coefs))

    for i in range(i_max):
        if i < len(p1.coefs) and i < len(p2.coefs):
            res_coefs = res_coefs + (p1.coefs[i]-p2.coefs[i],)
        elif i < len(p1.coefs):
            res_coefs = res_coefs + (p1.coefs[i],)
        elif i< len(p2.coefs):
            res_coefs = res_coefs + (-p2.coefs[i],)        
    return poly(res_coefs)

def mul(p1, p2):
    "Return a new polynomial which is the product of polynomials p1 and p2."
    list_poly = []
    move = ()
    index = 0
    for c1 in p1.coefs:
        if index >0:
            move = move + (0,)
        index = index + 1
        c = ()
        for c2 in p2.coefs:
            c = c+ (c1*c2,)
        list_poly.append(poly(move + c))
    poly_result = poly((0,))
    for p in list_poly:
        poly_result = add(poly_result,p)
    return poly_result

def power(p, n):
    "Return a new polynomial which is p to the nth power (n a non-negative integer)."
    power_poly = p
    if n == 0:
        return poly((1,))
    for i in range(n-1):
        power_poly = mul(power_poly,p)
    return power_poly
"""
If your calculus is rusty (or non-existant), here is a refresher:
The deriviative of a polynomial term (c * x**n) is (c*n * x**(n-1)).
The derivative of a sum is the sum of the derivatives.
So the derivative of (30 * x**2 + 20 * x + 10) is (60 * x + 20).

The integral is the anti-derivative:
The integral of 60 * x + 20 is  30 * x**2 + 20 * x + C, for any constant C.
Any value of C is an equally good anti-derivative.  We allow C as an argument
to the function integral (withh default C=0).
"""
    
def deriv(p):
    "Return the derivative of a function p (with respect to its argument)."
    deriv_poly = poly((0,))
    index = 0
    l_coefs = []
    for c in p.coefs:
        if index > 0:
            l_coefs.append(index*c)
        index = index + 1
    deriv_coefs = tuple(l_coefs)
    return poly(deriv_coefs)

def integral(p, C=0):
    "Return the integral of a function p (with respect to its argument)."
    n = len(p.coefs)
    l_coefs = []
    index = 0
    for c in p.coefs:
        if index >0:
            l_coefs.append(c/(index+1))
        else:
            l_coefs.append(c)
        index = index + 1
    integral_coefs = (C,)+ tuple(l_coefs)
    return poly(integral_coefs)
"""
Now for an extra credit challenge: arrange to describe polynomials with an
expression like '3 * x**2 + 5 * x + 9' rather than (9, 5, 3).  You can do this
in one (or both) of two ways:

(1) By defining poly as a class rather than a function, and overloading the 
__add__, __sub__, __mul__, and __pow__ operators, etc.  If you choose this,
call the function test_poly1().  Make sure that poly objects can still be called.

(2) Using the grammar parsing techniques we learned in Unit 5. For this
approach, define a new function, Poly, which takes one argument, a string,
as in Poly('30 * x**2 + 20 * x + 10').  Call test_poly2().
"""
def Poly(str_poly):
    str_poly = str_poly.replace(' ','')
    list_s = str_poly.split('+')
    d_coefs = {}
    power = 0
    coef = 0
    for s in list_s:
        # case of powers > 1
        if s.find('**') != -1:
            i = s.find('**')
            power = int(s[i+2:])
        # base cases power == 1 and ==0
        else:
            i = len(s)
            # has an x <=> the power of one ;-)
            if s.find('x')!= -1:
                power = 1
            else:
                power = 0
        #clean up
        str_coef = s[:i].replace('*x','')
        # nothing left? coef 1 then
        if len(str_coef) == 0:
            coef = 1
        else:
            coef = int(str_coef)
        # add to dictionary
        d_coefs[power] = coef
    list_poly = []
    for n in sorted(d_coefs):
        list_poly.append(d_coefs[n])
    t = tuple(list_poly)
    return poly(t)
#    print d_coefs

def test_poly1():
    # I define x as the polynomial 1*x + 0.
    x = poly((0, 1))
    # From here on I can create polynomials by + and * operations on x.
    newp1 =  30 * x**2 + 20 * x + 10 # This is a poly object, not a number!
    assert p1(100) == newp1(100) # The new poly objects are still callable.
    assert same_name(p1.__name__,newp1.__name__)
    assert (x + 1) * (x - 1) == x**2 - 1 == poly((-1, 0, 1))

def test_poly2():
    newp1 = Poly('30 * x**2 + 20 * x + 10')
    assert p1(100) == newp1(100)
    assert same_name(p1.__name__,newp1.__name__)

