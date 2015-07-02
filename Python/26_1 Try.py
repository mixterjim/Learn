try:
    print 'Try...'
    r = 10/0
    #r = 10/1
    print 'result:', r
except ZeroDivesionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
