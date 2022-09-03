from math import pi

def cube(s):
    return s**3

def cuboid(w,h,l):
    return w*h*l

def cone(r,h):
    return (1/3)*(r**2)*h*pi

def orb(r):
    return (4/3)*(r**3)*pi

def cylinder(r,h):
    return (r**2)*h*pi

print("1) 정육면체 2)직육면체 3)원뿔 4) 구 5) 원기둥")
a = int(input("원하는 도형을 고르시오: "))

if a == 1 or a == 4:
    s = int(input("모서리 혹은 반지름의 길이: "))

elif a == 3 or a == 5:
    r, h = map(int, input("반지름과 높이를 입력하시오 : ").split())

else:
    w, h, l = map(int, input("가로, 세로, 높이를 입력하시오 : ").split())


if a == 1:
    print(cube(s))

elif a == 2:
    print(cuboid(w, h, l))

elif a == 3:
    print(cone(r, h))

elif a == 4:
    print(orb(s))

else:
    print(cylinder(r,h))
