import math

class Circle:
    def __init__(self):
        self.r = 0

    def data(self):
        self.r = float(input("Enter the radius of the circle: "))

    def circumference(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

    def display(self):
        print(f"\nCircle Details:")
        print(f"Radius: {self.r}")
        print(f"Circumference: {self.circumference():.2f}")
        print(f"Area: {self.area():.2f}")

circle = Circle()
circle.data()
circle.display()