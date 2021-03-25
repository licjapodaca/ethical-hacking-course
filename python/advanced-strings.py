#!/bin/python3

# Advanced Strings

my_name = "George"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                 hello            "
print(too_much_space.strip())

print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) # Improved

# String Interpolation
movie = "The Hangover"
print("My favorite movie is {0}. [{1}]".format(movie, word))