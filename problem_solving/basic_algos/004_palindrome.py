"""

Check if a number is palindrome or not.
Palindrome: number = reverse of the number


input:
n
output:
YES/ NO

sample input:
212
sample output:
YES

"""


n = input()
print("YES" if n == n[::-1] else "NO")
