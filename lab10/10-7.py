n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
new_list = []

#1
for i in n_list:
    if i > 0:
        new_list.append(int(i))

print(new_list)

#2
new_list = list(map(int, filter(lambda x: x >0, n_list)))
print(new_list)

#3
new_list = [int(x) for x in n_list if x>0]
print(new_list)
