import random

numbers = [int(random.random()*200)+9531313113 for _ in range(20)]
names = [int(random.random()*200) for _ in range(20)]

# for name,num in zip(names, numbers):
#     print(name,num)

phonebook = {
    num:name for num,name in zip(numbers,names)
}
# print(phonebook)

for k in phonebook:
    print(k, phonebook[k])

print()

for k in list(sorted(phonebook.keys())):
    print(k, phonebook[k])

print()

for k,v in list(sorted(phonebook.items(), key=lambda t:t[0])):
    print(k, v)

