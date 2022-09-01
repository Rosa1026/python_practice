def dev(lst, a):
    summ = 0
    for i in lst:
        summ += (i-a)**2

    return (summ/len(lst))**(1/2)

lst = list(map(int, input("10개의 수를 입력하세요:").split(" ")))

print("합 :", sum(lst))
print("평균 :", sum(lst)/len(lst))
print("표준편차 :", dev(lst, sum(lst)/len(lst)))
