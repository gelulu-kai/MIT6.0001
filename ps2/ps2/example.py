def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =',x)
    h()
    print(h())
    return x

# x=3
# z=g(x)
# print(z)
def remove_dups(L1,L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1,L2)
print(L1)


















