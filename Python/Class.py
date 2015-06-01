class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_score(self):
        return '%s: %s' % (self.name, self.score)
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
Bart = Student('Bart', 59)
Lisa = Student('Lisa', 0)    #Defined lisa
Lisa.__init__('Lisa', 87)
Jim = Student('Jim', 0) 
Jim.score = 100
print '%s  %s' % (Bart.get_score(), Bart.get_grade())
name = Lisa
print '%s  %s' % (name.get_score(), name.get_grade())
name = Jim
print '%s  %s' % (name.get_score(), name.get_grade())
