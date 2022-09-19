f1 = open('number1to10.txt','r')
f2 = open('numberby10.txt','r')
f3 = open('merge.txt', 'w')

for _ in range(10):
    s1 = int(f1.readline())
    s2 = int(f2.readline())
    f3.write('{} : {}'.format(s1,s2))
    f3.write('\n')

f1.close()
f2.close()
f3.close()

f = open('merge.txt', 'r')

print('merge.txt 파일')
for _ in range(10):
    s = f.readline()
    print(s, end='')

f.close()
