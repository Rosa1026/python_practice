import random as rd

def rcp():
    k = rd.randrange(1,4)
    res = 0
    
    if k == 1:
        res = '가위'

    elif k == 2:
        res = '바위'

    else:
        res = '보'

    return k, res

num_rom, romeo = rcp()
num_jul, juliet = rcp()

print("로미오의 승부 :",romeo)
print("줄리엣의 승부 :",juliet)

if romeo == juliet:
    print("비겼습니다.")

elif num_rom > num_jul:
    if num_rom == 3 and num_jul == 1:
        print("줄리엣이 이겼습니다.")
    else:
        print("로미오가 이겼습니다.")
    
elif num_rom < num_jul:
    if num_jul == 3 and num_rom == 1:
        print("로미오가 이겼습니다.")
    else:
        print("줄리엣이 이겼습니다.")
