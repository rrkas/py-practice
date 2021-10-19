l = [1, 2, 3, 4, 5]  # list/array

# while loop
i = 0
while i < len(l):
    print(f"{l[i]}**2 = {l[i]**2}")
    i += 1

print("==================")

# for loop, method 1
for e in l:
    print(f"{e}**2 = {e**2}")

print("==================")

# for loop, method 2
for i in range(len(l)):
    print(f"{l[i]}**2 = {l[i]**2}")

print("======= for else ======")

for i in range(len(l)):
    print(f"{l[i]}**2 = {l[i]**2}")
else:
    print("for-else")

for i in range(0):
    pass
else:
    print("for-else-range-0")
