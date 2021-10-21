l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l, len(l))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 10

# 0..len(l)-1
print(l[5])  # 6
# print(l[10])            # error

# -len(l)...-1
print(l[len(l) - 1])  # 10
print(l[-1])  # 10

print(l[-10])  # 1
print(l[-len(l) + 1])  # 2

del l[6]  # same as remove, but using index and not element value
print(l)  # [1, 2, 3, 4, 5, 6, 8, 9, 10]
