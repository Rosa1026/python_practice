import numpy as np

n = int(input('n을 입력하세요 : '))

a = np.ones((n,n))

print('a행렬\n',a)

c = a
c[0,0::] = 0
c[1:n-1:, 0::n-1] = 0
c[n-1, 0::] = 0

print('c행렬\n',c)
