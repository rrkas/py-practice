"""

recursion:  function calling itself
            function call inside function body

"""

def add1(a,b):
    return a+b

def add2(a,b):
    print("add2:", a,b)
    # if b == 0:
    #     return a
    return add2(a+1, b-1)

print(add1(4,5))
print(add2(4,5))
