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
#s.set_score(-1)
print s.get_score()
#-----------------------------#
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score = 99
#s.score = 101
print  s.score
