#!/usr/bin/python
#Filename:user_defined_exception.py

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Enter something-->')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
    else:
        print s
except EOFError:
    print '\nWhy did you do an EOF on me?'
#except ShortInputException, x:
except ShortInputException as x:
    print 'ShortInputException:The input was length %d, \
            was expecting at least %d.'%(x.length, x.atleast)

else:
    print 'No exception was raised.'
