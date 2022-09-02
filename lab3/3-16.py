a = int(input("1에서 9까지의 수를 입력하세요 : "))

while True:
    if a > 10 or a < 1:
        a = int(input("1에서 9까지의 수를 다시 입력하세요 : "))

    else:
        break

for i in range(1,10):
    print("{} * {} = {}".format(a, i, a*i))
