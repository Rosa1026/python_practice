menu = {'Americano' : 3000, 'Ice Americano' : 3500, 'Cappuccino' : 4000,
        'Cafe Latte' : 4500, 'Espresso' : 3600}

for i in menu:
    print(i,'가격 :',menu[i])

order = input("위의 메뉴 중 하나를 선택하세요 :")

if order in menu:
    print(order+'는 {}원 입니다. 결제를 부탁합니다.'.format(menu[order]))

else:
    print('미안합니다.',order+'는 메뉴에 없습니다.')
