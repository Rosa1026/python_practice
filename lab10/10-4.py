lyrics = 'Half of my heart is in Havana'

a = lyrics.split()

#1
lst = []
for i in a:
    lst.append((i, i.upper()))

print(lst)

#2
l_lst = [(x, x.upper()) for x in a]
print(l_lst)
