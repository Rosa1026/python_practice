def factorial(k):
    res = 1
    
    for i in range(2,k+1):
        res *= i

    return res

def euler(n):
    res = 1

    for i in range(1, n+1):
        res += 1/factorial(i)

    return res

print("euler( 5) = {:.5f}".format(euler(5)))
print("euler(20) = {:.5f}".format(euler(20)))
