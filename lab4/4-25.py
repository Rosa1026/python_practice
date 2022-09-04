s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

s1_s = s1.upper().replace(' ','')#중간 공백을 지우기 위해선 replace 이용
s2_s = s2.upper().replace(' ','').replace('-','')
s3_s = s3.upper().replace(' ','')
s4_s = s4.upper().replace(' ','').replace('-','')

print("{}(은)는 {}(으)로 수정됨".format(s1, s1_s))
print("{}(은)는 {}(으)로 수정됨".format(s2, s2_s))
print("{}(은)는 {}(으)로 수정됨".format(s3, s3_s))
print("{}(은)는 {}(으)로 수정됨".format(s4, s4_s))

print("{} : {} 개의 N이 나타남".format(s1_s,s1_s.count('N')))
print("{} : {} 개의 N이 나타남".format(s2_s,s2_s.count('N')))
print("{} : {} 개의 N이 나타남".format(s3_s,s3_s.count('N')))
print("{} : {} 개의 N이 나타남".format(s4_s,s4_s.count('N')))
