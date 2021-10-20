"""

bit = (B)inary dig(IT) =  0 1

Logical and, or, not
different from
Bitwise and(&), or(|), negation(~), xor(^)


logical                 bitwise
- datatype: bool        -  datatype: any
- logical rules/        -  bitwise operation
  truth table
- and, or, not          - &, |, ~, ^


Ex: True and True       Ex: 5 & 10

===================================================

Theory: Bitwise operator

&               |               ^ (even no 1s = 0, odd no of 1s = 1)
1 & 1 = 1       1 | 1 = 1       1 ^ 1 = 0
1 & 0 = 0       1 | 0 = 1       1 ^ 0 = 1
0 & 1 = 0       0 | 1 = 1       0 ^ 1 = 1
0 & 0 = 0       0 | 0 = 0       0 ^ 0 = 0

~
~1 = 0
~0 = 1


===========================================================


decimal     binary
5           0101
10          1010
&           0000
|           1111
^           1111

ex:
5           00000101
~5          11111010

~n = -(n+1)
~10 = -11
~-10 = 9

"""

print("24 & 2: ", 24 & 2)
print("10 & 5: ", 10 & 5)

print("24 | 2: ", 24 | 2)
print("10 | 5: ", 10 | 5)

print("~2: ", ~2)
print("~5: ", ~5)

print("24 ^ 2: ", 24 ^ 2)
print("10 ^ 5: ", 10 ^ 5)

for i in range(-10, 10):
    print(f"~{i}", ~i, bin(i), bin(~i))


"""

Shifting

5           00000101
5 >> 1      00000010(1) = 2
5 << 1      00001010    = 10

n << x = n * (2**x)
n >> x = n // (2**x)

"""

print(5, 5 >> 1, 5 << 1, 5 << 2)
