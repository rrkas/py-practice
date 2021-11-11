def add(a,b):
    print(a, b)
    return a+b

add2 = lambda a,b: a+b

print(add(5,6))
print(add2(5,6))

l = list(range(10))
print(l)
l = list(map(lambda x:(x*x) % 17, l))
print(l)
