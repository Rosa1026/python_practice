def sort3(num1, num2, num3):
    lst = []

    lst.append(num1)
    lst.append(num2)
    lst.append(num3)

    lst.sort()

    return lst

a, b, c = map(int, input("세 수를 입력하세요.:").split(" "))

print(sort3(a,b,c))
