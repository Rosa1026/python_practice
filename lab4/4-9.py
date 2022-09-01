import math

lst = list(map(int, input("정수를 여러 개 입력하시오 :").split(" ")))

def mean_of_n(nums):
    sum = 0
    for i in nums:
        sum += i

    return sum/len(nums)

def max_of_n(nums):
    cur = 0
    for i in nums:
        if cur < i:
            cur = i

    return cur

def min_of_n(nums):
    cur = max_of_n(nums)
    for i in nums:
        if cur > i:
            cur = i
    return cur

print("평균값은", mean_of_n(lst))
print("최댓값은", max_of_n(lst))
print("최솟값은", min_of_n(lst))
