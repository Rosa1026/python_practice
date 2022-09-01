record = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)

cur = record[0]
count = 0

for i in record:
    if i < cur:
        count += 1
    cur = i
        

print("일일 매출 기록: ", record)
print("지난 10일 동안 전일대비 매출이 감소한 날은 '{}'일입니다.".format(count))
