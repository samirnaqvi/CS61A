def ab_plus_c(a, b, c):
    """Computes a * b + .

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if a<b:
        return ab_plus_c(b,a,c)
    if b==0:
        return c
    return ab_plus_c(a,b-1,c)+a
    "*** YOUR CODE HERE ***"

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if(b>a):
        return gcd(b,a)
    if(a%b==0):
        return b
    return gcd(b,a%b)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if(n==1):
        return 1
    if(n%2==0):
        b= (int)(n/2)
        return 1+hailstone(b)
    else:
         c= (int)(3*n+1)
         return 1+hailstone(c)