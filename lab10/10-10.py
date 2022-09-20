new_list = []

#1
for i in range(1,101):
    if i % 6 == 0 and i % 7 == 0:
        new_list.append(i)

print(new_list)

#2
new_list = list(filter(lambda x: x%6 == 0 and x%7 == 0, [i for i in range(1,101)]))
print(new_list)

#3
new_list = [x for x in [i for i in range(1,101)] if x % 6 == 0 and x % 7 == 0]
print(new_list)
