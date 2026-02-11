import pandas as pt

names = pt.Series(["Shreya","L", "Naik", "Python"])

# Convert to uppercase
print(names.str.upper())

#to get length of each string
print(names.str.len())

#to convert it into lowercase
print(names.str.lower())

#to find the text
print(names.str.contains("a"))

#to replace the text
print(names.str.replace("a","y"))
