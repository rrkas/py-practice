from random import seed, random, randrange, randint, choice, sample

seed(20)

print(random())
# [0.0, 1.0)

# randrange
print(randrange(20))  # [0, 20)
print(randrange(20, 30))  # [20, 30)
print(randrange(20, 30, 2))  # [20, 30) step 2

# randint
print(randint(20, 30))  # [20, 30)

# choice : 1 element from sequence (list, tuple, etc)
l = [randint(1, 100) for i in range(20)]
print(l)
print(choice(l))

# sample : n elements from sequence (list, tuple, etc)
print(sample(l, 3))
