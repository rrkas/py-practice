"""

input : n

Sample input:
5
Sample output:
15 14 13 12 11
10 09 08 07
06 05 04
03 02
01


"""

n = int(input())
c = (n * (n + 1)) // 2
dig_count = len(str(c))

for i in range(n):
    for j in range(n - i):
        print(str(c).zfill(dig_count), end=" ")
        c -= 1
    print()
