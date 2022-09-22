import numpy as np

n = int(input('n을 입력하세요 : '))

a = np.zeros((n,n))
a[::2, ::2] = 1
a[1::2, 1::2] = 1
print(a)
