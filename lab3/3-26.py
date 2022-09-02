a = int(input("n을 입력하시오 : "))

for i in range(1, a+1):
    if i % 2 == 1:
        for j in range(a*(i-1)+1, a*i+1):
            if j == a*i:
                print(j)
                break
            print(j, end=' ')

    else:
        for j in range(a*i, a*(i-1), -1):
            if j == a*(i-1)+1:
                print(j)
                break
            print(j, end=' ')
