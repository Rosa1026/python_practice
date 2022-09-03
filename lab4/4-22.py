import datetime

date = datetime.datetime.now()
y, m, d = date.year, date.month, date.day

print("현재 시간은 {}년 {}월 {}일입니다.".format(y,m,d))

if m < 10:
    mon = '0'+str(m)

if d < 10:
    day = '0'+str(d)
print("지금 태어난 아이의 주민등록번호 앞자리는 : {}".format(str(y)[2:4] + mon + day))
