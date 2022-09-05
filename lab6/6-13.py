lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

print("주어진 리스트는 =",lst)

for j in range(len(lst)):
    for i in range(len(lst)-j-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

print("정렬된 결과는 :",lst)
