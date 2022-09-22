import numpy as np

#1
a = np.arange(1,11)
print('a =',a)

#2
a2 = np.arange(10,0,-1)
print('a =',a2)

#3
a3 = a2.reshape(2,5)
print(a3)

#4
a4 = a3.reshape(5,2)
print(a4)
