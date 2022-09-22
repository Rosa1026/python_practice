import numpy as np

a = np.array([0, 10, 20, 40, 60, 80])
b = np.array([0, 20])

res = []

for i in a:
    if i in b:
        res.append(True)
    else:
        res.append(False)

print(res)
