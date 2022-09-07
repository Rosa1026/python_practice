import time

#1
def Hello():
    start = time.time()

    for _ in range(100):
        print("Hello Python!")

    end = time.time()

    return end-start


print("Hello Python! 출력을 100번 반복하는 시간 : {:.4f}".format(Hello()))

#2
def 
