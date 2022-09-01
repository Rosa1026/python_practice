x1, y1, x2, y2 = map(int, input("좌표를 입력하세요: ").split(" "))

def area(x1, y1, x2, y2):
    x_dif = x2 - x1
    y_dif = y2 - y1

    return (x_dif*y_dif)*(1/2)


print(area(x1, y1, x2, y2))
