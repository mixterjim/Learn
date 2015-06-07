def int2(x, base=2):
    return int(x, base)
print int2('10010')
import functools
int2_f = functools.partial(int, base=2)    #def
print int2_f('10010')    #print int('10010', base=2)
list = functools.partial(max, 18)    #get the max number
print list(1,2,3)    #print the max in (18,1,2,3)
