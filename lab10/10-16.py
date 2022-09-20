test_list = ['No. 224', 'No. 587', 'No. 29', 'No. 37']

#1
num_list1 = []
for i in test_list:
    num = int(i.split()[1])
    num_list1.append(num)

print(num_list1)

#2
num_list2 = [int(x.split()[1]) for x in test_list]
print(num_list2)
