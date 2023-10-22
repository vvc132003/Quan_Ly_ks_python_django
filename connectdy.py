import mysql.connector

# Thông tin kết nối đến MySQL
db = mysql.connector.connect(user='root', password='chinh@2003', host='localhost', database='tesst')

# Tạo một con trỏ (cursor) để thao tác với cơ sở dữ liệu
mycursor = db.cursor()

# Câu lệnh SQL để tạo bảng
create_table_sql = """
CREATE TABLE IF NOT EXISTS mytable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
);
"""

# Thực hiện câu lệnh SQL để tạo bảng
mycursor.execute(create_table_sql)

# Commit thay đổi vào cơ sở dữ liệu
db.commit()

# Đóng kết nối khi hoàn thành
db.close()