import random as rd

rom = rd.randrange(1,7)
jul = rd.randrange(1,7)

print("로미오의 주사위 숫자는 {} 입니다.".format(rom))
print("줄리엣의 주사위 숫자는 {} 입니다.".format(jul))

if rom > jul:
      print("로미오가 이겼습니다.")
elif rom < jul:
      print("줄리엣이 이겼습니다.")
else:
      print("비겼습니다.")
