lst = [(), 1, (), (), (1,), ('a',), ('a','b'), ((),), ('a','b'), '']

print("주어진 리스트 :",lst)

for i in range(len(lst)):
    print(lst[i])
    if type(lst[i]) != int and len(lst[i]) == 0:
        del lst[i]
            

print("빈 튜플 요소를 제거한 결과 :",lst)
