#!/usr/bin/python
#Filename:lambda.py

def make_repeater(n):
    return lambda s:s*n

twice = make_repeater(5)

print twice('word')
print twice(5)
