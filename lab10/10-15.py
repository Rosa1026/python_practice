fruits_list = ['Apple = 사과', 'Strawberry = 딸기',
          'Peach = 복숭아', 'Grape = 포도']

#1
fruits1 = {}
for i in fruits_list:
    key = i.split()[0]
    item = i.split()[2]
    fruits1[key] = item

print(fruits1)

#2
cur = [(x.split()[0], x.split()[2]) for x in fruits_list]
fruits2 = dict((x,y) for x,y in cur)
print(fruits2)

#3
rev_cur = [(x.split()[2], x.split()[0]) for x in fruits_list]
rev_fruits = dict((x,y) for x,y in rev_cur)
print(rev_fruits)
