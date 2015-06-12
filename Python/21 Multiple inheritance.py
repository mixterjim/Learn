class Animal(object):
    pass

class Mammal(Animal):
    pass
class Bird(Animal):
    pass

class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        return('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass
