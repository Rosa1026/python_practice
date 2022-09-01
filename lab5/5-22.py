a = int(input("n을 입력하세요 :"))

lst = list(range(1, a**2+1))

for i in range(a):
    if i % 2 == 1:
        s = list(reversed(lst[i*a:i*a+a]))
        print(s)
    else:
        print(lst[a*i:a*i+a])


