inp = input("문자열을 입력하세요 : ").replace(' ','').upper()

lst = list(inp)
rev = []

for i in range(-1,-len(lst)-1,-1):
    rev.append(lst[i])


if rev == lst:
    print("회문입니다.")

else:
    print("회문이 아닙니다.")
