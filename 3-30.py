def cal(num1, num2, num3):
    if num1 == 1:
        return print("{} + {} = {}".format(num2,num3,num2+num3))
    elif num1 == 2:
        return print("{} - {} = {}".format(num2,num3,num2-num3))
    elif num1 == 3:
        return print("{} * {} = {}".format(num2,num3,num2*num3))
    elif num1 == 4:
        return print("{} / {} = {}".format(num2,num3,num2/num3))


print("1)덧셈 2)뺄셈 3)곱셈 4)나눗셈")
lst = [1,2,3,4]
a = int(input("어떤 연산을 원하는지 번호를 입력하세요: "))

if a not in lst:
    print("잘못 입력하였습니다.")

else:
    print("연산을 원하는 숫자 두개를 입력하세요")
    b = int(input())
    c = int(input())

    cal(a, b, c)
