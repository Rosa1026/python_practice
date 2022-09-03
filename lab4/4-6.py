def cel2fah(cel):
    return (9/5)*cel + 32

for i in [10,20,30,40,50]:
    print("섭씨 {} 도 = 화씨 {} 도".format(i,cel2fah(i)))
