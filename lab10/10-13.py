#1
year = list(filter(lambda x: x%4 == 0 and x%100 != 0, [i for i in range(2001,2031)]))

print('2001년부터 2030년 사이의 윤년 :',year)

#2
year = [x for x in [i for i in range(2001,2031)] if x%4==0 and x%100 !=0]
print('2001년부터 2030년 사이의 윤년 :',year)
