fruits = {'Apple':'사과', 'Strawberry':'딸기',
          'Peach':'복숭아', 'Grape':'포도'}

#1
lst = []
for x,y in fruits.items():
    lst.append('{} = {}'.format(x,y))

print(lst)

#2
lst2 = list(map(lambda x : '{} = {}'.format(x[0], x[1]), fruits.items()))
print(lst2)

#3
lst3 = ['{} = {}'.format(x[0],x[1]) for x in fruits.items()]
print(lst3)
