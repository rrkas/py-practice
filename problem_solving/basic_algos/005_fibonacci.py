"""

Input n, number of terms and print nth term of fibonacci series
Series: 0 1 1 2 3 5 ...

input:
n

sample input:
4
sample output:
2

"""

n = int(input())
a = 0
b = 1
c = -1
if n == 1:
    c = a
elif n >= 2:
    c = b
    for _ in range(n - 2):
        c = a + b
        a = b
        b = c
print(c)
