import numpy as np

def get_nth(n, lst):
    fir = int(n / (lst.shape[1]*lst.shape[2]))
    if n % (lst.shape[1]*lst.shape[2]) == 0:
        fir -= 1
    sec = int((n) % lst.shape[1])
    thi = int((n - 6*fir - 3*sec) % lst.shape[2])
    return lst[fir][sec][thi]

a = np.arange(0,24).reshape(4,3,2)

print(a)
while True:
    n = int(input('배열의 몇번째 원소 값을 알고 싶으신가요? : '))

    if n < 1 or n > 24:
        break

    print(get_nth(n, a))
