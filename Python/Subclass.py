class Animal(object):
    def run(self):
        print ('Animal is runing...')
Animal().run()
class Dog(Animal):#Inherit form Animal
    def run(self):
        print('Dog is running...')
Dog().run()
class Cat(Animal):
    def run(self):
        print('Cat is running...')
    def sleep(self):
        print('Cat is sleeping...')
cat = Cat()
cat.run()
def sleeping(f_animal):
    f_animal.sleep()
sleeping(Cat())
