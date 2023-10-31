# import mysql.connector
#
# # Thông tin kết nối đến MySQL
# db = mysql.connector.connect(user='root', password='chinh@2003', host='localhost', database='tesst')
#
# # Tạo một con trỏ (cursor) để thao tác với cơ sở dữ liệu
# mycursor = db.cursor()
#
# # Câu lệnh SQL để tạo bảng
# create_table_sql = """
# CREATE TABLE IF NOT EXISTS mytable (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT
# );
# """
#
# # Thực hiện câu lệnh SQL để tạo bảng
# mycursor.execute(create_table_sql)
#
# # Commit thay đổi vào cơ sở dữ liệu
# db.commit()
#
# # Đóng kết nối khi hoàn thành
# db.close()

import math
def ham(re):
    print(math.sqrt(16))
    print(math.radians(30))
    print(math.pi * (180 / math.pi))
    print(math.cos(30))
    print(math.tan(45))
    print(math.pow(9, 3))
    print(math.log(30))
    print(2 * math.pi * 30)
    return re;


def canbac2(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        return "vô nghiệm"


a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
result = canbac2(a, b, c)
print("Kết quả:", result)
