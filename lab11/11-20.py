import numpy as np

#1
a = np.array([[2,1,1], [1,2,1], [1,1,2]])
b = np.array([16,9,3])

res = np.linalg.solve(a,b)
print('x = {}, y = {}, z = {:.1f}'.format(res[0], res[1], res[2]))

#2
res2 = np.linalg.det(a)
print('det(A) =',res2)
