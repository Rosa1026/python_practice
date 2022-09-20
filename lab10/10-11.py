word = ['one', 'two', 'three', 'four']
new = []

#1
for i in word:
    new_word = i[0].upper() + i[1:]
    new.append(new_word)

print(new)

#2
new = list(map(lambda x: x[0].upper()+x[1:], word))
print(new)

#3
new = [x[0].upper()+x[1:] for x in word]
print(new)
