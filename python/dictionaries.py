#!/bin/python3

# Dictionaries - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashion": 10}

print(drinks)

employees = { "Finanzas": ["Luis","Hugo","Paco"], "IT": ["Jorge", "Daniel"], "HR": ["Joel","Patricia"] }

employees["Cibersecurity"] = ["Raul","Alex"]

print(employees)

employees.update({ "Sales": ["Omar","Francisco"]})

print(employees)

drinks["Old Fashion"] = 4

print(drinks)

print(drinks.get("White Russian"))