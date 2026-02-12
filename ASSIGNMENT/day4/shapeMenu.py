import math

def circle():
    r = float(input("Enter radius: "))
    print("Area:", math.pi * r * r)
    print("Perimeter:", 2 * math.pi * r)

def square():
    s = float(input("Enter side: "))
    print("Area:", s * s)
    print("Perimeter:", 4 * s)

def rectangle():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area:", l * b)
    print("Perimeter:", 2 * (l + b))

choice = input("1.Circle 2.Square 3.Rectangle: ")

if choice == "1":
    circle()
elif choice == "2":
    square()
elif choice == "3":
    rectangle()

