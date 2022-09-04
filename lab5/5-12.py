n = int(input("n을 입력하세요 : "))

lst = list(map(int, input("{}개의 수를 입력하세요 : ".format(n)).split()))

print("합 :",sum(lst))
print("평균 :",sum(lst)/n)
print("최댓갑 :",max(lst))
print("최솟갑 :",min(lst))
