n_list = [10,20,30,50,60]
cur = max(n_list)

for i in n_list:
    if cur > i:
        cur = i


print("리스트 원소들 :",n_list)
print("리스트 원소들 중 최솟값 :", cur)

