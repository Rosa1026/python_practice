student_tuple = (('191101','홍길동','010-123-45xx'),('191102','임꺽정','010-223-45xx'),
                 ('191103','장길산','010-323-45xx'))

s1 = (student_tuple[0][0],student_tuple[0][1])
s2 = (student_tuple[1][0],student_tuple[1][1])
s3 = (student_tuple[2][0],student_tuple[2][1])

dic = dict((s1, s2, s3))

print("학생 정보 :",dic)
while True:
    num = input("학번을 입력하세요 : ")

    if int(num) < 0:
        print("프로그램을 종료합니다.")
        break

    elif num not in dic.keys():
        print("해당 학번의 학생이 없습니다.")

    else:
        print(num+"번 학생은 "+dic[num]+"입니다.")
