class Student(object):
    name = 'Jim'
s = Student()
s.name = 'Mirror'
print (s.name)
print (Student().name)
del s.name
print (s.name)
