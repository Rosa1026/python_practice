scores = (('박동규',88,95,90),
          ('강영민',85,90,95),
          ('박동민',70,90,80),
          ('홍승주',90,90,95))

zip_lst = list(zip(scores[0], scores[1], scores[2], scores[3]))
a, b, c, d = zip(*zip_lst)
print("학생들의 수학 성적의 평균은 {}입니다.".format((a[2]+b[2]+c[2]+d[2])/4))

sum_a, sum_b = 0, 0

for i in range(len(scores)):
    a, b = scores[i][3], scores[i][2]
    sum_a += a
    sum_b += b

total = (sum_a/4 + sum_b/4)/2

print("학생들의 수학과 과학 성적의 평균은 {}입니다.".format(total))

student_dic = {}

for i in range(len(scores)):
    avg = (scores[i][1] + scores[i][2] + scores[i][3])/3
    student_dic[scores[i][0]] = avg

print("이름       평균성적")
print("-------------------")
for i in student_dic:
    print(i,"    {:.2f}".format(student_dic[i]))
