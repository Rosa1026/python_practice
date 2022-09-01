a, b, c = map(int, input("세 수를 입력하시오 :").split(" "))

def max3(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c

    else:
        if b > c:
            return b
        else:
            return c

def min3(a,b,c):
    if a < b:
        if b < c:
            return a

        else:
            if a < c:
                return a
            else:
                return c

    else:
        if a < c:
            return b
        else:
            if b > c:
                return c
            else:
                return b

def mean3(a, b, c):
    return (a+b+c)/3

print("10, 20, 30의 평균값은", mean3(a, b, c))
print("10, 20, 30의 최댓값은", max3(a, b, c))
print("10, 20, 30의 최솟값은", min3(a, b, c))
