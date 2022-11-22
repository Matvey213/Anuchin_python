default_a = 7
default_b = 2
default_c = 8


def triangle_perimeter(a = default_a, b= default_b, c=default_c):
    perimeter = a + b + c
    return perimeter

def triangle_area(a = default_a, b= default_b, c=default_c):
    import math 
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area 

