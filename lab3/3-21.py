def check(a):
    cnt = 0
    if a % 2 == 0 and a != 2:
        return False
    
    elif a % 2 != 0:
        for i in range(1, a, 2):
            if a % i == 0:
                cnt += 1

    if cnt > 1:
        return False

    else:
        return True

a = int(input("숫자를 입력하세요 : "))

if check(a):
    print("{}는 소수입니다.".format(a))

else:
    print("{}는 소수가 아닙니다.".format(a))
