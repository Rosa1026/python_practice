import random as rd

f = open('randint30.txt','w')

for i in range(30):
    a = rd.randint(1,10)
    f.write(str(a)+' ')

f.close()

f1 = open('randint30.txt','r')

s = list(f1.readline().split(' '))
count = []

for i in range(1,11):
    cnt = 0
    for j in range(30):
        if int(s[j]) == i:
            cnt += 1
    count.append(cnt)

for i in range(1,11):
    print('{} : {}개'.format(i,count[i-1]))
