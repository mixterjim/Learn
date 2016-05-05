l = [0,1,2,3,4,5,6,7,8,9,]
def f(x):
    return x**2
print(list(map(f,l)))
def fake_map(function,list):
    list_new = []
    for n in list:
        i = function(n)
        list_new.append(i)
    return list_new
print(fake_map(f,l))
