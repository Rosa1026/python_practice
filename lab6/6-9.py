tup = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
dup = set()

for i in tup:
    if i not in dup:
        dup.add(i)

dup = tuple(dup)

print("주어진 튜플은 :",tup)
print("중복 제거 튜플 :",dup)
