import doan
import menu,ham


if __name__ == '__main__':
    while True:
        print("====== MENU ======")
        print("1. CHƢƠNG 1: PYTHON CƠ BẢN")
        print("2. CHƢƠNG 2: LẬP TRÌNH VỚI THƢ VIỆN")
        print("3. CHƢƠNG 3: LẬP TRÌNH NÂNG CAO")
        print("4. Thoát")
        print("==================")
        chuong = input("Nhập chương bạn muốn xem: ")
        if chuong == '1':
            ham.chuong_1_menu()
        elif chuong == '2':
            ham.chuong_2_menu()
        elif chuong == '3':
            menu.menu_chuong_3()
        elif chuong == '4':
            print("Bạn đã chọn thoát. Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


