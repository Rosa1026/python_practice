x, y = map(int, input("두 정수를 입력하시오 : ").split())
cur = 0

if x > 0 and y > 0:
    cur = 1
elif x > 0 and y < 0:
    cur = 4
elif x <0 and y > 0:
    cur = 2
elif x < 0 and y < 0:
    cur = 3


print("{}사분면에 있음".format(cur))
