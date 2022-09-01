lst = list([x for x in range(1, 10001) if x == sum(y for y in range(1,x) if x%y == 0)])

print(lst)

for i in lst:
    s_lst = []
    
    for x in range(1,i):
        if i%x == 0:
            s_lst.append(x)
            
    print("'{}'은 완전수입니다.".format(i))
    print("'{}'의 약수 :".format(i), s_lst, "약수의 합 =", sum(s_lst))
    
