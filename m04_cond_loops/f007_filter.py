# # filter = remove elements on certain criteria


def is_even(n):
    return n % 2 == 0


l = list(range(2, 100, 3))
print(
    l
)  # [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
t = list(filter(is_even, l))
print(t)  # [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98]
