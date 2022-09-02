a, b, c = map(int, input("세 복권번호를 입력하시오 : ").split())

cnt = 0

if a in [2,3,9]:
    cnt += 1

if b in [2,3,9]:
    cnt += 1

if c in [2,3,9]:
    cnt += 1

if cnt == 0:
    print("다음 기회에...")

elif cnt == 1:
    print("상금 1만 원")

elif cnt == 2:
    print("상금 1천만 원")

elif cnt == 3:
    print("상금 1억 원")
