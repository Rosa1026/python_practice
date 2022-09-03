from math import pi

def area_and_circumference(r):
    area = pi*(r**2)
    circumference = 2*pi*r

    return area, circumference

while True:

    r = int(input("반지름을 입력하시오 : "))
    area, cir = area_and_circumference(r)

    if r < 0:
        print("프로그램을 종료합니다.")
        break

    print("넓이 : {:7.3f}, 둘레 : {:7.3f}".format(area, cir))
