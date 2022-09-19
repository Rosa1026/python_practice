#1
f = open('hello.txt', 'r')
s = f.read()
print("hello.txt 파일 :")
print(s)
f.close()

#2
f = open('hello.txt', 'a')
f.write('\nWelcome to Python!.')
f.close()

f = open('hello.txt', 'r')
s = f.read()
print("hello.txt 파일 :")
print(s)
f.close()
