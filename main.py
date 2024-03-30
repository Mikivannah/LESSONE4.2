class Bird():
   def __init__(self, name, voice, color):
     self.name = name
     self.voice = voice
     self.color = color

   def fly(self):
       print(f"{self.name} летает")
   def eat(self):
       print(f"{self.name} ест")
   def sing(self):
       print(f"{self.name} - поет чирик ")

   def info(self):
        print(f"{self.name} имя")
        print(f"{self.voice} голос")
        print(f"{self.color} окрас птицы")

class Pigeon(Bird):

    def __init__(self, name, voice, color, food):
        super().__init__(name, voice, color)
        self.food = food

    def food(self):
        print(f"{self.name} любит хлебные крошки")

    def wolk(self):
        print(f"{self.name} гуляет")

    def sing(self):
        print(f"{self.name} курлык - курлык" )

bird1 = Pigeon("Гоша", "курлы", "серый","хлебные крошки")
bird2 = Bird("Маша","чирик","коричневый")

bird1.sing()
bird1.info()
bird1.wolk()

bird2.sing()