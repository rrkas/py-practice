c = 1  # declaration
while c < 10:  # condition
    print(c)  # statements
    c += 1  # increment/decrement
print("After loop")

print("===================")

i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("else", i)

if i >= 10:
    pass
    print("pass:", i)

# while-else if while doesnt execute at all

while False:
    pass
else:
    print("while-else-false")
