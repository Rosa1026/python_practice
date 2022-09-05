print("사전 프로그램 시작... 종료는 q를 입력")

dic = {}

while True:
    inp = input("$ ")

    if inp == 'q':
        print("사전 프로그램을 종료합니다.")
        break

    lst = list(inp[2:].split(':'))

    if inp[0] != '>' and inp[0] != '<':
        print("입력오류가 발생했습니다.")

    else:
        if inp[0] == '<':
            dic[lst[0]] = lst[1]

        elif inp[0] == '>':
            if lst[0] not in dic:
                print(lst[0]+"가 사전에 없습니다.")

            else:
                print(dic[lst[0]])
