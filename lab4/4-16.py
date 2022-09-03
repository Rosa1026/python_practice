lst = list(map(int, input("쉼표로 구분된 정수를 여러 개 입력하시오 : ").split(',')))

print("입력된 정수의 리스트 :",lst)
lst = sorted(lst)

print("정렬된 정수의 리스트 :", end=' ')
for i in lst:
    print(i, end=' ')
