from test.shaps import detect
from test.shaps import calc



def test1():
    a = detect.is_square([2, 2, 21, 2])
    assert a == True, "this is not a square and  everything should be equal here is an example:[2,2,2,2] "

def test2():
    b=calc.square_area([1,-1,1,1])
    assert b!=None,"the nums are supposed to be positive"


if __name__ == "__main__":
    test1()
    test2()
