#!/usr/bin/python
#Filename:class_init.py

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hello, my name is', self.name

p = Person('Shibo')
p.sayHi()

print 'Done'

