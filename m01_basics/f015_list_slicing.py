# slice = part
# very musch like range

"""
Note:

 - l[a:b]   ->      l[a]...l[b-1]
 - l[a:b:c] ->      l[a]...l[b-1] step c
 - a, b, c are optional
   default:
    - a = 0
    - b = len(l)
    - c = 1

 Example:
 - l[:]
 - l[a:]
 - l[:b]
 - l[::]
 - l[::c]
 - l[a::c]
 - l[:b:c]

"""

l = list(range(1, 11))

a = 2
b = 8
c = 3

print(l[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[a:])  # [3, 4, 5, 6, 7, 8, 9, 10]
print(l[:b])  # [1, 2, 3, 4, 5, 6, 7, 8]
print(l[a:b])  # [3, 4, 5, 6, 7, 8]
print(l[::])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[::c])  # [1, 4, 7, 10]
print(l[a::c])  # [3, 6, 9]
print(l[:b:c])  # [1, 4, 7]
print(l[a:b:])  # [3, 4, 5, 6, 7, 8]
print(l[a:b:c])  # [3, 6]
