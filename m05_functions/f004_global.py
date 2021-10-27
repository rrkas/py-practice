a = 10


def func():
    global a
    a = 5
    global b
    b = 20
    print(a)
    print(b)


print(a)
# print(b)
func()
print(a)
print(b)

"""
10
5
20
5
20
"""
