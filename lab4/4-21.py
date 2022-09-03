birth = input("주민등록번호 첫 6숫자 형식 입력: ")
nine = str(19)
two = str(20)

if int(birth[0:2]) >= 50:
    nine = nine + birth[0:2]
    print("{}년 {}월 {}일".format(int(nine),int(birth[2:4]),int(birth[4:6])))

else:
    two = two + birth[0:2]
    print("{}년 {}월 {}일".format(int(two),int(birth[2:4]),int(birth[4:6])))
