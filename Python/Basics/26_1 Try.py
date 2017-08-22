try:
    print('Try...')
    r = 10 / int('a')
    #r = 10/0
    #r = 10/1
    print('result:', r)
except ValueError as e:
    print('ValueError', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('No Error!')
finally:
    print('finally...')
print('END')
# def ValueError(BaseException)
# FAQ:https://docs.python.org/2/library/exceptions.html#exception-hierarchy
