prompt = "Enter space separated numbers: "

s = input(prompt)

# method 1
m1 = s.split()
l = []
for x in m1:
    l.append(int(x))
print(l)

# method 2
l = [int(x) for x in s.split()]
print(l)
