#!/bin/python3

# Conditional Statements

def drink(money) :
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "NO drink for you!"

print(drink(3))
print(drink(1))
print("\n\n")

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money!"
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too poor and too young"

print(alcohol(24,7))
print(alcohol(23, 3))
print(alcohol(12,7))
print(alcohol(5, 3))