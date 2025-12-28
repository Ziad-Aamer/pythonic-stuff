# More special methods (similar to operator overloading *, +, ...)
import math


class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __repr__(self):
        """
        valid pytohn representation of the object, that can be used to create the object. Hence, it is more unambigious than str().
        __str__ uses __repr__ if it is not implmented, which makes repre more important. 
        Also, it shows/differentiates between the types used to create the object and not only string representation:
        e.g: d = datetime.date.today()
        str(d) -> '2025-09-15'
        repr(d) -> 'datetime.date(2025, 9, 15)'
        or myClass('3') (str) vs. myClass(3) (int)
        """
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __bool__(self):
        return bool(abs(self)) # The abs value of self will return a magnitude/number, if the number is 0 then False otherwise it is True.
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

v = Vector(1, 2)

print(v)

print(v + v)
print(v * 10)

print(abs(v))

