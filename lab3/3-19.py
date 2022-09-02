print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")
inp = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ")

if inp not in ['b','c','p']:
    inp = input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")

if inp == 'c':
    print("치킨을 선택하였습니다.")

elif inp == 'b':
    print("햄버거를 선택하였습니다.")

else:
    print("피자를 선택하였습니다.")
