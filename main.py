# main.py
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

def main():
    print("=== Calculator Demo ===")
    calc = Calculator()
    print("7 + 5 =", calc.add(7, 5))
    print("34 - 21 =", calc.subtract(34, 21))
    print("54 * 2 =", calc.multiply(54, 2))
    print("144 / 2 =", calc.divide(144, 2))
    print("45 / 0 =", calc.divide(45, 0))

    print("\n=== Circle Demo ===")
    try:
        radius = float(input("Enter the radius of the circle: "))
    except ValueError:
        print("Invalid input. Using default radius of 1.0.")
        radius = 1.0
    circle = Circle(radius)
    print("Area of the circle:", circle.area())
    print("Perimeter of the circle:", circle.perimeter())

if __name__ == "__main__":
    main()
