class Dogs:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        return self.name

    def age(self):
        return self.age

    def __str__(self):
        return '이름은 {}이고, 나이는 {}살입니다.'.format(self.name, self.age)

my_dog = Dogs('Mango', 3)

print(my_dog)
