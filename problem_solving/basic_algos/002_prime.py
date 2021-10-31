"""

Check whether number is prime or not.
Prime: The number is divisible by 1 and itself ONLY.

input:
n
output:
YES/ NO

sample input:
40
sample output:
NO

"""

n = int(input())

if n <= 1:
    print("Invalid Input!")
    exit()

prime = True
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break

print("YES" if prime else "NO")
