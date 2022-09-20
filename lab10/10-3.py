persons = [('GilDong', 'Hong', 27),('SunSin','Lee',46)
           ,('YuSin','Gim',34)]

#1
persons = sorted(persons, key=lambda x:x[1])

print(persons)

#2
persons = sorted(persons, key=lambda x:x[2],reverse = True)

print(persons)
