"""
AND

a       b       a and b
True    True    True
True    False   False
False   True    False
False   False   False
"""

"""
OR

a       b       a or b
True    True    True
True    False   True
False   True    True
False   False   False
"""

"""
a       not a
True    False
False   True
"""

print(True and False)  # False
print(True or False)  # True
print(not True)  # False
print(not not True)  # True
