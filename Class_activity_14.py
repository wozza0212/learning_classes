class Polygon():
    '''
    A class to check out the properties of shapes
    '''
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths


    @property
    def num_sides(self):
        return len(self.side_lengths)

    @property
    def perimeter(self):
        return sum(self.side_lengths)


class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__([height, width, height, width])

    @property
    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)


y = Rectangle(5, 10)

print(y.area)
print(y.perimeter)

x = Polygon([8, 8, 8])
print(x.perimeter)

z = Square(5)
print(z.area)
print(z.perimeter)
