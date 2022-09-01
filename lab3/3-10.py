a, b = map(int, input("두 정수를 입력하시오 : ").split())

if a % b == 0:
    print("{}는(은) {}의 배수입니다.".format(a, b))

else:
    print("{}는(은) {}의 배수가 아닙니다.".format(a,b))
