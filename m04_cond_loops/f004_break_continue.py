# break, continue: loops only

# 0..9
# skip 5
# end at 8
for i in range(10):
    if i == 5:
        continue  # skips all lines in the block
    elif i == 8:
        break  # breaks the loop, doesnt execute following lines
    print(i)
