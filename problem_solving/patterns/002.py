"""

input : n

output:
n
n n-1
n n-1 n-2
...
n n-1 n-2 ... 1

Sample input:
5
Sample output:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

"""

n = int(input())

print()
# method 1
for i in range(n):
    for j in range(n, n - i - 1, -1):
        print(j, end=" ")
    print()
print()

# method 2
for i in range(n):
    for j in range(i + 1):
        print(n - j, end=" ")
    print()
