class b:
    l=5
    
    def __init__(self):
        l=7
    def p(self):
        return l
def splice(a, b, k):
"""Return a list of the first k elements of a, then all of b, then the rest of a.
>>> spli
e([2, 3, 4, 5℄, [6, 7℄, 2)
[2, 3, 6, 7, 4, 5℄
"""
    return a[:k] + b + a[k:]
def all_splice(a, b, c):
"""Return a list of all k su
h that spli
ing b into a at position k gives 
.
>>> all_spli
e([1, 2℄, [3, 4℄, [1, 3, 4, 2℄)
[1℄
>>> all_spli
e([1, 2, 1, 2℄, [1, 2℄, [1, 2, 1, 2, 1, 2℄)
[0, 2, 4℄
"""
    return [k for k in range(len(a) + 1) if splice(a, b, k) == 


class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

def digits(n):
    """Return the digits of n as a linked list.

    >>> digits(0) is Link.empty
    True
    >>> digits(543)
    Link(5, Link(4, Link(3)))
    """
    s = Link.empty
    while n > 0:
        n, last = n // 10, n % 10
        "*** YOUR CODE HERE ***"
        s= Link(last,s)
    return s

class Fib():
    """A Fibonacci number.
        
    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """
    previous=0

    def __init__(self, value=0):
        self.value = value
    def next(self):
        if(self.value ==0 and self.previous ==0):
            self.value=1
            self.previous=0

        else:
            z=self.previous+self.value
            self.previous=self.value
            self.value= z
        return Fib(self.value)
        "*** YOUR CODE HERE ***"

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    
    def __init__(self, name, quantity, stock=0, balance=0):
        self.name=name
        self.price=quantity
        self.stock=stock
        self.balance=balance
    def vend(self):
        if(self.stock<1):
            return 'Machine is out of stock.'
        elif(self.balance<self.price):
             return 'You must deposit $'+str(self.price-self.balance)+' more.'
        elif(self.balance==self.price):
            self.balance=0
            self.stock-=1
            return 'Here is your '+str(self.name)+'.'
        else:
            z=self.balance-self.price
            self.balance=0
            self.stock-=1
            return 'Here is your '+str(self.name)+' and $'+str(z)+' change.'


    def deposit(self, money):
        if(self.stock<1):
            return 'Machine is out of stock. Here is your $'+str(money)+'.'
        self.balance+=money
        return 'Current balance: $'+str(self.balance)
    def restock(self, e):
        self.stock=self.stock+e
        return 'Current '+str(self.name)+' stock: '+str(self.stock)
class MissManners:
    """A container class that only forwards messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        z=str.replace(message,'please ','',1)
        if hasattr(self.obj, z):
            return getattr(self.obj, z)(*args)
        else:
            return 'Thanks for asking, but I know not how to '+str(z)+'.'
        "*** YOUR CODE HERE ***"
