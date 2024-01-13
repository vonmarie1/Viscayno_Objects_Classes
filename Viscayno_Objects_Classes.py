class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return 2*self.radius*3.14


radius = float(input("Enter the radius of the circle: "))
c = Circle(radius)

print(c.area())
print(c.perimeter())
