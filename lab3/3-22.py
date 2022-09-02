def check(a):
    cnt = 0
    for i in range(1, a):
        if a % i == 0:
            cnt += 1

    if cnt > 1:
        return '합성수'

    else:
        return '소수'


for i in range(2, 13):
    print("{} :".format(i), check(i))
