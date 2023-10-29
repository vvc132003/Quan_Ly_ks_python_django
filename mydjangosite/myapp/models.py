from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Phong(models.Model):
    maPhong = models.AutoField(primary_key=True)
    soPhong = models.CharField(max_length=255)
    loaiPhong = models.CharField(max_length=255)
    tinhTrangPhong = models.CharField(max_length=255)
    giaTien = models.DecimalField(max_digits=10, decimal_places=2)



class NhanVien(models.Model):
    maNhanVien = models.AutoField(primary_key=True)
    hoVaTenDem = models.CharField(max_length=255)
    luong = models.DecimalField(max_digits=10, decimal_places=2)
    taiKhoan = models.CharField(max_length=255)
    matKhau = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    vaiTro = models.CharField(max_length=255)
    trangThai = models.CharField(max_length=255)

    def check_password(self, raw_password):
        # Thực hiện kiểm tra mật khẩu ở đây, ví dụ:
        return self.matKhau == raw_password


class KhachHang(models.Model):
    maKhachHang = models.AutoField(primary_key=True)
    hoVaTenDem = models.CharField(max_length=255)
    soDienThoai = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cccd = models.CharField(max_length=255)
    diaChi = models.TextField()
    taiKhoan = models.CharField(max_length=255)
    matKhau = models.CharField(max_length=255)
    trangThai = models.CharField(max_length=255)

    def check_password(self, raw_password):
        # Thực hiện kiểm tra mật khẩu ở đây, ví dụ:
        return self.matKhau == raw_password


class ThuePhong(models.Model):
    maThuePhong = models.AutoField(primary_key=True)
    khachHang = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name='thue_phong')
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE)
    ngayNhanPhong = models.DateField()
    ngayTraPhong = models.DateField()
    tongTien = models.DecimalField(max_digits=10, decimal_places=2)
    trangThai = models.CharField(max_length=255)
    tienDatCoc = models.DecimalField(max_digits=10, decimal_places=2)
    nhanVien = models.ForeignKey(NhanVien, on_delete=models.SET_NULL, null=True)


class DichVu(models.Model):
    maDichVu = models.AutoField(primary_key=True)
    tenDichVu = models.CharField(max_length=255)
    moTa = models.TextField()
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    trangThai = models.CharField(max_length=255)
    image = models.TextField()


class ThueDichVu(models.Model):
    maThueDichVu = models.AutoField(primary_key=True)
    thuePhong = models.ForeignKey(ThuePhong, on_delete=models.CASCADE, related_name='thue_dich_vu')
    dichVu = models.ForeignKey(DichVu, on_delete=models.CASCADE)
    nhanVien = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    soLuong = models.PositiveIntegerField()
    thanhTien = models.DecimalField(max_digits=10, decimal_places=2)

    def calculateTotalCost(self):
        return self.thanhTien * self.soLuong


class ChuyenPhong(models.Model):
    maChuyenPhong = models.AutoField(primary_key=True)
    khachHang = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name='chuyen_phong')
    phongCu = models.ForeignKey(Phong, on_delete=models.CASCADE, related_name='chuyen_phong_phong_cu')
    phongMoi = models.ForeignKey(Phong, on_delete=models.CASCADE, related_name='chuyen_phong_phong_moi')


class TraPhong(models.Model):
    maTraPhong = models.AutoField(primary_key=True)
    thuePhong = models.ForeignKey(ThuePhong, on_delete=models.CASCADE, related_name='tra_phong')
    ngayTraPhong = models.DateField()
    tongTien = models.DecimalField(max_digits=10, decimal_places=2)
    nhanVien = models.ForeignKey(NhanVien, on_delete=models.SET_NULL, null=True)


class NhanPhong(models.Model):
    maNhanPhong = models.AutoField(primary_key=True)
    thuePhong = models.ForeignKey(ThuePhong, on_delete=models.CASCADE, related_name='nhan_phong')
    ngayNhanPhong = models.DateField()
