l = list(range(101))
def even(i):
    return i % 2 == 0
print(list(filter(even, l)))
def fake_filter(function, list):
    list_new=[]
    for n in list:
        if function(n) is True:
            list_new.append(n)
    return list_new
print(fake_filter(even, l))
