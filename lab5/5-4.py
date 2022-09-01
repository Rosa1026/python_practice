a = [2,3,4,5,6]
rev_a = []

for _ in range(len(a)):
    b = a.pop()
    rev_a.append(b)

print(rev_a)
