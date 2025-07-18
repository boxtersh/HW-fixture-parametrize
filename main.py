from random import randint as rint
import math
# *************** 1. Vector ****************************************************************
class Vector:

    def __init__(self, x: int|float, y: int|float, z: int|float)->None:
        self.x = self.__check_int_float(x)
        self.y = self.__check_int_float(y)
        self.z = self.__check_int_float(z)


    def __check_int_float(self,number):
        if not isinstance(number,int|float):
            raise TypeError('Данные не int или float')

        return number


    def get_x(self)->int|float:
        """
        Функция возвращает координату X вектора
        :return: X
        """
        return self.x


    def get_y(self)->int|float:
        """
        Функция возвращает координату Y вектора
        :return: Y
        """
        return self.y


    def get_z(self)->int|float:
        """
        Функция возвращает координату Z вектора
        :return: Z
        """
        return self.z


    def length(self)->int|float:
        """
        Функция возвращает длину вектора
        Пример А(2,1,2) = (2^2 + 1^2 + 2^2)^0.5 = 3
        :return: int|float
        """
        s = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

        return round(s,2)


    def add(self, other: 'Vector')->'Vector':
        """
        Функция возвращает новый вектор
        как сумму текущего и other вектора
        Примет А(1,2,3) + В(3,2,1) = АВ(4,4,4)
        :param other:
        :return: new vector
        """
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Vector(x, y, z)


    def sub(self, other: 'Vector') -> 'Vector':
        """
        Функция возвращает новый вектор
        как разность текущего и other вектора
        Примет А(1,2,3) - В(3,2,1) = АВ(-2,0,2)
        :param other: переданный вектор
        :return: новый вектор
        """
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vector(x, y, z)


    def scalar_mul(self, other: 'Vector')->int|float:
        """
        Функция возвращает скалярное произведение двух векторов
        текущего и other вектора
        Пример А(1,2,3) В(3,2,1) = АВ(1*3 + 2*2 + 3*1)
        :param other: переданный вектор
        :return: скалярное произведение
        """
        scalar = self.x * other.x + self.y * other.y * self.z * other.z

        return round(scalar, 2)


    def angle_between(self, other: 'Vector')->int|float|None:
        """
        Функция возвращает угол (в радианах) между текущим и other вектором
        Пример А(2,1,2) В(1,0,0) =
        скаляр АВ = (2*1 + 1*0 + 2*0) = 2
        длина А = (2^2 + 1^2 + 2^2)^0.5 = 3
        длина В = (1^2 + 0^2 + 0^2)^0.5 = 1
        cos(угла) = 2 / (3*1)
        rad = arccos(cos(угла)) = 0.841
        :param other: переданный вектор
        :return: radian
        """
        scalar = self.scalar_mul(other)
        length_1 = self.length()
        length_2 = other.length()
        if (length_1 * length_2) == 0:
            raise ZeroDivisionError('На ноль делить нельзя')
        cos = scalar / (length_1 * length_2)

        if cos < -1 or cos > 1:
            raise ValueError('Значения координат векторов вне зоны области определения угла')

        return round(math.acos(cos),2)


    @staticmethod
    def random():
        x = rint(-100,100)
        y = rint(-100, 100)
        z = rint(-100, 100)
        return Vector(x, y, z)


    def __repr__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}'

