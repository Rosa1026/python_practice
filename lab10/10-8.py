from functools import reduce

n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]

#1
print(n_list)
print('최댓값 : {}\n최솟값 : {}'.format(max(n_list), min(n_list)))

#2
def my_max(lst):
    cur = 0
    for i in lst:
        if cur < i:
            cur = i

    return cur

def my_min(lst):
    cur = my_max(lst)
    for i in lst:
        if cur > i:
            cur = i

    return cur

print(n_list)
print('최댓값 : {}\n최솟값 : {}'.format(my_max(n_list), my_min(n_list)))

#3
max_value = reduce(max, n_list)
min_value = reduce(min, n_list)
print(n_list)
print('최댓값 : {}\n최솟값 : {}'.format(max_value, min_value))
