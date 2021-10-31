"""

Reverse digits of a number.

input:
n

sample input:
12345
sample output:
54321

"""

n = int(input())

# method 1
t = n
r = 0
while t > 0:
    r = r * 10 + (t % 10)
    t //= 10
print(r)

# method 2
print(str(n)[::-1])
