from mypackage.module1 import m1

_count = 0

def m2():
    global _count
    print("m2")
    if _count < 10:
        _count += 1
        m1()