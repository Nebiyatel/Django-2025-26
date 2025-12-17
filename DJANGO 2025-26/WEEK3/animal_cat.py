class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animal1 = Animal()
cat1 = Cat()

animal1.make_sound()
cat1.make_sound()
