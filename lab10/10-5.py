lyrics = 'Half of my heart is in Havana'

a = lyrics.split()
#1
lst = []
for i in a:
    lst.append((i, len(i)))

print(lst)

#2
l_lst = [(x, len(x)) for x in a]
print(l_lst)
