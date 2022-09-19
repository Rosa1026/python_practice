f1 = open('number1to10.txt','r')
f2 = open('numberby10.txt','w')

print('number1to10.txt 파일')
for i in range(10):
    s = int(f1.readline())
    print(s)
    f2.write(str(s*10))
    f2.write('\n')

f1.close()
f2.close()

print('\n')
f = open('numberby10.txt','r')

print('numberby10.txt 파일')    
for i in range(10):
    s = f.readline()
    print(s, end='')
    
f.close()
