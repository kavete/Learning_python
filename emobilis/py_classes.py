class Circle:
    def __init__(self, radius):
        print(f"Initializing with a radius of { radius } ")
        self.circle_radius = radius

    def calc_area(self):
        a = 22/7 * self.circle_radius ** 2
        print(f"The area is { round(a) }")

    def calc_perimeter(self):
        p = 22/7 * self.circle_radius * 2
        print(f"The Circumference is { round(p) }")


circle1 = Circle(10)
circle2 = Circle(14)
circle3 = Circle(35.5)

circle1.calc_perimeter()
circle1.calc_area()
