"""

input : n

Sample input:
5
Sample output:
01
02 03
04 05 06
07 08 09 10
11 12 13 14 15


"""

n = int(input())

print()
# method 1
last_num = (n * (n + 1)) // 2
dig_count = len(str(last_num))
c = 1
for i in range(n):
    for j in range(i + 1):
        print(str(c).zfill(dig_count), end=" ")
        c += 1
    print()
