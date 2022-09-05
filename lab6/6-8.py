tup = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
dup = set()

for i in tup:
    if tup.count(i) > 1:
        dup.add(i)

print("주어진 튜플은 :",tup)
print("중복 원소는 :",dup)
