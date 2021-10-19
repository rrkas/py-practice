# input:
# line1: string
# line2: char
# output: index/ error

s = input("Enter string: ")
c = input("Enter char: ")
if len(c) != 1:
    print("Invalid char!")
else:
    if c in s:
        print(s.index(c))  # throws error if c not in s
    else:
        print(f"char '{c}' not in '{s}'")
