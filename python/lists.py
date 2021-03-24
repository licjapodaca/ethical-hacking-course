#!/bin/python3

# Lists - have brackets []

numbers = ["One","Two","Three","Four","Five"]

print(numbers[1]) # returns the second item
print(numbers[1:3]) # starts on the second position and stops in the third position
print(numbers[1:]) # starts to display from the second position to the last item
print(numbers[:3]) # starts from the first position and stops in the third position
print(numbers[-1]) # last item of the list

print(len(numbers)) # length of the list

numbers.append("Six") # appends a value to the end of the list

print(numbers)

numbers.pop() # remove the last item from the list

print(numbers)

numbers.pop(0) # remove the first item from the list

print(numbers)