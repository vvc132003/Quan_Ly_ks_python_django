# # 1) Cho list x = [[1], [1,2], [1,2,3], [1,2,3,4]]
# """Viết chương trình Python tính tổng tất cả các số trong list"""
# x = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
# sum = 0
#
# for i in x:
#     for number in i:
#         sum += number
# print("----------- Bài 1 -----------")
# print("Tổng các số trong list x:", sum)
# print("-" * 75)
# # 2)
# A = [[1, 0, 5], [13, -1, 0], [2, 16, -18], [10, 9, -1]]
#
# hang = len(A)
# cot = len(A[0])
# print("----------- Bài 2 -----------")
# print("Số hàng của ma trận A là:", hang)
# print("Số cột của ma trận A là:", cot)
# print("-" * 75)
#
#
# # 3)
# def ChangeRow(A, i, j):
#     if 0 <= i < len(A) and 0 <= j < len(A):
#         A[i], A[j] = A[j], A[i]
#
#
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("----------- Bài 3 -----------")
# print("In ma trận sau khi đổi vị trí")
# ChangeRow(A, 0, 1)
#
# for row in A:
#     print(row)
# print("-" * 75)
#
#
# # 4)
# def ChangeColumn(A, i, j):
#     if 0 <= i < len(A[0]) and 0 <= j < len(A[0]):
#         for row in A:
#             row[i], row[j] = row[j], row[i]
#
#
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("----------- Bài 4 -----------")
# print("In ma trận sau khi đổi vị trí")
# ChangeColumn(A, 0, 2)
#
# for row in A:
#     print(row)
# print("-" * 75)
#
#
# # 5
# def Sum(A, B):
#     rowA = len(A)
#     colA = len(A[0])
#     rowB = len(B)
#     colB = len(B[0])
#
#     if rowA != rowB or colA != colB:
#         raise ValueError("Hai ma trận không cùng kích thước !!")
#
#     C = [[0 for _ in range(colA)] for _ in range(rowA)]
#
#     for i in range(rowA):
#         for j in range(colA):
#             C[i][j] = A[i][j] + B[i][j]
#
#     return C
#
#
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# B = [[4, -4, 8], [3, 10, -2], [6, -6, 8]]
#
# C = Sum(A, B)
#
# print("5)  Ma trận C là tổng của 2 ma trận A,B:")
# for row in C:
#     print(row)
#
# print("-" * 75)
#
#
# # 6
# def Scalar(A, k):
#     row = len(A)
#     col = len(A[0])
#
#     C = [[0 for _ in range(col)] for _ in range(row)]
#
#     for i in range(row):
#         for j in range(col):
#             C[i][j] = k * A[i][j]
#
#     return C
#
#
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# k = 2.5
#
# C = Scalar(A, k)
# print("6) Ma trận C là kết quả của phép nhân:")
# for row in C:
#     print(row)
#
# print("-" * 75)
#
#
# # 7
# def Multiple(A, B):
#     rowsA = len(A)
#     columA = len(A[0])
#     rowsB = len(B)
#     columB = len(B[0])
#     if columA != rowsB:
#         raise ValueError("Số cột của ma trận A phải bằng số hàng của ma trận B")
#     C = [[0 for _ in range(columB)] for _ in range(rowsA)]
#     for i in range(rowsA):
#         for j in range(columB):
#             for k in range(columA):
#                 C[i][j] += A[i][k] * B[k][j]
#     return C
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[7, 8], [9, 10], [11, 12]]
#
# C = Multiple(A, B)
# print("7) Ma trận C là kết quả của phép nhân:")
# for row in C:
#     print(row)
from django.urls import path
import chinh
import random

a = random.randint(1, 100)
b = random.randint(1, 5)
print(a)
print(b)
print("tong :", chinh.tong(a, b))
print("tích :", chinh.tich(a, b))
print("mũ :", chinh.mu(a, b))
print("căn bậc 2:", chinh.canbac2(a))
print("sin :", chinh.sin(a))
print(chinh.giai_phuong_trinh_bac_1(a, b))