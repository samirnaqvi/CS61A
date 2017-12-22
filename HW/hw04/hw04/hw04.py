HW_SOURCE_FILE = 'hw04.py'
from math import sqrt, log, floor
###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(b)-street(a))+abs(avenue(b)-avenue(a))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    z= [sqrt(x) for x in s if sqrt(x)%1<=0.0000001 ]
    b=[int(n) for n in z ]
    return b

    "*** YOUR CODE HERE ***"

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if(n<=3):
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)
        

def g_iter(n):
    """Return the value of G(n), computed iteratively.
    
    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if(n<=3):
        return n
    a=1 
    b= 2
    c=3
    x=3
    while(x<n):
        a,b,c= b,c, c+2*b+3*a
        x=x+1
    return c
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    """def(n):
        return[n+1 if x this else print(x) for x in i_list]"""

    def fun (d,direction,n,n2):
        #print(n,d)
        if(n==0):
            return d
        elif (has_seven(n2-n) or (n2-n)%7==0 ):
            return fun(d+1*(-1*direction),direction*-1,n-1,n2)
        return fun(d+1*direction,direction, n-1,n2)


    """///z=1;
    temp =1 
    d=[]
    direction=1
    while(z<=n):
        
        if(has_seven(z) or z%7==0):
            d=d+[temp]
            direction=direction*-1
        else:
            d=d+[temp]
        z=z+1
        temp=temp+1*direction///"""

    return fun(1,1,n-1,n)
    "*** YOUR CODE HERE ***"

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828

    """
    if(amount<0 ):
        return 0
    if(amount==0 or amount==1 ):
        return 1
    c=log(amount,2)
    c=floor(c)
    """///if(c-temp>=0):
        c=c-temp
    else:
        return count_change(amount-1, temp)
    print("count change",amount,c, temp)"""
    
   

    def count_pow(b,k):
        if(b==0 or k==0):
            return 1
        if(b<0):
            return 0
        return count_pow(b-pow(2,k),k)+count_pow(b,k-1)

    "*** YOUR CODE HERE ***"
    return count_pow(amount, c)

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
