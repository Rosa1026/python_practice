tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)
cur = 0
res = 0

for i in tup:
    if tup.count(i) > cur:
        cur = tup.count(i)
        res = i

    elif tup.count(i) == cur:
        res = i

print("주어진 튜플은 :",tup)
print("가장 많이 나타나는 요소는 :",res)
