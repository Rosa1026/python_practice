myList = [(1,2),(4,5),(4,2),(3,1),(9,4)]

(a, b) = map(int, input("두 정수를 입력하세요 : ").split())

if (a,b) in myList:
    print('{}번째에'.format(myList.index((a,b))+1),(a,b),'요소가 있습니다.')

else:
    if (b,a) in myList:
        print((a,b),'요소는 없으나 {}번째에'.format(myList.index((b,a))+1),(b,a),'요소가 있습니다.')

    else:
        print('이 요소는 없습니다.')
