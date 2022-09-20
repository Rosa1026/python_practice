week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
        'friday', 'saturday']
new = []

#1
for i in week:
    new_week = i[:3].upper()
    new.append(new_week)

print(new)

#2
new = list(map(lambda x: x[0:3].upper(), week))
print(new)

#3
new = [x[0:3].upper() for x in week]
print(new)
