import sys
sys.setrecursionlimit(3927)

def factorial(n):
    if n in [0,1]:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))
