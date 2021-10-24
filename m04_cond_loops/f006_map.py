# mapping : relation of 1 set to another
#           applying a certain function on every element

l = [1, 2, 3, 4, 5]
print(l)  # [1, 2, 3, 4, 5]
t = map(str, l)
print(t)  # <map object at 0x000001BBA9994208>
print(list(t))  # ['1', '2', '3', '4', '5']
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
