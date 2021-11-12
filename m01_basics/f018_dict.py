"""

dict = dict(ionary)

word: definition

words are unique and immutable, difinition may be duplicate
(symnonyms)

"""

d = {
    2:3,
    "a":"abc",
    # [123,1]:45, # unhashable type: 'list'
    # {1,2}: True, # unhashable type: 'set'
    (2,3):2.3,
    True: False,
    2.3: 5.2,
    2.3: "203",
}

print(d)


d.update({10:20})
d.update({2:40})
print(d)

print(d.get(2))
print(d.get(20))

d[10] = 200
d["30"] = 402
print(d)


print(d[2])
# print(d[20]) # KeyError: 20

d[20] = 10

if d.get(20):
    print(d[20], d.get(20))


print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

print()

for k,v in d.items():
    print(k,v)


del d[20]
print(d)

"""

Note:
    - d.get(k) is safer than d[k]
    - d[k]=v is same as d.update({k:v})


"""