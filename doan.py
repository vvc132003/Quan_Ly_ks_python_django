# chuyển đổi nhiệt đô bài 01
def chuyen_doi_nhiet_do():
    nhiet_do_celsius = float(input("Nhập nhiệt độ ở độ Celsius: "))
    nhiet_do_fahrenheit = nhiet_do_celsius * 9 / 5 + 32
    print(f"Nhiệt độ {nhiet_do_celsius} độ Celsius tương ứng với {nhiet_do_fahrenheit} độ Fahrenheit")


# bài 2
def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def tongsonguyento(n):
    tong_nguyen_to = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            tong_nguyen_to += i
    return tong_nguyen_to


def tongcacuocso(n):
    tong_uoc = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc


def tongsochanfor(n):
    tong_chan = 0
    for i in range(2, n + 1, 2):
        tong_chan += i
    return tong_chan


def tốngchanwwhile(n):
    tong_chan = 0
    i = 2
    while i <= n:
        tong_chan += i
        i += 2
    return tong_chan


# bài 3

def demuocsothucsu(n):
    dem = 0
    for i in range(1, n):
        if n % i == 0:
            dem += 1
    return dem


def lasonguyento(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def demuocsole(n):
    dem = 0
    for i in range(1, n + 1, 2):
        if n % i == 0:
            dem += 1
    return dem


def demsonguyentonhohonn(n):
    dem = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            dem += 1
    return dem


def tonguocsothucsu(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong



# bài 4
import math


def find_gcd(a, b):
    return math.gcd(a, b)


def create_array_C(A, B):
    if len(A) != len(B):
        return "Độ dài của hai dãy không bằng nhau"
    C = []
    for i in range(len(A)):
        gcd = find_gcd(A[i], B[i])
        C.append(gcd)
    return C


# bài 5

def kiemtrachuoicon(Str1, Str2):
    return Str2 in Str1

def demsolanxuathien(Str1, Str2):
    dem = 0
    vi_tri = 0
    while True:
        vi_tri = Str1.find(Str2, vi_tri)
        if vi_tri != -1:
            dem += 1
            vi_tri += len(Str2)
        else:
            break
    return dem
def chenchuoi(Str1, Str2, k):
    return Str1[:k] + Str2 + Str1[k:]


# bài 6
import random

def taotaphopA():
    tap_hop_A = set(random.sample(range(1, 1001), 100))
    return tap_hop_A

def taotaphopB(tap_hop_A):
    if tap_hop_A is None:
        print("Tạo tập hợp A trước.")
        return None
    else:
        list_tap_hop_A = list(tap_hop_A)  # Chuyển đổi tap_hop_A thành list
        tap_hop_B = set(random.sample(list_tap_hop_A, 20))
        return tap_hop_B

def taotaphopC(tap_hop_B):
    if tap_hop_B is None:
        print("Tạo tập hợp B trước.")
        return None
    else:
        list_tap_hop_B = list(tap_hop_B)  # Chuyển đổi tap_hop_B thành list
        tap_hop_C = set(random.sample(list_tap_hop_B, 10))
        return tap_hop_C


def hien_thi_tap_hop(tap_hop, ten_tap_hop):
    print(f"Tập hợp {ten_tap_hop}: {tap_hop}")

#bài 7


def indiemlonnhat(dictionary):
    max_score = max(dictionary.values())
    print(f"Điểm lớn nhất là: {max_score}")

def inmondiemlonnhat(dictionary):
    max_score = max(dictionary.values())
    mon_hoc_max = [mon for mon, diem in dictionary.items() if diem == max_score]
    print(f"Môn và điểm có điểm lớn nhất: {', '.join(mon_hoc_max)}: {max_score}")

def indiemsochan(dictionary):
    diem_chan = [diem for diem in dictionary.values() if diem % 2 == 0]
    print(f"Các điểm số chẵn: {diem_chan}")

def tinhtrungbinhdiem(dictionary):
    avg_score = sum(dictionary.values()) / len(dictionary)
    print(f"Trung bình các điểm: {avg_score}")

def taotudienmoi(dictionary):
    tu_dien_moi = {mon: diem for mon, diem in dictionary.items() if diem > 7}
    print(f"Từ điển mới với các môn lớn hơn 7 điểm: {tu_dien_moi}")

def daonguoctudien(dictionary):
    tu_dien_dao = {v: k for k, v in dictionary.items()}
    print(f"Từ điển sau khi đảo ngược: {tu_dien_dao}")


#bài 8

import math
import random

def tong(a, b):
    return a + b

def tich(a, b):
    return a * b

def mu(a, b):
    return a ** b

def can_bac_2(a):
    return math.sqrt(a)

def tan(a):
    return math.tan(a)

def giai_ptb2(a, b, c):
    if a == 0:
        raise ValueError("Phương trình không phải là phương trình bậc 2.")
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt x1 = {x1}, x2 = {x2}"

def random_numbers():
    a = random.randint(1, 100)
    b = random.randint(1, 5)
    c = random.randint(1, 50)
    return a, b, c


#bài 9

def doc_du_lieu_tu_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines

def tinh_tong_da_sos(lines):
    sums = []
    for line in lines[1:]:
        numbers = line.strip().split()
        numbers = [float(num) for num in numbers]
        total = sum(numbers)
        sums.append(total)
    return sums


def ghi_ket_qua_ra_file(filename, sum_all, sums):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Tổng của các dãy số từ fin.txt là: {sum_all}\n")
        for s in sums:
            file.write(f"{s}\n")

# bài 10

def tinh_phan_so():
    try:
        a = int(input("Nhập số nguyên a: "))
        b = int(input("Nhập số nguyên b (khác 0): "))

        phan_so = a / b
        print(f"Giá trị phân số {a}/{b} là: {phan_so}")

    except ValueError:
        print("Lỗi: Bạn cần phải nhập vào số nguyên.")
    except ZeroDivisionError:
        print("Lỗi: Số b không được bằng 0.")

# bài 11
#a) Xây dựng lớp NhanVien:
class NhanVien:
    def __init__(self, hoten, tuoi, luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong

#) Viết hàm nhập dữ liệu cho list các đối tượng NhanVien:
def nhap_danh_sach_nhan_vien():
    danh_sach = []
    for _ in range(2):
        hoten = input("Nhập họ tên: ")
        tuoi = int(input("Nhập tuổi: "))
        luong = float(input("Nhập lương: "))
        nv = NhanVien(hoten, tuoi, luong)
        danh_sach.append(nv)
    return danh_sach
#c) Viết hàm xắp xếp và in ra danh sách nhân viên theo tuổi giảm dần:
def sap_xep_theo_tuoi_giam_dan(danh_sach):
    danh_sach.sort(key=lambda x: x.tuoi, reverse=True)
    for nv in danh_sach:
        print(f"{nv.hoten}, {nv.tuoi} tuổi, lương {nv.luong}")
#d) Viết hàm ghi danh sách nhân viên vào tệp tin NhanVien.txt:
def ghi_danh_sach_vao_file(danh_sach_nv):
    with open('NhanVien.txt', 'w', encoding='utf-8') as file:
        for nv in danh_sach_nv:
            try:
                file.write(f"{nv.hoten}, {nv.tuoi} tuổi, lương {nv.luong}\n")
            except UnicodeEncodeError:
                print(f"Lỗi ở dòng: {nv.hoten}, {nv.tuoi} tuổi, lương {nv.luong}")


#e) Viết hàm đọc file NhanVien.txt và in danh sách nhân viên:
def doc_va_in_danh_sach_tu_file():
    with open('NhanVien.txt', 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

# bài 12

import numpy as np

def tao_vector_x(n):
    return np.arange(-3, 6)[:n]

def tao_ma_tran_random(m, n):
    return np.random.randint(-10, 10, size=(m, n))

def tinh_tich_vector_va_ma_tran(vector, matrix):
    return np.dot(vector, matrix)

def tinh_tich_hai_ma_tran(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

#bài 15
import numpy as np
from sympy import symbols, limit, sqrt, diff, integrate, tan, cos, pi

def solve_equation():
    coeff_matrix = np.array([[2, -5, 1], [4, 2, -2], [1, 1, -1]])
    constants = np.array([-5, 2, 0])

    solution = np.linalg.solve(coeff_matrix, constants)
    return solution


def calculate_limit():
    x = symbols('x')
    f = ((x**3 - 3*x**2)**(1/3)) + ((x**2 - 2*x)**(1/2))
    limit_value = limit(f, x, 5)
    return limit_value



#Viết hàm tính nguyên hàm của hàm f = x/(x2 + 1
def nguyeham():
    # Khai báo biến
    x = symbols('x')
    # Định nghĩa hàm số f(x)
    f_x = x / (x ** 2 + 1)
    # Tính nguyên hàm của f(x)
    integral = integrate(f_x, x)
    # Trả về kết quả
    return integral

def calculate_derivative():
    x = symbols('x')
    f = (2*x - 1) / (x + 2)

    derivative = diff(f, x)
    return derivative


def calculate_integral_with_limits():
    x = symbols('x')
    f = (1 - x*tan(x)) / (x**2 * cos(x) + x)
    integral = integrate(f, (x, 0, 2*pi/3))
    return integral

