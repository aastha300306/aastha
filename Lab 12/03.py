class RectangularSolid:
    def __init__(self):
        self.l = 0
        self.b = 0
        self.h = 0

    def data(self):
        self.l = float(input("Enter length of the solid: "))
        self.b = float(input("Enter width of the solid: "))
        self.h = float(input("Enter height of the solid: "))

    def surface_area(self):
        return 2 * (self.l * self.b + self.l * self.h + self.b * self.h)

    def volume(self):
        return self.l * self.b * self.h

    def display(self):
        print(f"\nRectangular Solid Dimensions:")
        print(f"Length: {self.l}")
        print(f"Width: {self.b}")
        print(f"Height: {self.h}")
        print(f"Surface Area: {self.surface_area():.2f}")
        print(f"Volume: {self.volume():.2f}")

solid = RectangularSolid()
solid.data()
solid.display()