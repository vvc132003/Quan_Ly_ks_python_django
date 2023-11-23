import doan
import menu


def chuong1():
    while True:
        menu.menuchuong1()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            # tính nhiệt độ
            doan.chuyen_doi_nhiet_do()
        elif lua_chon == '2':
            bai2()
        elif lua_chon == '3':
            bai3()
            pass
        elif lua_chon == '4':
            # bài 4
            # Dãy số A và B
            A = [12, 24, 36, 48, 60]
            B = [18, 30, 42, 54, 66]
            C = doan.create_array_C(A, B)
            print(f"Dãy C là: {C}")
            pass
        elif lua_chon == '5':
            bai5()
            pass
        elif lua_chon == '6':
            bai6()
            pass
        elif lua_chon == '7':
            dictionary_A = {"Toan": 9, "Van": 5, "Su": 8, "Dia": 7, "Hoa": 6}
            bai7(dictionary_A)
            pass
        elif lua_chon == '8':
            bai8()
            pass
        elif lua_chon == '9':
            bai9()
            pass
        elif lua_chon == '10':
            bai10()
            pass
        elif lua_chon == '11':
            bai11()
            pass
        elif lua_chon == '0':
            print("Quay lại Menu chương.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def bai2():
    while True:
        menu.menubai2()
        lua_chon_bai2 = input("Nhập lựa chọn của bạn(a,b,c): ")
        n = int(input("Nhập số tự nhiên n (50 <= n <= 150): "))
        if 50 <= n <= 150:
            if lua_chon_bai2 == 'a':
                #Tính tổng và in ra các số nguyên tố nhỏ hơn n.
                tong_nguyen_to = doan.tongsonguyento(n)
                print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {tong_nguyen_to}")
            elif lua_chon_bai2 == 'b':
                #Tính tổng của tất cả các ước số của n
                tong_uoc_so = doan.tongcacuocso(n)
                print(f"Tổng các ước số của {n} là: {tong_uoc_so}")
            elif lua_chon_bai2 == 'c':
                #Tính tổng các số chẵn từ 1 đến n bằng hai cách: sử dụng vòng lặp for và vòng lặp while
                tong_chan_for = doan.tongsochanfor(n)
                tong_chan_while = doan.tốngchanwwhile(n)
                print(f"Tổng các số chẵn từ 1 đến {n} (sử dụng vòng lặp for) là: {tong_chan_for}")
                print(f"Tổng các số chẵn từ 1 đến {n} (sử dụng vòng lặp while) là: {tong_chan_while}")
        elif lua_chon_bai2 == '0':
            print("Đã chọn thoát. Kết thúc chương trình.")
            break
        else:
            print("Số không nằm trong khoảng từ 50 đến 150.")


def bai3():
    while True:
        menu.menubai3()
        lua_chon_bai3 = input("Nhập lựa chọn của bạn(a,b,c,d,e): ")
        n = int(input("Nhập số tự nhiên n (50 <= n <= 150): "))
        if 50 <= n <= 150:
            if lua_chon_bai3 == 'a':
                #Hàm trả lại số các ước số thực sự của n.
                so_uoc_so = doan.demuocsothucsu(n)
                print(f"Số ước số thực sự của {n} là: {so_uoc_so}")
            elif lua_chon_bai3 == 'b':
                #Hàm trả lại 1 nếu n là nguyên tố, ngược lại hàm trả về 0.
                la_so_nguyen_to_kq = "là" if doan.lasonguyento(n) else "không phải là"
                print(f"{n} {la_so_nguyen_to_kq} số nguyên tố")
            elif lua_chon_bai3 == 'c':
                #Hàm đếm số các ước số là lẻ của n.
                so_uoc_so_le = doan.demuocsole(n)
                print(f"Số ước số lẻ của {n} là: {so_uoc_so_le}")
            elif lua_chon_bai3 == 'd':
                #Hàm đếm số các số nguyên tố nhỏ hơn n
                so_nguyen_to_nho_hon_n = doan.demsonguyentonhohonn(n)
                print(f"Số số nguyên tố nhỏ hơn {n} là: {so_nguyen_to_nho_hon_n}")
            elif lua_chon_bai3 == 'e':
                #Hàm tính tổng tất cả các ước số thực sự của n.
                tong_uoc_so_thuc_su = doan.tonguocsothucsu(n)
                print(f"Tổng tất cả các ước số thực sự của {n} là: {tong_uoc_so_thuc_su}")
        elif lua_chon_bai3 == '0':
            print("Đã chọn thoát. Kết thúc chương trình.")
            break
        else:
            print("Số không nằm trong khoảng từ 50 đến 150.")


def bai5():
    while True:
        menu.menubai5()
        lua_chon_bai5 = input("Nhập lựa chọn của bạn(1,2,3): ")
        Chuoi_1 = "Đây là ví dụ về chuỗi."
        Chuoi_2 = "ví dụ"
        k = 10
        if lua_chon_bai5 == '1':
            # Kiểm tra xem xâu Str2 có nằm trong Str1 hay không
            la_chuoi_con = doan.kiemtrachuoicon(Chuoi_1, Chuoi_2)
            if la_chuoi_con:
                print(f"Chuỗi 2 ({Chuoi_2}) nằm trong Chuỗi 1 ({Chuoi_1})")
            else:
                print(f"Chuỗi 2 ({Chuoi_2}) không nằm trong Chuỗi 1 ({Chuoi_1})")
        elif lua_chon_bai5 == '2':
            #Nếu có thì Str2 được xuất hiện (có thể chồng lên nhau) trong Str1 bao nhiêu lần.
            so_lan_xuat_hien = doan.demsolanxuathien(Chuoi_1, Chuoi_2)
            print(f"Số lần Chuỗi 2 xuất hiện trong Chuỗi 1: {so_lan_xuat_hien}")
        elif lua_chon_bai5 == '3':
            #Cho trước số k < length(Str1). Viết chương trình chèn xâu St2 vào Str1tại vị trí ký tự thứ k. In kết quả ra màn hình
            chuoi_moi = doan.chenchuoi(Chuoi_1, Chuoi_2, k)
            print(f"Sau khi chèn Chuỗi 2 vào vị trí {k}: {chuoi_moi}")
        elif lua_chon_bai5 == '0':
            print("Đã chọn thoát. Kết thúc chương trình.")
            break


def bai6():
    tap_hop_A = None
    tap_hop_B = None
    tap_hop_C = None
    while True:
        menu.menubai6()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            #Tạo tập hợp A
            tap_hop_A = doan.taotaphopA()
            doan.hien_thi_tap_hop(tap_hop_A, 'A')
        elif lua_chon == '2':
            #tạo tập hợp B từ tập hợp A
            if tap_hop_A is None:
                print("Tạo tập hợp A trước.")
            else:
                tap_hop_B = doan.taotaphopB(tap_hop_A)
                doan.hien_thi_tap_hop(tap_hop_B, 'B')
        elif lua_chon == '3':
            #Tạo tập hợp C từ tập hợp B
            if tap_hop_B is None:
                print("Tạo tập hợp B trước.")
            else:
                tap_hop_C = doan.taotaphopC(tap_hop_B)
                doan.hien_thi_tap_hop(tap_hop_C, 'C')
        elif lua_chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def bai7(dictionary):
    while True:
        menu.menubai7()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            #In điểm lớn nhất
            doan.indiemlonnhat(dictionary)
        elif lua_chon == '2':
            #In môn và điểm có điểm lớn nhất
            doan.inmondiemlonnhat(dictionary)
        elif lua_chon == '3':
            #In các điểm số chẵn
            doan.indiemsochan(dictionary)
        elif lua_chon == '4':
            #Tính trung bình các điểm
            doan.tinhtrungbinhdiem(dictionary)
        elif lua_chon == '5':
            #Tạo từ điển mới với các môn lớn hơn 7 điểm
            doan.taotudienmoi(dictionary)
        elif lua_chon == '6':
            #Đảo ngược từ điển
            doan.daonguoctudien(dictionary)
        elif lua_chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def bai8():
    while True:
        menu.menubai8()
        choice = input("Nhập lựa chọn của bạn: ")
        a, b, c = doan.random_numbers()
        if choice == '1':
            #Tính tổng hai số
            a, b = map(int, input("Nhập hai số cần tính tổng, cách nhau bởi dấu cách: ").split())
            print(f"Tổng của {a} và {b} là: {doan.tong(a, b)}")
        elif choice == '2':
            #Tính tích hai số
            a, b = map(int, input("Nhập hai số cần tính tích, cách nhau bởi dấu cách: ").split())
            print(f"Tích của {a} và {b} là: {doan.tich(a, b)}")
        elif choice == '3':
            #Tính lũy thừa
            a, b = map(int, input("Nhập số cơ sở và số mũ, cách nhau bởi dấu cách: ").split())
            print(f"{a} mũ {b} là: {doan.mu(a, b)}")
        elif choice == '4':
            #Tính căn bậc 2
            a = int(input("Nhập số cần tính căn bậc 2: "))
            print(f"Căn bậc 2 của {a} là: {doan.can_bac_2(a)}")
        elif choice == '5':
            #Tính hàm tan
            a = float(input("Nhập số cần tính hàm tan: "))
            print(f"Tan của {a} là: {doan.tan(a)}")
        elif choice == '6':
            #Giải phương trình bậc 2
            a, b, c = map(int, input(
                "Nhập hệ số a, b, c của phương trình ax^2 + bx + c = 0, cách nhau bởi dấu cách: ").split())
            print(f"Giai phương trình bậc 2: {doan.giai_ptb2(a, b, c)}")
        elif choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def bai9():
    while True:
        menu.menubai9()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            #Đọc dữ liệu từ tệp fin.txt và tính tổng các dãy số
            lines = doan.doc_du_lieu_tu_file("fin.txt")
            result = doan.tinh_tong_da_sos(lines)
            print(f"Tổng của các dãy số từ fin.txt là: {result}")
        elif choice == '2':
            # Xuất kết quả ra tệp fout.txt
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


def bai10():
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


def bai11():
    while True:
        menu.menubai11()
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


def chuong2():
    while True:
        menu.menuchuong2()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            #Thƣ viện NumPy
            bai12()
            pass
        elif lua_chon == '2':
            bai15()
            pass
        elif lua_chon == '0':
            print("Quay lại Menu chương.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
import numpy as np
def bai12():
    while True:
        menu.menubai12()
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            #Tạo vectơ x và ma trận A, B, C
            m = 4
            n = 3
            x = doan.vectorx(m)
            print("Vector x:")
            print(x)
            A = doan.matran(m, n)
            B = doan.matran(n, n)
            print("\nMa trận A:")
            print(A)
            print("\nMa trận B:")
            print(B)
            C = doan.matran(n, m)
            print("\nMa trận C:")
            print(C)
            print("Vectơ và các ma trận đã được tạo.")
        elif choice == '2':
            #Tính tích của vectơ x và ma trận A
            kq1 = doan.tichvector(x, A)
            print("\nTích của vectơ x và ma trận A:")
            print(kq1)
        elif choice == '3':
            #Tính tích của hai ma trận A và B
            kq2 = doan.tichh2mt(A, B)
            print("\nTích hai ma trận A và B:")
            print(kq2)
        elif choice == '4':
            #Tính tích của ma trận chuyển vị C và ma trận B
            kq3 = doan.tichcv(C, B)
            print("\nTích hai ma trận chuyển vị C và B:")
            print(kq3)
        elif choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")




def bai15():
    while True:
        menu.menubai15()
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            #Viết hàm giải hệ phương trình
            result_1 = doan.solve_equation()
            print("Kết quả của hệ phương trình:")
            print("x =", result_1[0])
            print("y =", result_1[1])
            print("z =", result_1[2])
        elif choice == '2':
            #Viết hàm tính giới hạn của hàm
            result_2 = doan.calculate_limit()
            print("Giới hạn của hàm khi x tiến tới 5 là:", result_2)
        elif choice == '3':
            #Viết hàm tính đạo hàm của hàm
            result_3 = doan.calculate_derivative()
            print("Đạo hàm của hàm là:", result_3)
        elif choice == '4':
            # nguyên hàm
            # Gọi hàm và in kết quả
            nguyham1 = doan.nguyeham()
            print("Nguyên hàm của f(x) là:", nguyham1)
        elif choice == '5':
            # tích phân
            result_4 = doan.calculate_integral_with_limits()
            print("Tích phân của hàm từ 0 đến 2pi/3 là:", result_4)
        elif choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")