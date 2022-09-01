def num(a):
    sum1 = 1
    sum2 = 1
    
    for i in range(2, a):
        if a % i == 0:
            sum1 += i
    
    for i in range(2,sum1):
        if sum1 % i == 0:
            sum2 += i

    if sum2 == a and sum2 != sum1:
        return sum1


for i in range(1, 20001):
    a = num(i)
    if a != None:
        print("{}의 친화수 {}".format(i, num(i)))
