from functools import reduce
l = [0,1,2,3,4,5,6,7,8,9]
def f(a, b):
    return a * 10 + b
print(reduce (f,l))
def fake_reduce(function,list):
    outcome = list[0]
    for x in list[1:]:
        outcome = function(outcome,x)
    return outcome
print(fake_reduce(f,l))
