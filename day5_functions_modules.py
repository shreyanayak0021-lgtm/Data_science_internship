def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

l = int(input("Enter length: "))
w = int(input("Enter width: "))

area, perimeter = calc_rectangle(l, w)
print(f"Area: {area}, Perimeter: {perimeter}")