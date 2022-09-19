f1 = open('random_numbers.txt','r')
f2 = open('random_odd.txt','w')

s = list(f1.readline().split(' '))
         
for i in range(10):
    if int(s[i]) % 2 == 1:
        f2.write(s[i])
        f2.write(' ')

f1.close()
f2.close()

f = open('random_odd.txt','r')
s = f.read()
print(s)
