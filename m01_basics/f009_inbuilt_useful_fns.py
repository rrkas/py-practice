a = int(input("a: "))
b = int(input("b: "))

# =========== abs ====================

print("a-b= ", a - b)  # can be negative
print("abs= ", end="")
# absolute value c = |a-b|
c = a - b
if c < 0:
    print(-c, end=" ")
else:
    print(c, end=" ")

print(abs(c))  # for absolute value

# ============= max ===============

d = int(input("d: "))
print("max= ", end="")
if d < a > b:
    print(a, end=" ")
elif d < b > a:
    print(b, end=" ")
else:
    print(d, end=" ")

print(max(a, b, d))

# ========= min ============

print("min=", min(a, b, d))

# ========== len ===========

password = input("Enter password: ")
if len(password) < 8:
    print("Password not valid!")
else:
    print("Acceptable password!")
