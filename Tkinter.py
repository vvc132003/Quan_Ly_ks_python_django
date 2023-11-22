import tkinter as tk
from tkinter import *
from tkinter import ttk
import ketnoicsdl

cursor = ketnoicsdl.connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS san_pham (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        ten TEXT NOT NULL,
        gia INTEGER NOT NULL,
        mo_ta TEXT,
        ngay_them DATE NOT NULL,
        so_luong_con INTEGER NOT NULL,
        trang_thai BOOLEAN NOT NULL
    )
''')
def hien_thi_danh_sach_san_pham():
    try:
        for row in tree.get_children():
            tree.delete(row)
        with ketnoicsdl.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM san_pham")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", "end", values=row)
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu từ CSDL: {str(e)}")

def them_san_pham():
    ten_san_pham = entrytensanpham.get()
    gia_san_pham = entrygiasanpham.get()
    mo_ta = entrymota.get()
    ngay_them = entryngaythem.get()
    so_luong_con = entrysoluongcon.get()
    selected_option = radio_var.get()
    with ketnoicsdl.connection.cursor() as cursor:
        cursor.execute("INSERT INTO san_pham (ten, gia, mo_ta, ngay_them, so_luong_con,trang_thai) VALUES (%s, %s, %s, %s, %s, %s)",
                       (ten_san_pham, gia_san_pham, mo_ta, ngay_them, so_luong_con,selected_option))
        ketnoicsdl.connection.commit()
        hien_thi_danh_sach_san_pham()



def get_selected_product(event):
    # Lấy dòng sản phẩm được chọn từ Treeview
    selected_item = tree.focus()
    product = tree.item(selected_item, 'values')
    # Hiển thị thông tin sản phẩm lên các Entry/Label
    entrytensanpham.delete(0, END)
    entrytensanpham.insert(0, product[1])  # Tên sản phẩm
    entrygiasanpham.delete(0, END)
    entrygiasanpham.insert(0, product[2])  # Giá sản phẩm
    entrymota.delete(0, END)
    entrymota.insert(0, product[3])  # Mô tả
    entryngaythem.delete(0, END)
    entryngaythem.insert(0, product[4])  # Ngày thêm
    entrysoluongcon.delete(0, END)
    entrysoluongcon.insert(0, product[5])  # Số lượng còn
def cap_nhat_san_pham():
    selected_item = tree.focus()
    product = tree.item(selected_item, 'values')
    ten_san_pham = entrytensanpham.get()
    gia_san_pham = entrygiasanpham.get()
    mo_ta = entrymota.get()
    ngay_them = entryngaythem.get()
    so_luong_con = entrysoluongcon.get()

    with ketnoicsdl.connection.cursor() as cursor:
        cursor.execute("UPDATE san_pham SET ten = %s, gia = %s, mo_ta = %s, ngay_them = %s, so_luong_con = %s WHERE id = %s",
                       (ten_san_pham, gia_san_pham, mo_ta, ngay_them, so_luong_con, product[0]))
        ketnoicsdl.connection.commit()
        hien_thi_danh_sach_san_pham()


def xoa_san_pham():
    selected_item = tree.focus()
    product = tree.item(selected_item, 'values')
    product_id = product[0]  # Lấy ID của sản phẩm được chọn

    # Xoá sản phẩm dựa trên ID
    with ketnoicsdl.connection.cursor() as cursor:
        cursor.execute("DELETE FROM san_pham WHERE id = %s", (product_id,))
        ketnoicsdl.connection.commit()
        hien_thi_danh_sach_san_pham()

def on_radio_select():
    selected_option = radio_var.get()
    print("Selected option:", selected_option)

window = Tk()
window.title("Quản lý ản phẩm")
window.geometry("1260x500")

# ten sản phẩm
tensanpham = Label(window, text="Tên sản phẩm:", font="arial 10 bold", fg="green")
tensanpham.place(x=30, y=20)
entrytensanpham = Entry(window, font="arial 10 bold", bg="white", fg="black", bd=4, width=25)
entrytensanpham.place(x=150, y=20)

# giá sản phẩm
giasanpham = Label(window, text="Gía sản phẩm:", font="arial 10 bold", fg="green")
giasanpham.place(x=30, y=50)
entrygiasanpham = Entry(window, font="arial 10 bold", bg="white", fg="black", bd=4, width=25)
entrygiasanpham.place(x=150, y=50)

# mô tả
mota = Label(window, text="Mô tả:", font="arial 10 bold", fg="green")
mota.place(x=30, y=80)
entrymota = Entry(window, font="arial 10 bold", bg="white", fg="black", bd=4, width=25)
entrymota.place(x=150, y=80)

# ngày thêm
ngaythem = Label(window, text="Ngày thêm:", font="arial 10 bold", fg="green")
ngaythem.place(x=380, y=20)
entryngaythem = Entry(window, font="arial 10 bold", bg="white", fg="black", bd=4, width=25)
entryngaythem.place(x=480, y=20)

# Số lượng còn
soluongcon = Label(window, text="Số lượng còn:", font="arial 10 bold", fg="green")
soluongcon.place(x=380, y=50)
entrysoluongcon = Entry(window, font="arial 10 bold", bg="white", fg="black", bd=4, width=25)
entrysoluongcon.place(x=480, y=50)



# Tạo biến để lưu trạng thái của radio button
radio_var = tk.StringVar()
# Tạo các radio button và liên kết với biến trạng thái
radiobutton = Label(window, text="Trạng thái:", font="arial 10 bold", fg="green")
radiobutton.place(x=380, y=80)

radio_button1 = tk.Radiobutton(window, text="True", variable=radio_var, value="1", command=on_radio_select)
radio_button1.place(x=480, y=80)

radio_button2 = tk.Radiobutton(window, text="False", variable=radio_var, value="0", command=on_radio_select)
radio_button2.place(x=580, y=80)


# button thêm sản phẩm
btnthemsanpham = tk.Button(window, text="Thêm sản phẩm", width=20, bg="green", fg="white", font="arial 10 bold", command=them_san_pham)
btnthemsanpham.place(x=780, y=20)

# button cập nhật sản phẩm

btncapnhatsanpham = tk.Button(window, text="Cập nhật sản phẩm", width=20, bg="orange", fg="white", font="arial 10 bold",command=cap_nhat_san_pham)
btncapnhatsanpham.place(x=780, y=50)

# button xoá sản phẩm
btnxoasanpham = Button(window, text="Xoá sản phẩm", width=20, bg="red", fg="white", font="arial 10 bold",command=xoa_san_pham)
btnxoasanpham.place(x=780, y=85)


# Khung chứa Treeview
tablesanpham = tk.Frame(window)
tablesanpham.place(x=30, y=150)

# Tạo Treeview để hiển thị danh sách sản phẩm
tree = ttk.Treeview(tablesanpham, columns=("Id","Tên sản phẩm", "Giá", "Mô tả", "Ngày thêm", "Số lượng còn"), show="headings")
tree.heading("Id", text="Id", anchor=tk.CENTER)
tree.heading("Tên sản phẩm", text="Tên sản phẩm", anchor=tk.CENTER)
tree.heading("Giá", text="Giá", anchor=tk.CENTER)
tree.heading("Mô tả", text="Mô tả", anchor=tk.CENTER)
tree.heading("Ngày thêm", text="Ngày thêm", anchor=tk.CENTER)
tree.heading("Số lượng còn", text="Số lượng còn", anchor=tk.CENTER)
for col in tree["columns"]:
    tree.column(col, anchor=tk.CENTER)
tree.bind('<ButtonRelease-1>', get_selected_product)
tree.pack()
hien_thi_danh_sach_san_pham()
window.mainloop()
