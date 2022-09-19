import random as rd

f = open('random_numbers.txt','w')

for _ in range(10):
    num = rd.randint(1,1000)
    f.write(str(num)+' ')

f.close()

f = open('random_numbers.txt','r')
s = f.read()
print(s)

f.close()
