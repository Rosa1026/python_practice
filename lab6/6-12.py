lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

print("주어진 리스트는 =",lst)

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print("가장 큰 수를 마지막으로 옮긴 결과 :",lst)
