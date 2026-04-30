
class Animal:
    def make_sound(self):
        print("Some generic animal sound")


# Subclasses
class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Bird(Animal):
    def make_sound(self):
        print("Tweet!")
# Instantiate objects
dog = Dog()
cat = Cat()
bird = Bird()

# Call make_sound()
dog.make_sound()
cat.make_sound()
bird.make_sound()