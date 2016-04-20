class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(Mammal):

    def run(self):
        print('Running...')


class Flyable(Bird):

    def fly(self):
        print('Flying...')


class Dog(Runnable):
    pass


class Parrot(Flyable):
    pass
Dog().run()
Parrot().fly()


class Pet(object):
    pass


class Cat(Pet, Runnable):
    pass


class Bat(Pet, Flyable):
    pass
# MixIn


class Chicken(Pet, Runnable, Flyable):
    pass
Cat().run()
Bat().fly()
Chicken().run()
Chicken().fly()
