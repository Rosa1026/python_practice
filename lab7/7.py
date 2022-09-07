import datetime as dt

today = dt.datetime.now()
start = dt.datetime(2019, 2, 24)

#1
gap = today - start

print("춘향이와 몽룡이의 연애 시작일:2019년 2월 24일")
print("연애 시작일로부터 경과한 날짜:'{}'일",gap)

#2
lst = [100,200,500,1000]

print("춘향이와 몽룡이의 연애 시작일:2019년 2월 24일")

for i in lst:
    s = dt.timedelta(days = i)
    print("{}일 기념일 : {}년 {}월 {}일".format(i, (start+s).year, (start+s).month, (start+s).day))
