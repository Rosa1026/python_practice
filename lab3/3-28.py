def reverse(a):
    x = a[-1]
    
    for i in range(len(a)-2,-1,-1):
        x += a[i]

    if x == a:
        print("{}은(는) 거꾸로 정수입니다.".format(int(a)))

    else:
        print("{}은(는) 거꾸로 정수가 아닙니다.".format(int(a)))


a = str(input("정수를 입력하시오 : "))

reverse(a)
