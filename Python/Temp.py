name = ['Jim','Bob','Tim',[123,True]]
len(name)
name[-1]
name.append(input("You can't input anything!\n"))
name.pop()
name.insert(0,'Hi')
name[1]=input("What's your name?\n")
number = (1,name)
for n in name:
    print n
x = 100
sum = 0
while x > 0:
    sum = sum + x
    x = x - 2
print sum
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Adam'] = 67
s1 = set([0,1, 1, 2, 2, 3, 3])
s1.add(4)
s1.remove(0)
s2 = set ([1,3,5])
s1 & s2
s1 | s2
