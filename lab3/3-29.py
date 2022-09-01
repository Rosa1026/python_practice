oil = 500

while oil > 50:
    a = input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오:")

    if a[0] == '+':
        oil += int(a[1:len(a)+1])
        print("현재 탱크양은 {}입니다.".format(oil))

    else:
        oil -= int(a[1:len(a)+1])
        print("현재 탱크양은 {}입니다.".format(oil))


print("경고 : 연료가 10% 미만이니 충전하세요!")
