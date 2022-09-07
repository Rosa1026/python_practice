import random as rd

x = rd.randrange(1,21)
cnt = 1

while True:
    user = int(input("1~20까지의 숫자를 입력하세요 : "))

    if user == x:
        print("정답입니다!")
        print(cnt,"번만에 맞추셨네요. 잘했어요^^")
        break

    elif user > x:
        print(user,"보다 작습니다!")

    else:
        print(user,"보다 큽니다!")
    cnt += 1
