



class Animal():
    def make_sound(self):
         pass


class Dog(Animal):
    def make_sound(self):
        print("гав")

class Cat(Animal):
    def make_sound(self):
        print ("мау")



class Cow(Animal):
    def make_sound(self):
        print("муу")


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()




