import tkinter as tk
from tkinter import *
from tkinter import ttk
import bai14,vedothi


window = Tk()
window.title("Vẽ đồ thị")
window.geometry("400x200")

# button thêm sản phẩm
yenngua = tk.Button(window, text="Vẽ đồ thị mặt yên ngựa", width=20, bg="green", fg="white", font="arial 10 bold", command=bai14.yenngua)
yenngua.place(x=30, y=20)

# button cập nhật sản phẩm

hyperbolic = tk.Button(window, text="Vẽ đồ thị mặt hyperbolic", width=20, bg="orange", fg="white", font="arial 10 bold",command=bai14.hyperbolic)
hyperbolic.place(x=30, y=50)

# button xoá sản phẩm
matcau = Button(window, text="Vẽ đồ thị mặt cầu", width=20, bg="red", fg="white", font="arial 10 bold",command=bai14.matcau)
matcau.place(x=30, y=85)

bai13 = Button(window, text="Vẽ đồ thị hàm số y, y’, y” và y’’’ xét x ∈ [−10, 10]", bg="black", fg="white", font="arial 10 bold",command=vedothi.bai13)
bai13.place(x=30, y=120)

window.mainloop()
