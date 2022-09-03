def fibo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

n = int(input("fibo(n)의 n을 입력하세요: "))
print("fibo({}) =".format(n), fibo(n))
