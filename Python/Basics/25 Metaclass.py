class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print("L=", L)

#  Normal list will be Error
i = list()
i.add(1)
