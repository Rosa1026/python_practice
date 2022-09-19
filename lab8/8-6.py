f = open('number1to10.txt','r')

print('number1to10.txt 파일을 읽었습니다.')
n = int(input('몇 번째 라인까지 출력하시겠습니까? :'))

for i in range(n):
    print(f.readline(), end='')

f.close()
