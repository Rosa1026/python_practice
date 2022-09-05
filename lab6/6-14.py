lst = [5, 6, 31, 9, 2, 12, 13, 8, 7]

print("정렬전 리스트는 =",lst)

for j in range(len(lst)):
    for i in range(len(lst)-j-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

    if j < len(lst)-1:
        print("{} 단계 :".format(j+1),lst[:len(lst)-j-1],', ',lst[-j-1:])

print("정렬된 리스트 : ",lst)
