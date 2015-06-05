class USA(object):
    def live(self):
        print ('Batman live in USA')
class Dog(USA):
    def live(self):
        print ('Dog live in USA')
a = list()
b = USA()
c = Dog()
print 'Is list belong list',isinstance(a, list)
print 'is USA belong USA',isinstance(b, USA)
print 'Is Dog belong Dog',isinstance(c, Dog)
print 'Is Dog belong USA',isinstance(c, USA)
