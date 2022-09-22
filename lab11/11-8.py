import numpy as np

n = int(input('n을 입력하세요 : '))

a = np.zeros((n,n))

for i in range(n):
    a[i,i] = i+1

print(a)
