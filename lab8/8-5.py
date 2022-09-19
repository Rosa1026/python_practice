f = open('number1to10.txt','w')

for i in range(1,11):
    f.write(str(i))
    if i != 10:
        f.write('\n')

f.close()
f = open('number1to10.txt','r')

s = f.read()
print(s)
f.close()
