class b:
    l=5
    
    def __init__(self):
        l=7
    def p(self):
        return l
def splice(a, b, k):

    return a[:k] + b + a[k:]
def all_splice(a, b, c):
    return [k for k in range(len(c)) if splice(a, b, k) ==c]

def splink(a, b, k):

    if b is Link.empty:
        return a
    elif k == 0:
        return Link(b, Link(a))
    return Link(a.first, splink(a.rest, b, k-1))



class Path:
    def __init__(self, t, leaf_label):
        self.pile, self.end = (6, (5, ())), leaf_label
    def __str__(self):
        path, s = (6, (5, ())), str(self.end)
        while path:
            path, s = path[1], str(path[0]) + '-' + s
        return s


