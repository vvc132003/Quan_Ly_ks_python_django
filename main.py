# n = input("Nhập dãy số: ")
# so_list = [float(x) for x in n.split()]
# tong = 0
# for so in so_list:
#     tong += so
# trungbinh = tong / len(so_list)
# print(f"Tổng của dãy: {tong}, Trung bình của dãy: {trungbinh}")

# A = [-1, 0, 5, -7, 6, 8]
# for x in A[:]:
#     if x < 0:
#         A.remove(x)
# print(A)

# ds = [
#     ["Chính", [2, 3, 4], [6, 7, 8]],
#     ["Ngọc", [5, 6, 9], [7, 8, 2]],
#     ["Uyên", [2, 3, 3], [6, 5, 9]]
# ]
# print("{:<12} {:<12} {:<12} {:<12} {:<12}".format("Tên", "Toán", "Lý", "Hoá", "Sinh"))
# for entry in ds:
#     ten = entry[0]
#     diem_mon1 = entry[1]
#     diem_mon2 = entry[2]
#     print("{:<12} {:<12} {:<12} {:<12} {:<12}".format(ten, *diem_mon1, *diem_mon2))
# In ma tran
# A = [[1,0,5],[13,-1,0],[2,16,-18],[10,9,-1]]
# B = [[4,-4,8],[3,10,-2],[6,-6,8],[1,-9,1]]
# for i in range(4):
#     for j in range(3):
#         print(A[i][j], end=" ")
#     print()
# tạo 1 ma trận m x n với các phần tử bằng 0
# m = 4
# n = 5
# b = []
# x = 0
# for i in range(m):
#     a = []
#     for j in range(n):
#         a.append(x)
#     b.append(a)
# for row in b:
#     print(row)

# tạo 1 ma trận m x n với các phần tử hàng tăng 1 từ 0
# m = 4
# n = 5
# b = []
# for i in range(m):
#     a = []
#     x = 0
#     for j in range(n):
#         a.append(x)
#         x += 1
#     b.append(a)
# for row in b:
#     print(row)
# tạo 1 ma trận m x n với các phần tử cột tăng 1 từ 0
m = 4
n = 5
c = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i)
    c.append(row)
for row in c:
    print(" ".join(map(str, row)))