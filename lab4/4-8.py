a, b, c, d, e, f = map(int, input("여섯 개의 수를 입력하시오 :").split(" "))

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

def max6(a,b,c,d,e,f):
    if max3(a,b,c) > max3(d,e,f):
        return max3(a,b,c)

    else:
        return max3(d,e,f)

def min6(a,b,c,d,e,f):
    if min3(a,b,c) > min3(d,e,f):
        return min3(d,e,f)
    else:
        return min3(a,b,c)

def mean6(a,b,c,d,e,f):
    return (mean3(a,b,c)+mean3(d,e,f))/2

print("10, 20, 30의 평균값은", mean3(a, b, c))
print("10, 20, 30의 최댓값은", max3(a, b, c))
print("10, 20, 30의 최솟값은", min3(a, b, c))

print("평균값은", mean6(a, b, c, d, e, f))
print("최댓값은", max6(a, b, c, d, e, f))
print("최솟값은", min6(a, b, c, d, e, f))
