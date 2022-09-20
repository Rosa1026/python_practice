n_list = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]
new_list = []

#1
for i in n_list:
    if i % 12 == 0:
        new_list.append(i)

print(new_list)

#2
new_list = list(filter(lambda x: x%12 == 0, n_list))
print(new_list)

#3
new_list = [x for x in n_list if x%12 == 0]
print(new_list)
