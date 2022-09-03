def area(w, h):
    return w*h/2

width = int(input("밑변을 입력하시오:"))
height = int(input("높이를 입력하시오:"))

print("삼각형의 면적 : {}".format(area(width, height)))
