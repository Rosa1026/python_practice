import time

def sum1to1000000():
    start = time.time()
    res = 0
    
    for i in range(1,1000001):
        res += i

    end = time.time()

    return end-start

print("1에서 1,000,000까지의 합을 구하는 시간 : {:.4f}".format(sum1to1000000()))

res = 0

for i in range(100):
    res += sum1to1000000()

print("1,000,000까지의 합을 100번 반복해서 구하는 시간 : {:.4f}".format(res))
