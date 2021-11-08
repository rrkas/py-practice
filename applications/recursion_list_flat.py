def flat(l):
    t = []
    for e in l:
        if isinstance(e,list):
            t.extend(flat(e))
        else:
            t.append(e)
    return t

l = [[[[[1],2],3],4], [[5],6], [7], 8]

print(l)
print(flat(l))