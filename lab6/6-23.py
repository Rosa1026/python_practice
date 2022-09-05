import string

lst = string.ascii_uppercase

for i in range(10):
    print(lst[i:]+lst[0:i])
