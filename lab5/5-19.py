s_list = ['abc', 'abc', 'opq', 'bcd', 'abba', 'cddc', 'opq']
new_s_list = []

for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)


print(new_s_list)
