class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('Name is %s.' % self.name)
Student('Jim')()
# s=Student('Jim')
