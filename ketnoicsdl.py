import pymysql

# Thay thế các giá trị bên dưới bằng thông tin cơ sở dữ liệu MySQL của bạn
host = 'localhost'
user = 'root'
password = 'chinh@2003'
database = 'test'

# Kết nối đến MySQL
connection = pymysql.connect(host=host, user=user, password=password, database=database)