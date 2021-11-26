def fibo(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

def rms(l):
    return _root(_mean(__squared(l)))

def __squared(l):
    return list(i**2 for i in l)

def _mean(l):
    return sum(l) / len(l)

def _root(v):
    return v**0.5

"""
NOTE:
_ and __ are used to indicate private elements

_ can be accessed 
__ should not be accessed

"""