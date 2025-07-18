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

def test_create_vector(x,y,z,expected):
    vec = Vector(x,y,z)
    expected = True
    res = isinstance(vec, Vector)

    assert expected == res, f'Ожидали: {expected}, получили: {res}'


def test_create_vector_not_number_x():

    with pytest.raises(TypeError):
        Vector('a',1,3)


def test_create_vector_not_number_y():

    with pytest.raises(TypeError):
        Vector(1,'a',3)


def test_create_vector_not_number_z():

    with pytest.raises(TypeError):
        Vector(1,1,None)


def test_len_vector():
    vec = Vector(-10.3,-5.7,-3.1)
    expected = 12.17
    res = vec.length()

    assert expected == res, f'Ожидали: {expected}, получили: {res}'


def test_add_coordinates_minus():
    vec = Vector(-10.3, -5.7, -3.1)
    vec_1 = Vector(-1,-1,-1)
    new_vec = vec.add(vec_1)

    expected = -11.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = -6.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = -4.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


def test_add_coordinates_plus():
    vec = Vector(10.3, 5.7, 3.1)
    vec_1 = Vector(1,1,1)
    new_vec = vec.add(vec_1)

    expected = 11.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = 6.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = 4.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


def test_add_coordinates_mix():
    vec = Vector(10.3, -5.7, 3.1)
    vec_1 = Vector(-1,1,-1)
    new_vec = vec.add(vec_1)

    expected = 9.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = -4.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = 2.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


def test_add_vector_null():
    vec = Vector(-10.3, -5.7, -3.1)
    vec_1 = Vector(0,0,0)
    new_vec = vec.add(vec_1)

    expected = -10.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = -5.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = -3.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


def test_sub_coordinates_minus():
    vec = Vector(-10.3, -5.7, -3.1)
    vec_1 = Vector(-1,-1,-1)
    new_vec = vec.sub(vec_1)

    expected = -9.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = -4.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = -2.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


def test_sub_coordinates_plus():
    vec = Vector(10.3, 5.7, 3.1)
    vec_1 = Vector(1,1,1)
    new_vec = vec.sub(vec_1)

    expected = 9.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = 4.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = 2.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


def test_sub_coordinates_mix():
    vec = Vector(10.3, -5.7, 3.1)
    vec_1 = Vector(-1,1,-1)
    new_vec = vec.sub(vec_1)

    expected = 11.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = -6.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = 4.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


def test_sub_vector_null():
    vec = Vector(-10.3, -5.7, -3.1)
    vec_1 = Vector(0,0,0)
    new_vec = vec.sub(vec_1)

    expected = -10.3
    assert expected == new_vec.get_x(), f'Ожидали: {expected}, получили: {new_vec.get_x()}'

    expected = -5.7
    assert expected == new_vec.get_y(), f'Ожидали: {expected}, получили: {new_vec.get_y()}'

    expected = -3.1
    assert expected == new_vec.get_z(), f'Ожидали: {expected}, получили: {new_vec.get_z()}'


@pytest.mark.parametrize('x1,y1,z1,x2,y2,z2,scalar',
                         [(1,1,1,10.3,5.7,3.1,27.97),
                          (-1,1,1,-10.3,-5.7,-3.1,27.97),
                          (1,-1,1,-10,-5,-3,-25),
                          (1,1,-1,10.3,5.7,3.1,-7.37),
                          (0,0,0,-10.3,-5.7,-3.1,0),
                          (-10,-5,-3,-10.3,-5.7,-3.1,368.05)])

def test_scalar(x1,y1,z1,x2,y2,z2,scalar):
    vec_1 = Vector(x1,y1,z1)
    vec_2 = Vector(x2,y2,z2)
    expected = scalar

    res = vec_1.scalar_mul(vec_2)

    assert expected == res, f'Ожидали: {expected}, получили: {res}'


@pytest.mark.parametrize('x1,y1,z1,x2,y2,z2,scalar',
                         [(2,1,-1,10.3,5.7,3.1,1.47),
                          (13,1,-1,10.3,5.7,3.1,0.75),
                          (1,2,-1,10.3,5.7,3.1,2.57),
                          (1,1,-1,10.3,5.7,3.1,1.93)
                          ])

def test_angle(x1,y1,z1,x2,y2,z2,scalar):
    vec_1 = Vector(x1,y1,z1)
    vec_2 = Vector(x2,y2,z2)
    expected = scalar

    res = vec_1.angle_between(vec_2)

    assert expected == res, f'Ожидали: {expected}, получили: {res}'

def test_angle_div_zero():
    vec_1 = Vector(0, 0, 0)
    vec_2 = Vector(-10.3, -5.7, -3.1)

    with pytest.raises(ZeroDivisionError):
        vec_1.angle_between(vec_2)

def test_angle_out_scope_definition():
    vec_1 = Vector(-10,-5,-3)
    vec_2 = Vector(-10.3,-5.7,-3.1)

    with pytest.raises(ValueError):
        vec_1.angle_between(vec_2)

def test_random_vector():
    expected = True
    vec = Vector.random()

    res = isinstance(vec.get_x(), int|float)
    assert expected == res, f'Ожидали: {expected}, получили: {res}'

    res = isinstance(vec.get_y(), int | float)
    assert expected == res, f'Ожидали: {expected}, получили: {res}'

    res = isinstance(vec.get_z(), int | float)
    assert expected == res, f'Ожидали: {expected}, получили: {res}'



