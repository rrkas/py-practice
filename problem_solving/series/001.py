"""

input:
n m
output:
n + n*n + n*n*n ... m terms

sample input:
5 3
sample output:
155
explanation:
5 + 5*5 + 5*5*5 = 5 + 25 + 125 = 155

"""

l = list(map(int, input().split()))
n = l[0]
m = l[1]

# method 1 : loop
s = 0
for i in range(m):
    s += n ** (i + 1)
print(s)

# method 2 : Geometric Progression
# series = a, a*r, a*r*r, a*r*r*r, ... n terms
# sum = a*(r**(n)-1)/(r-1)
a = n
r = n
s = a * (r ** m - 1) // (r - 1)
print(s)
