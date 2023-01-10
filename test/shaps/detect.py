# Implement a function is_rectangle that receives as parameter a list of side lengths and returns
# True if the provided shape represents a proper rectangle, False otherwise.
def is_rectangle(l: list):
    if len(l) > 4 or len(l) < 4:
        return False
    first_elem = l[0]
    second_elem = l[1]
    third_elem = l[2]
    fourth_elem = l[3]
    if l.count(first_elem) == 2 and l.count(second_elem) == 2 and l.count(third_elem) == 2 and l.count(
            fourth_elem) == 2:
        return True
    return False


# print(is_rectangle([3, 4, 3, 4]))


# Implement a function is_square that receives as parameter a list of side lengths and returns True if the provided
# shape represents a proper square, False otherwise. Note, the following shape: [2, 2, 2, 2] is both rectangle and
# square
#
def is_square(l: list):
    if len(l) > 4 or len(l) < 4:
        return False
    first_elem = l[0]
    if l.count(first_elem) == 4:
        return True
    return False


#
# print(is_square([2, 2, 2, 2]))

# Implement a function is_triangle that receives as parameter a list
# of side lengths and returns True if the provided shape represents a proper triangle, False otherwise

def is_triangle(l: list):
    if len(l) > 3 or len(l) < 3:
        return False
    first_elem = l[0]
    second_elem = l[1]
    third_elem = l[2]
    if first_elem + second_elem < third_elem or first_elem + third_elem < second_elem or second_elem + third_elem < first_elem:
        return False
    return True
#
#
# print(is_triangle([8, 10, 3]))




