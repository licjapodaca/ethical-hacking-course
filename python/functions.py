#!/bin/python3

# Functions

def who_am_i(): # this is a function
    name = "Jorge"
    age = 44
    print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

# adding parameters
def add_one_hundred(num) :
    print(num + 100)

add_one_hundred(100)

# Multiple parameters
def add(x,y) :
    print(x+ y)

add(7,7)

def multiply(x,y) :
    return x * y

print(multiply(7,7))

def square_root(x) :
    print(x ** .5)

square_root(64)

def nl() :
    print("\n")

nl()