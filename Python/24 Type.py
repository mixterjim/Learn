class Hello(object):
    def hello(self, name='world'):
        print ('Hello, %s.' % name)
#Save as hello.py
#from hello import Hello
h = Hello()
h.hello()
print (type(Hello))
print (type(h))
print "----------------------------"
def fn(self, name='world'):
    print ('Hi, %s.' % name)
Hi = type('Hi',(object,), dict(hello=fn)) #def Hi class
g=Hi()
g.hello()
print (type(Hi))
print (type(g))
