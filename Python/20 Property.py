class Student(object):
    def get_score(self):
        return self.score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Please enter an integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100!')
        self.score = value
s = Student()
s.set_score(100)
print s.get_score()
