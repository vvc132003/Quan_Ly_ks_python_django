import ham


if __name__ == '__main__':
    while True:
        print()
        print("|============================================|")
        print("|            ~~~~~  MENU  ~~~~~              |")
        print("|============================================|")
        print("| 1. CHƯƠNG 1: PYTHON CƠ BẢN                 |")
        print("| 2. CHƯƠNG 2: LẬP TRÌNH VỚI THƯ VIỆN        |")
        print("| 0.  THOÁT  <--|                            |")
        print("|============================================|")
        chuong = input("Nhập chương bạn muốn xem: ")
        if chuong == '1':
            ham.chuong1()
        elif chuong == '2':
            ham.chuong2()
        elif chuong == '0':
            print("Bạn đã chọn thoát. Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


