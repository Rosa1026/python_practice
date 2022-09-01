x1, y1, x2, y2 = map(int, input("좌표를 입력하세요: ").split(" "))

def distance(x1, y1, x2, y2):
    x_dif = x2 - x1
    y_dif = y2 - y1

    return (x_dif**2+y_dif**2)**(1/2)


print(distance(x1, y1, x2, y2))
