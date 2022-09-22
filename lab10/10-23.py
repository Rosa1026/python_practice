year, month, day = map(int, input('연월일을 .으로 구분하여 입력하시오(예: 1987.6.10) : ').split('.'))

#1
if year >= 2000:
    print('20세기가 아닙니다.\n제대로 된 입력이 아닙니다.')

#3
elif month > 13:
    print('잘못된 월입니다.\n제대로 된 입력이 아닙니다.')

#4
else:
    print('제대로 된 입력입니다.')
