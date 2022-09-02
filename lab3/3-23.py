a = int(input("숫자를 입력하세요 : "))
sum = 0

for i in range(1, a+1):
    sum += i**2

print("결과는 {}입니다.".format(sum))
