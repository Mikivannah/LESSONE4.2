# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).



import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("Tweet tweet")

    def fly(self):
        print(f"{self.name} is flying")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Roar")

    def run(self):
        print(f"{self.name} is running")

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        print("Hiss")

    def crawl(self):
        print(f"{self.name} is crawling")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Пример использования полиморфизма
animals = [Bird("Polly", 3, "yellow"), Mammal("Leo", 5, "brown"), Reptile("Spike", 2, "green")]
animal_sound(animals)

# Класс Zoo с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Добавился новый - {staff}")

    def save_zoo(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
            print(f"Сохранение зоопарка в файл {filename}")

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
            print(f"Загрузка зоопарка из файла {filename}")
            return zoo

# Пример создания и использования класса Zoo
zoo = Zoo()
zoo.add_animal(Bird("Polly", 3, "yellow"))
zoo.add_animal(Mammal("Leo", 5, "brown"))
zoo.add_staff("ZooKeeper")
zoo.add_staff("Veterinarian")
zoo.save_zoo("zoo.pkl")

# Загрузка зоопарка из файла
new_zoo = Zoo.load_zoo("zoo.pkl")

# Пример использования классов
bird = Bird("Polly", 3, "yellow")
mammal = Mammal("Leo", 5, "brown")
reptile = Reptile("Spike", 2, "green")

bird.make_sound()
bird.fly()

mammal.make_sound()
mammal.run()

reptile.make_sound()
reptile.crawl()