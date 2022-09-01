lst = []

for i in range(100, 1000):
    a = i // 100
    b = (i - (a*100))//10
    c = i % 10

    sum1 = a**3 + b**3 + c**3

    if sum1 == i:
        lst.append(i)

print("세 자리의 암스트롱 수 :", *lst)
