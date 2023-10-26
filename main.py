# n = input("Nhập dãy số: ")
# so_list = [float(x) for x in n.split()]
# tong = 0
# for so in so_list:
#     tong += so
# trungbinh = tong / len(so_list)
# print(f"Tổng của dãy: {tong}, Trung bình của dãy: {trungbinh}")

A = [-1, 0, 5, -7, 6, 8]
for x in A[:]:
    if x < 0:
        A.remove(x)
print(A)