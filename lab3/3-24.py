n = int(input("숫자를 입력하세요 : "))

result = 0

for i in range(1, n+1):
    result += 1/(i**(2))

print(result)
