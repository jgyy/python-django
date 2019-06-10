"""Object Oriented Programming"""


class Animal:
    """Inheritance"""
    animal = "ANIMAL"
    eating = "EATING"

    def __init__(self, breed, name, radius=1):
        self.breed = breed
        self.name = name
        self.radius = radius
        print("ANIMAL CREATED")

    def __str__(self):
        return "Breed: {}, Name: {}, Radius: {}".format(self.breed, self.name, self.radius)

    def __len__(self):
        return self.radius

    def __del__(self):
        print("A book is destroyed!")

    def who_am_i(self):
        """who am i"""
        print(self.animal)

    def eat(self):
        """eat"""
        print(self.eating)


MYA = Animal("Lab", "Sammy")
print(MYA, len(MYA))
MYA.who_am_i()
MYA.eat()


class Dog(Animal):
    """CLASS OBJECT ATTRIBUTE"""
    species = "mammal"
    pi = 3.14
    barking = "WOOF"
    dog_eating = "DOG EATING"

    def __init__(self):
        Animal.__init__(self, "Lab", "Sammy")
        print("DOG CREATED")

    def bark(self):
        """bark"""
        print(self.barking)

    def eat(self):
        """eat"""
        print(self.dog_eating)

    def area(self):
        """Area of the circle"""
        return self.radius**2 * self.pi

    def set_radius(self, new_r):
        """set the circle radius"""
        self.radius = new_r


MY_DOG = Dog()
MY_DOG.set_radius(999)
print(MY_DOG.breed, MY_DOG.name, MY_DOG.species, MY_DOG.radius, MY_DOG.area())
del MYA
