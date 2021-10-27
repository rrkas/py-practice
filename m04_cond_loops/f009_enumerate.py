# print all index of prime number in a list

l = list(range(2, 25))


def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# method 1
for i in range(len(l)):
    v = l[i]
    if isprime(v):
        print(i, end=" ")

print()

# method 2
for i, v in enumerate(l):
    if isprime(v):
        print(i, end=" ")

"""

Enumerate

returns item value along with its index

"""
