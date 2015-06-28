class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list):
    __metaclass__ = ListMetaclass
L = MyList()
L.add(1)
print L
