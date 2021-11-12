"""

set: list with unique elements

"""

l = [1,2,2,3,3,5,2]
s = {1,2,2,3,3,5,2}
print(l, s)
print(len(l), len(s))

ul = list(set(l))
print(ul)

# print(s[3]) # 'set' object does not support indexing

"""

Note:
    - indexing invalid
    - no slicing

Additional:
    - set operations
        - union
        - intersection
        - difference
        - symmetric difference
        - subset/ superset

"""


