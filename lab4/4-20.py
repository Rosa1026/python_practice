def fibo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

for i in range(16):
    print("fibo({0:3d}) = {1:4d}".format(i, fibo(i)))

