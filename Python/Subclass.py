class Animal(object):
    def run(self):
        print ('Animal is runing...')
Animal().run()
class Dog(Animal):#Inherit form Animal
    pass
Dog().run()
class Cat(Animal):
    def run(self):
        print('Cat is running...')
cat = Cat()
cat.run()
