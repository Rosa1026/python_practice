class Circle:
    PI = 3.14
    def __init__(self, x, y, r):
        self.__x = x
        self.__y = y
        self.__radius = r

    def __str__(self):
        return 'Circle : (x = {}, y = {}, r = {}), 면적 : {}'.format(self.__x, self.__y, self.__radius, self.area())
                                                    
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_radius(self, r):
        self.__radius = r

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_radius(self):
        return self.__radius
    
    def area(self):
        area = self.PI*(self.__radius)**2
        return area

    def overlaps(self, circle):
        d = ((self.__x - circle.__x)**2 + (self.__y - circle.__y)**2)**(1/2)
        if self.__radius > circle.__radius:
            b = self.__radius
            s = circle.__radius

        else:
            b = circle.__radius
            s = self.__radius
                
        if d < b + s or d > b - s:
            return True
        else:
            return False

    def contains(self, circle):
        d = ((self.__x - circle.__x)**2 + (self.__y - circle.__y)**2)**(1/2)
        if self.__radius > circle.__radius:
            b = self.__radius
            s = circle.__radius

        else:
            b = circle.__radius
            s = self.__radius
            
        if d < b - s:
            return True
        else:
            return False

c1 = Circle(0, 0, 100)
c2 = Circle(0, -10, 10)
c3 = Circle(-100, 0, 120)

print('c1 =', c1)
print('c2 =', c2)
print('c3 =', c3)

print('c1 contains c2 :', c1.contains(c2))
print('c1 contains c3 :', c1.contains(c3))
print('c1 overlaps c2 :', c1.overlaps(c2))
print('c1 overlaps c3 :', c1.overlaps(c3))
