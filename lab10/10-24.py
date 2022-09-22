a = [(2,5),(1,4),(4,7),(2,3),(2,1)]

a1 = sorted(a, key = lambda x:(x[0], x[-1]))
a2 = sorted(a, key = lambda x:x[1])

print(a1)
print(a2)
