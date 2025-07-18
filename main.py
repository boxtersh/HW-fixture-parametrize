from random import randint as rint
import math
# *************** 1. Vector ****************************************************************
class Vector:

    def __init__(self, x: int|float, y: int|float, z: int|float)->None:
        self.__x = self.__check_int_float(x)
        self.__y = self.__check_int_float(y)
        self.__z = self.__check_int_float(z)


    def __check_int_float(self,number):
        if not isinstance(number,int|float):
            raise TypeError('Данные не int или float')

        return number


    def get_x(self)->int|float:
        """
        Функция возвращает координату X вектора
        :return: X
        """
        return self.__x


    def get_y(self)->int|float:
        """
        Функция возвращает координату Y вектора
        :return: Y
        """
        return self.__y


    def get_z(self)->int|float:
        """
        Функция возвращает координату Z вектора
        :return: Z
        """
        return self.__z


    def length(self)->int|float:
        """
        Функция возвращает длину вектора
        Пример А(2,1,2) = (2^2 + 1^2 + 2^2)^0.5 = 3
        :return: int|float
        """
        s = (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

        return round(s,2)


    def add(self, other: 'Vector')->'Vector':
        """
        Функция возвращает новый вектор
        как сумму текущего и other вектора
        Примет А(1,2,3) + В(3,2,1) = АВ(4,4,4)
        :param other:
        :return: new vector
        """
        x = self.__x + other.__x
        y = self.__y + other.__y
        z = self.__z + other.__z

        return Vector(x, y, z)


    def sub(self, other: 'Vector') -> 'Vector':
        """
        Функция возвращает новый вектор
        как разность текущего и other вектора
        Примет А(1,2,3) - В(3,2,1) = АВ(-2,0,2)
        :param other: переданный вектор
        :return: новый вектор
        """
        x = self.__x - other.__x
        y = self.__y - other.__y
        z = self.__z - other.__z

        return Vector(x, y, z)


    def scalar_mul(self, other: 'Vector')->int|float:
        """
        Функция возвращает скалярное произведение двух векторов
        текущего и other вектора
        Пример А(1,2,3) В(3,2,1) = АВ(1*3 + 2*2 + 3*1)
        :param other: переданный вектор
        :return: скалярное произведение
        """
        scalar = self.__x * other.__x + self.__y * other.__y * self.__z * other.__z

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
        return f'Вектор с координатами:\nx = {self.__x}, y = {self.__y}, z = {self.__z}'

vector_1 = Vector(1,1,-1)
vector_2 = Vector(10.3,5.7,3.1)
print(vector_1)
print(vector_2)
print(f'Длинна вектора vector_1 = {vector_1.length()}')
print(f'Длинна вектора vector_2 = {vector_2.length()}')
print(f'Сложение векторов vector_1 и vector_2:\n{vector_1.add(vector_2)}')
print(f'Скаляр векторов vector_1 и vector_2 = {vector_1.scalar_mul(vector_2)}')
print(f'Угол между векторами vector_1 и vector_2 в радианах = {vector_1.angle_between(vector_2)}')
print(f'Вектор случайных координат чисел int:\n{vector_1.random()}')
print(f'{'\n' * 2}')

# *************** 2. Circle (с фокусом на параметризацию) *************************************************

class Circle:

    def __init__(self, r: int|float) -> None:
        self.__r = self.__check_int_float(r)

    def __check_int_float(self, r: int|float) -> int|float:
        if not isinstance(r, int|float):
            raise TypeError('Данные не int или float')

        if r < 0 or r == 0:
            raise ValueError('Радиус не может быть отрицательным или равен нулю')

        return r


    def get_r(self):
        """
        Функция возвращает значения поля радиус
        :return: радиус
        """
        return self.__r


    def area(self) -> int|float:
        """
        Функция возвращает площадь круга
        Пример:
        радиус = 13, площадь = 3.14 * 13^2 = 530.93
        :return: площадь круга
        """
        return round(math.pi * self.__r ** 2, 2)


    def circumference(self) -> int|float:
        """
        Функция возвращает длину окружности
        Пример:
        радиус = 13, площадь = 2 * 3.14 * 13 = 81.68
        :return: длина окружности
        """
        return round(2 * math.pi * self.__r, 2)


    def diameter(self) -> int|float:
        """
        Функция возвращает диаметр круга
        Пример:
        радиус = 13, диаметр = 2 * 13 = 26
        :return: диаметр круга
        """
        return round(2 * self.__r, 2)


    def __repr__(self):
        return f'Радиус круга = {self.__r}'

circle = Circle(13)
print(circle)
print(f'Площадь круга = {circle.area()}')
print(f'Длина окружности = {circle.circumference()}')
print(f'Диаметр круга = {circle.diameter()}')