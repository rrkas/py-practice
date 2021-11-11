"""

tuple: same as list, but non mutable

"""

l = [1, 2, 3]
t = (1, 2, 3)

print(l, t)

l.append(4)

print(l, t)

t1 = ()                     # l = []
print(t1)

t2 = (2,)                   # l = [2]
print(t2)

t3 = (2, 3)                 # l = [2, 3]
print(t3)

t4 = tuple(range(10))       # l = list(range(10))
print(t4)

t5 = tuple(i**2 for i in range(10)) # t5 = [i**2 for i in range(10)]
print(t5)

t6 = 2,
print(t6)

t7 = 2,4,8,10
print(t7)

a= 2
b = 3
print(a,b)

a,b = 5,6
print(a,b)

b,a=a,b
print(a,b)

[a,b] = [2,3]
print(a,b)

[a,b] = [b,a]
print(a,b)

t = tuple(range(25))
print(t)
print(t[:])
print(t[::])
print(t[::-1])
print(t[1:-1:-1])
print(t[1::-1])
print(t[:-1:-1])
print(t[-1::-1])
