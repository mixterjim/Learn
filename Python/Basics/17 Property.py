class obj(object):

    def __init__(self):
        self.x = 2
print("Is obj have 'x'?", hasattr(obj(), 'x'))
print('x =', obj().x)
print("Find 'y' in obj.", getattr(obj, 'y', 404))  # Get 'y' in obj,if haven't,return 404
setattr(obj, 'y', 4)  # Add 'y'=4 in obj
print("Find 'y' in obj again.", getattr(obj, 'y'))  # Get 'y' in obj
print('123', type(123))
print("'abc'", type('abc'))
print('abs', type(abs))
print("Is 'abc'=str?", type('abc') == str)
import types


def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print(dir('ABC'))  # Get All about 'ABC'
print(len('ABC') == 'ABC'.__len__())
