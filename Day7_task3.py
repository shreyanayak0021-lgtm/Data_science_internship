x = input("Enter file name: ")

try:
    with open(x, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")
