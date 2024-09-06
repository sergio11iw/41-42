class  Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 50
        self.food_to_eat = ['мясо', 'корм', 'печенье']
        self.friend = None
        self.human = None
    def eat(self, food):
        if food in self.food_to_eat:
            self.health += 5
            print('Спасибо')
        else:
            print('Не ем')
    def walk(self):
        self.health += 5
        print('Прогулка')
    def conver(self):
        return self.age*7
    def get_friend(self, dog):
        if abs(dog.age - self.age) < 3:
            print('Теперь ты друг')
            self.friend = dog
            dog.friend = self
        else:
            print('Не друзья')
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 60
        self.dog = None
    def add_dog(self, dog):
        if not dog.human and not self.dog:
            self.dog = dog
            dog.human = self
            print('Мы подружились')
        else:
            print('Не получиться')



dog1 = Dog(name='Тузик', age=2)
dog2 = Dog(name='Чарли', age=4)

dog1.get_friend(dog2)
print()
print(dog1.friend.name)
print(dog2.friend.name)
dog1.eat('мясо')
dog1.eat('броколи')
dog1.walk()
print(dog1.health)
print(dog1.conver())
print()
human = Human('Джек', 23)
human.add_dog(dog1)
human.add_dog(dog2)