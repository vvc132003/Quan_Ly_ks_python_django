import math
def tong(a, b):
    return a + b
def tich(a, b):
    return a * b
def mu(a, b):
    return math.pow(a, b)
def sin(a):
    return math.sin(math.radians(a))
def canbac2(a):
    return math.sqrt(a)
def giai_phuong_trinh_bac_1(a, b):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Không có nghiệm"
    else:
        x = -b / a
        return x
