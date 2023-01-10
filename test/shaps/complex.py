import detect
import calc


def receives_a_list_of_lists_that_represents_shapes(l: list[list]) -> dict:
    my_dict = {}
    for list in l:
        if detect.is_rectangle(list):
            a = calc.rectangle_perimeter(list)
            b = calc.rectangle_area(list)
            my_dict["rectangle"] = [{"perimeter": a,
                                     "area": b,
                                     "sides": list}]

        elif detect.is_triangle(list):
            c = calc.triangle_area(list)
            d = calc.triangle_perimeter(list)
            my_dict["triangle"] = [{"perimeter": d,
                                    "area": c,
                                    "sides": list}]
        elif detect.is_square(list):
            e = calc.square_perimeter(list)
            f = calc.square_area(list)
            my_dict["square"] = [{"perimeter": e,
                                  "area": f,
                                  "sides": list}]

    return my_dict


print(receives_a_list_of_lists_that_represents_shapes(
    [[2, 2, 2, 2], [3, 4, 5], [2, 3, 2, 3]]))
