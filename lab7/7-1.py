import datetime as dt

today = dt.datetime.now()
start = dt.datetime(2019, 2, 24)

gap = today - start

print("춘향이와 몽룡이의 연애 시작일:2019년 2월 24일")
print("연애 시작일로부터 경과한 날짜:'{}'일",gap)
