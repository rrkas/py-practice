print()  # blank line
print(1)  # 1
print("abcd")  # abcd
print("ab", 1)  # ab 1
print("a", 1, True)  # a 1 True

# Note:
# each print = java println = c \n = c++ endl
# , = ' '

# Escape char ===============================

print("\\")

# end keyword arg =============================

print("Line 1", "")
print("Line 2")

print("Para 1", 1, True, end="-")
print("Para 2")

# sep keyword arg =============================

print(1, 2, 3)
print(1, 2, 3, sep="*")

# both end and sep ==============================

print(1, 2, 3, sep="+", end="-")
print(4, 5, 6, sep="*", end="")
