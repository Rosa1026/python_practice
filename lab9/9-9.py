class Counter:
    def __init__(self, number=0):
        self.__number = number

    def reset(self):
        self.__number = 0

    def inc(self):
        self.__number += 1
        if self.__number >= 100:
            self.__number = 0

    def dec(self):
        self.__number -= 1
        if self.__number < 0:
            self.__number = 0
            
    def __str__(self):
        return 'C({})'.format(self.__number)

    def __add__(self, other):
        num = self.__number + other.__number
        if num >= 100:
            num = 0
        return Counter(num)
        
    def __sub__(self, other):
        num = self.__number - other.__number
        if num < 0:
            num = 0
        return Counter(num)


c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =',c3)
print('c4 =',c4)
