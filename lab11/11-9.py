import numpy as np

n = int(input('n을 입력하세요 : '))

a = np.ones((n,n))
b = a
b[1:n-1,1:n-1] = 0

print('a행렬\n',a)
print('b행렬\n',b)
