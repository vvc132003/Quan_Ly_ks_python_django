import doan
import menu
import random


def chuong_1_menu():
    while True:
        menu.menu_chuong_1()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            doan.chuyen_doi_nhiet_do()
        elif lua_chon == '2':
            bai_2_menu()
        elif lua_chon == '3':
            bai_3_menu()
            pass
        elif lua_chon == '4':
            # Dãy số A và B
            A = [12, 24, 36, 48, 60]
            B = [18, 30, 42, 54, 66]
            C = doan.create_array_C(A, B)
            print(f"Dãy C là: {C}")
            pass
        elif lua_chon == '5':
            bai_5_menu()
            pass
        elif lua_chon == '6':
            menu_bai_6()
            pass
        elif lua_chon == '7':
            dictionary_A = {"Toan": 9, "Van": 5, "Su": 8, "Dia": 7, "Hoa": 6}
            menu_bai_7(dictionary_A)
            pass
        elif lua_chon == '8':
            menu_bai_8()
            pass
        elif lua_chon == '9':
            menu_bai_9()
            pass
        elif lua_chon == '10':
            menu_bai_10()
            pass
        elif lua_chon == '11':
            menu_bai_11()
            pass
        elif lua_chon == '0':
            print("Quay lại Menu chương.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def bai_2_menu():
    while True:
        menu.menubai2()
        lua_chon_bai2 = input("Nhập lựa chọn của bạn(a,b,c): ")
        n = int(input("Nhập số tự nhiên n (50 <= n <= 150): "))
        if 50 <= n <= 150:
            if lua_chon_bai2 == 'a':
                tong_nguyen_to = doan.tong_so_nguyen_to_duoi_n(n)
                print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {tong_nguyen_to}")
            elif lua_chon_bai2 == 'b':
                tong_uoc_so = doan.tong_cac_uoc_so(n)
                print(f"Tổng các ước số của {n} là: {tong_uoc_so}")
            elif lua_chon_bai2 == 'c':
                tong_chan_for = doan.tong_so_chan_for_loop(n)
                tong_chan_while = doan.tong_so_chan_while_loop(n)
                print(f"Tổng các số chẵn từ 1 đến {n} (sử dụng vòng lặp for) là: {tong_chan_for}")
                print(f"Tổng các số chẵn từ 1 đến {n} (sử dụng vòng lặp while) là: {tong_chan_while}")
            elif lua_chon_bai2 == '0':
                print("Đã chọn thoát. Kết thúc chương trình.")
                break
        else:
            print("Số không nằm trong khoảng từ 50 đến 150.")


def bai_3_menu():
    while True:
        menu.menubai3()
        lua_chon_bai3 = input("Nhập lựa chọn của bạn(a,b,c,d,e): ")
        n = int(input("Nhập số tự nhiên n (50 <= n <= 150): "))
        if 50 <= n <= 150:
            if lua_chon_bai3 == 'a':
                so_uoc_so = doan.dem_uoc_so_thuc_su(n)
                print(f"Số ước số thực sự của {n} là: {so_uoc_so}")
            elif lua_chon_bai3 == 'b':
                la_so_nguyen_to_kq = "là" if doan.la_so_nguyen_to(n) else "không phải là"
                print(f"{n} {la_so_nguyen_to_kq} số nguyên tố")
            elif lua_chon_bai3 == 'c':
                so_uoc_so_le = doan.dem_uoc_so_le(n)
                print(f"Số ước số lẻ của {n} là: {so_uoc_so_le}")
            elif lua_chon_bai3 == 'd':
                so_nguyen_to_nho_hon_n = doan.dem_so_nguyen_to_nho_hon_n(n)
                print(f"Số số nguyên tố nhỏ hơn {n} là: {so_nguyen_to_nho_hon_n}")
            elif lua_chon_bai3 == 'e':
                tong_uoc_so_thuc_su = doan.tong_uoc_so_thuc_su(n)
                print(f"Tổng tất cả các ước số thực sự của {n} là: {tong_uoc_so_thuc_su}")
            elif lua_chon_bai3 == '0':
                print("Đã chọn thoát. Kết thúc chương trình.")
                break
        else:
            print("Số không nằm trong khoảng từ 50 đến 150.")


def bai_5_menu():
    while True:
        menu.menu_bai_5()
        lua_chon_bai5 = input("Nhập lựa chọn của bạn(1,2,3): ")
        Chuoi_1 = "Đây là ví dụ về chuỗi."
        Chuoi_2 = "ví dụ"
        k = 10
        if lua_chon_bai5 == '1':
            la_chuoi_con = doan.kiem_tra_chuoi_con(Chuoi_1, Chuoi_2)
            if la_chuoi_con:
                print(f"Chuỗi 2 ({Chuoi_2}) nằm trong Chuỗi 1 ({Chuoi_1})")
            else:
                print(f"Chuỗi 2 ({Chuoi_2}) không nằm trong Chuỗi 1 ({Chuoi_1})")
        elif lua_chon_bai5 == '2':
            so_lan_xuat_hien = doan.dem_so_lan_xuat_hien(Chuoi_1, Chuoi_2)
            print(f"Số lần Chuỗi 2 xuất hiện trong Chuỗi 1: {so_lan_xuat_hien}")
        elif lua_chon_bai5 == '3':
            chuoi_moi = doan.chen_chuoi(Chuoi_1, Chuoi_2, k)
            print(f"Sau khi chèn Chuỗi 2 vào vị trí {k}: {chuoi_moi}")
        elif lua_chon_bai5 == '0':
            print("Đã chọn thoát. Kết thúc chương trình.")
            break


def menu_bai_6():
    tap_hop_A = None
    tap_hop_B = None
    tap_hop_C = None

    while True:
        menu.menu_bai_6()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            tap_hop_A = doan.tao_tap_hop_A()
            doan.hien_thi_tap_hop(tap_hop_A, 'A')
        elif lua_chon == '2':
            if tap_hop_A is None:
                print("Tạo tập hợp A trước.")
            else:
                tap_hop_B = doan.tao_tap_hop_B(tap_hop_A)
                doan.hien_thi_tap_hop(tap_hop_B, 'B')
        elif lua_chon == '3':
            if tap_hop_B is None:
                print("Tạo tập hợp B trước.")
            else:
                tap_hop_C = doan.tao_tap_hop_C(tap_hop_B)
                doan.hien_thi_tap_hop(tap_hop_C, 'C')
        elif lua_chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def menu_bai_7(dictionary):
    while True:
        menu.menu_bai_7()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            doan.in_diem_lon_nhat(dictionary)
        elif lua_chon == '2':
            doan.in_mon_diem_lon_nhat(dictionary)
        elif lua_chon == '3':
            doan.in_diem_so_chan(dictionary)
        elif lua_chon == '4':
            doan.tinh_trung_binh_diem(dictionary)
        elif lua_chon == '5':
            doan.tao_tu_dien_moi(dictionary)
        elif lua_chon == '6':
            doan.dao_nguoc_tu_dien(dictionary)
        elif lua_chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def menu_bai_8():
    while True:
        menu.menu_bai_8()
        choice = input("Nhập lựa chọn của bạn: ")
        a, b, c = doan.random_numbers()
        if choice == '1':
            a, b = map(int, input("Nhập hai số cần tính tổng, cách nhau bởi dấu cách: ").split())
            print(f"Tổng của {a} và {b} là: {doan.tong(a, b)}")
        elif choice == '2':
            a, b = map(int, input("Nhập hai số cần tính tích, cách nhau bởi dấu cách: ").split())
            print(f"Tích của {a} và {b} là: {doan.tich(a, b)}")
        elif choice == '3':
            a, b = map(int, input("Nhập số cơ sở và số mũ, cách nhau bởi dấu cách: ").split())
            print(f"{a} mũ {b} là: {doan.mu(a, b)}")
        elif choice == '4':
            a = int(input("Nhập số cần tính căn bậc 2: "))
            print(f"Căn bậc 2 của {a} là: {doan.can_bac_2(a)}")
        elif choice == '5':
            a = float(input("Nhập số cần tính hàm tan: "))
            print(f"Tan của {a} là: {doan.tan(a)}")
        elif choice == '6':
            a, b, c = map(int, input(
                "Nhập hệ số a, b, c của phương trình ax^2 + bx + c = 0, cách nhau bởi dấu cách: ").split())
            print(f"Giai phương trình bậc 2: {doan.giai_ptb2(a, b, c)}")
        elif choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def menu_bai_9():
    while True:
        menu.menu_bai_9()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            lines = doan.doc_du_lieu_tu_file("fin.txt")
            result = doan.tinh_tong_da_sos(lines)
            print(f"Tổng của các dãy số từ fin.txt là: {result}")
        elif choice == '2':
            lines = doan.doc_du_lieu_tu_file("fin.txt")
            sums = doan.tinh_tong_da_sos(lines)
            sum_all = sum(sums)
            doan.ghi_ket_qua_ra_file("fout.txt", sum_all, sums)
            print("Xuất kết quả ra tệp fout.txt thành công.")
        elif choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def menu_bai_10():
    while True:
        print("====== MENU ======")
        print("1. Tính giá trị phân số a/b")
        print("0. Thoát")
        print("==================")
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            doan.tinh_phan_so()
        elif lua_chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def menu_bai_11():
    while True:
        menu.menu_bai_11()
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            danh_sach_nv = doan.nhap_danh_sach_nhan_vien()
        elif choice == '2':
            print("\nDanh sách nhân viên theo tuổi giảm dần:")
            doan.sap_xep_theo_tuoi_giam_dan(danh_sach_nv)
        elif choice == '3':
            doan.ghi_danh_sach_vao_file(danh_sach_nv)
            print("Danh sách nhân viên đã được ghi vào file NhanVien.txt")
        elif choice == '4':
            print("\nDanh sách nhân viên từ file NhanVien.txt:")
            doan.doc_va_in_danh_sach_tu_file()
        elif choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def chuong_2_menu():
    while True:
        menu.menu_chuong_2()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            menu_bai_12()
        elif lua_chon == '12':
            bai_2_menu()
        elif lua_chon == '13':
            bai_3_menu()
            pass
        elif lua_chon == '4':
            # Dãy số A và B
            A = [12, 24, 36, 48, 60]
            B = [18, 30, 42, 54, 66]
            C = doan.create_array_C(A, B)
            print(f"Dãy C là: {C}")
            pass
        elif lua_chon == '0':
            print("Quay lại Menu chương.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
import numpy as np
def menu_bai_12():
    while True:
        menu.menu_bai_12()
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            n_phan_tu = 5
            m, n_hang = 5, 3
            vector_x = doan.tao_vector_x(n_phan_tu)
            matrix_A = doan.tao_ma_tran_random(m, n_hang)
            matrix_B = doan.tao_ma_tran_random(m, n_hang)
            matrix_C = doan.tao_ma_tran_random(n_hang, m)
            print("Vectơ và các ma trận đã được tạo.")
        elif choice == '2':
            result_xA = doan.tinh_tich_vector_va_ma_tran(vector_x, matrix_A)
            print("Tích của vector x và ma trận A:")
            print(result_xA)
        elif choice == '3':
            result_AB = doan.tinh_tich_hai_ma_tran(matrix_A, matrix_B)
            print("\nTích của hai ma trận A và B:")
            print(result_AB)
        elif choice == '4':
            result_CtB = doan.tinh_tich_hai_ma_tran(matrix_C.T, matrix_B)
            print("\nTích của ma trận chuyển vị C và ma trận B:")
            print(result_CtB)
        elif choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")