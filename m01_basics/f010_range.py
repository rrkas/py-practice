# N > M, P in direction of M to N
print(list(range(10)))  # 1 argument:(N)= [0, N)
print(list(range(-10, 10)))  # 2 argument:(M,N) = [M, N)
print(list(range(-10, 10, 3)))  # 2 argument:(M,N,P) = [M, N) step P

# miscellaneous case
print(list(range(0)))  # []
print(list(range(-1)))  # []
print(list(range(10, 0)))  # []
print(list(range(10, 0, 2)))  # []
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]
print(list(range(0, 10, -2)))  # []

# Note: start(M), end(N), step(P) MUST be int
