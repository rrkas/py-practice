# lists = arrays + flexibility

# declaring list
arr = [1, 2, 3, 4, 5]
print(arr)  # [1, 2, 3, 4, 5]

# list operations

arr.append(6)  # insert at last
print(arr)  # [1, 2, 3, 4, 5, 6]

arr.insert(0, 7)  # insert element at specified pos
print(arr)  # [7, 1, 2, 3, 4, 5, 6]

arr.sort()  # sorts ascending order, by default
print(arr)  # [1, 2, 3, 4, 5, 6, 7]

arr.sort(reverse=True)
print(arr)  # [7, 6, 5, 4, 3, 2, 1]

e = arr.pop()  # removes 1 element from end
print(e, arr)  # 1 [7, 6, 5, 4, 3, 2]

arr.append(5)
count = arr.count(5)
print(arr, count)  # [7, 6, 5, 4, 3, 2, 5] 2

arr.clear()
print(arr)  # []

arr.extend([1, 5, 861, 631, 3131])
print(arr)  # [1, 5, 861, 631, 3131]

arr.append([1, 5, 861, 631, 3131])
print(arr)  # [1, 5, 861, 631, 3131, [1, 5, 861, 631, 3131]]
