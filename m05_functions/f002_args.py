# default argument : default value of argument if no value is passed
def area(l, b=None):
    print(l, b)
    if b is None:
        return l * l
    else:
        return l * b


print(area(5))
print(area(5, 10))

print()

# keyword arguments : value for specific argument using = in function call
print(area(b=20, l=10))

print()

# variable arguments
def sum(*args):
    print(args, type(args))
    s = 0
    for val in args:
        s += val
    return s


print(sum(1))
print(sum(1, 20))
print(sum(1, 5, 5, 5, 131, 3131, 431531))

print()

# variable keyword arguments
def key_func(**kwargs):
    print(kwargs, type(kwargs))


key_func(a=1, b=2, c=3)

print()

# all together
def combo(a, b=10, *args, **kwargs):
    # a = positional arg
    # b = default arg
    # args = variable arg
    # kwargs = variable keyword arg
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


combo(10, 50, 4, 5, 6, shlok=100)
