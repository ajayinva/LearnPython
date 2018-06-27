class Shape:
    def __int__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle(Shape):
    """Circle Class"""
    PI = 3.1415
    all_circles = []

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return Circle.PI*self.radius**2

    def __str__(self):
        return "I am a Circle."

    @staticmethod
    def total_area():
        total = 0
        for each_circle in Circle.all_circles:
            total = total + each_circle.area()
        return total


c1 = Circle(2)
c2 = Circle(3)
print(c1.area())
print(c2.area())
print(Circle.total_area())
print(Circle.__doc__)
