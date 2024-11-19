from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

#Rectangle
class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimetr(self):
        return (self.__width + self.__height) * 2

#Triangle
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def get_area(self):
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))

    def get_perimetr(self):
        return self.__side_a + self.__side_b + self.__side_c

class Square(Figure):
    def __init__(self, side_a):
        self.side_a = side_a

    def get_area(self):
        return self.side_a ** 2

    def get_perimetr(self):
        return self.side_a * 4

shape = [
    Rectangle(2, 0),
    Triangle(3,3,3),
    Square(5)]
for item in shape:
    print(f'The area is {item.get_area()}')
    print(f'The perimetr {item.get_perimetr()}')