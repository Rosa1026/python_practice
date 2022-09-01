n_list = [10,20,30,50,60]
cur = 0

for i in n_list:
    if cur < i:
        cur = i


print("리스트 원소들 중 최댓값 :", cur)
