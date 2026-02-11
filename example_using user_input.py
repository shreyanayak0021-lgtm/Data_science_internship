import pandas as pd

# Take input from user (comma separated values)
user_input = input("Enter names separated by comma: ")

# Convert input string into list
names_list = user_input.split(",")

# Convert list into Pandas Series
names = pd.Series(user_input)

# Convert to uppercase
print("Uppercase:")
print(names.str.upper())

# Get length of each string
print("Length:")
print(names.str.len())

# Convert to lowercase
print("Lowercase:")
print(names.str.lower())

# Remove spaces
print("After removing spaces:")
print(names.str.strip())

# Find letter 'a'
print("Contains 'a':")
print(names.str.contains("a"))

# Replace 'a' with 'y'
print("Replace 'a' with 'y':")
print(names.str.replace("a", "y"))
