# flatten means multidimension to 1d

# 2d

m = [
    [1, 2, 3],
    [4, 5],
    [4, 4654, 1131, 4321],
]

l = []
for row in m:
    l.extend(row)
print(l)  # [1, 2, 3, 4, 5, 4, 4654, 1131, 4321]

# 3d

m = [
    [
        [1, 2],
        [2, 3],
    ],
    [
        [11, 256],
        [221, 213, 56],
    ],
]
l = []
for mat in m:
    for row in mat:
        l.extend(row)
print(l)  # [1, 2, 2, 3, 11, 256, 221, 213, 56]
