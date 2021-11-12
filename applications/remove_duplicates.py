import random

l = [int(random.random()*10) for _ in range(20)]
print(l)

# unordered unique
ul = list(set(l))
print(ul)

# ordered unique
ul = []
for e in l:
    if e not in ul:
        ul.append(e)
print(ul)
