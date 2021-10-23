l = []
for i in range(10):
    l.append(i ** 3)
print(l)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

l = [i ** 3 for i in range(10)]
print(l)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

l = [i ** 3 for i in range(10) if i % 2 == 0]
print(l)  # [0, 8, 64, 216, 512]

l = [i ** 3 if i % 2 == 0 else i ** 2 for i in range(10)]
print(l)  # [0, 1, 8, 9, 64, 25, 216, 49, 512, 81]

"""
Syntax:

 - general
   <value/expr> for <var_name> in <iterator>
 - simple if
   <value/expr> for <var_name> in <iterator> if <cond>
 - if-else
   <if_value/if_expr> if <cond> else <else_value/else_expr> for <var_name> in <iterator>

"""
print()

# 2-d list

m = [[c + r * 6 + 1 for c in range(6)] for r in range(5)]
for row in m:
    for col in row:
        print(f"{col:3d}", end="")
    print()
