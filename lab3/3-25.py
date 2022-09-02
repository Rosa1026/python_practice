cur = 7
cnt = 1

while True:
    print("day : {} 달팽이의 위치 : {} 미터".format(cnt, cur))

    cur += 7
    cnt += 1

    if cur >= 30:
        break

    cur -= 5

print("day : {} 달팽이의 위치 : {} 미터".format(cnt, cur))
print("우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(cnt))
