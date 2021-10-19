# in
# not in

s = "abcdef"
l = [1, 2, 3, 4, 5, "a"]

print("b" in s)  # True
print(5 in l)  # True
print("a" in s and "a" in l)  # True
print(6 not in l)  # True
print("e" not in s)  # False
