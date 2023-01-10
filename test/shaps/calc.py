# Implement a function rectangle_perimeter that receives as parameter a list that represents the rectangle and
# calculates its perimeter according to the formula provided above. If the provided shape is not a proper rectangle,
# you will not be able to calculate its perimeter, hence you should return None. Otherwise, return the calculated
# perimeter.

import detect


#
#
def rectangle_perimeter(l: list):
    if not detect.is_rectangle(l):
        return None
    perimeter = sum(l)
    return perimeter


#
#
# a = rectangle_perimeter([2, 2, 3, 3])
# print(a)


# Implement a function rectangle_area that receives as parameter a list that represents the rectangle and calculates
# its area according to the formula provided above. If the provided shape is not a proper rectangle, you will not be
# able to calculate its perimeter, hence you should return None. Otherwise, return the calculated area.

def rectangle_area(l: list):
    if not detect.is_rectangle(l):
        return None
    first_elem = l[0]
    for i in l:
        if i != first_elem:
            perimeter = first_elem * i
            return perimeter


#
# p=rectangle_area([10, 2, 10, 2])
# print(p)

# Implement a function triangle_perimeter that receives as parameter a list that represents the triangle and
# calculates its perimeter according to the formula provided above. If the provided shape is not a proper triangle,
# you will not be able to calculate its perimeter, hence you should return None . Otherwise, return the calculated
# perimeter.
def triangle_perimeter(l: list):
    if not detect.is_triangle(l):
        return None
    my_triangle_perimeter = sum(l)
    return my_triangle_perimeter


# a=triangle_perimeter([8, 2, 3] )
# print(a)

# Implement a function triangle_area that receives as parameter a list that represents the triangle and calculates
# its area according to the formula provided above. If the provided shape is not a proper triangle, you will not be
# able to calculate its perimeter, hence you should return None. Otherwise, return the calculated area.

def triangle_area(l: list):
    if not detect.is_triangle(l):
        return None
    a = l[0]
    b = l[1]
    c = l[2]
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
# e=triangle_area([3,4,5])
# print(e)

def square_area(l:list):
    if not detect.is_square(l):
        return None
    first_elem=l[0]
    if first_elem>=0:
        area=first_elem*first_elem
        return area
    return None
# print(square_area([1,1,1,1]))


def square_perimeter(l:list):
    my_perimeter=0
    for i in l:
        my_perimeter+=i
    return my_perimeter
