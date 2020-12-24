def gensubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = gensubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new

print(gensubsets([1,2,3,4]))