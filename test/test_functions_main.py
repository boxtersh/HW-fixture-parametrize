import pytest
from main import Vector

@pytest.mark.parametrize('x,y,z,expected',
                         [(1,1,1,True),
                          (-1,1,1,True),
                          (1,-1,1,True),
                          (1,1,-1,True),
                          (0,0,0,True),
                          (-10,-5,-3,True),
                          (-10.3,-5.7,-3.1,True),
                          (10.3,5.7,3.1,True)])

# @pytest.fixture
# def vector():
#     return Vector

def test_create_vector(x,y,z,expected):
    vec = Vector(x,y,z)
    expected = True
    res = isinstance(vec, Vector)

    assert expected == res, f'Ожидали: {expected}, получили: {res}'


def test_len_vector():
    vec = Vector(-10.3,-5.7,-3.1)
    expected = 12.17
    res = vec.length()

    assert expected == res, f'Ожидали: {expected}, получили: {res}'

def test_add_vector():
    vec = Vector(-10.3, -5.7, -3.1)
    vec_1 = Vector(1,1,-1)
    expected = -9.3

    new_vec = vec.add(vec_1)
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = -4.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = -4.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


