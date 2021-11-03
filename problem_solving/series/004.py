"""

input:
n m
output:
1 + n*n - n*n*n*n + n*n*n*n*n*n ... m terms

sample input:
5 3
sample output:
-599
explanation:
1 + 5*5 - 5*5*5*5 = 1 + 25 - 625 = -599

"""


l = list(map(int, input().split()))
n = l[0]
m = l[1]

# method 1 : loop
s = 1
for i in range(m - 1):
    s += (n * n) * ((-n * n) ** i)
print(s)

# method 2 : Geometric Progression
# series = a, a*r, a*r*r, a*r*r*r, ... n terms
# sum = a*(r**(n)-1)/(r-1)
a = n * n
r = -n * n
s = 1 + a * (r ** (m - 1) - 1) // (r - 1)
print(s)
