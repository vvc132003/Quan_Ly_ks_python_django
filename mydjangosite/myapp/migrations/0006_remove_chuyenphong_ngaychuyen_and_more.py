# Generated by Django 4.2.6 on 2023-10-22 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_chuyenphong_khachhang_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chuyenphong',
            name='ngayChuyen',
        ),
        migrations.RemoveField(
            model_name='chuyenphong',
            name='tienChuyenPhong',
        ),
        migrations.RemoveField(
            model_name='dichvu',
            name='danhSachThueDichVu',
        ),
        migrations.RemoveField(
            model_name='dichvu',
            name='image',
        ),
        migrations.RemoveField(
            model_name='khachhang',
            name='danhSachThuePhong',
        ),
        migrations.RemoveField(
            model_name='nhanvien',
            name='danhSachChuyenPhong',
        ),
        migrations.RemoveField(
            model_name='nhanvien',
            name='danhSachThueDichVu',
        ),
        migrations.RemoveField(
            model_name='nhanvien',
            name='danhSachThuePhong',
        ),
        migrations.RemoveField(
            model_name='nhanvien',
            name='danhSachTraPhong',
        ),
        migrations.RemoveField(
            model_name='phong',
            name='danhSachChuyenPhong',
        ),
        migrations.RemoveField(
            model_name='phong',
            name='danhSachThuePhong',
        ),
        migrations.RemoveField(
            model_name='thuephong',
            name='danhSachThueDichVu',
        ),
        migrations.AlterField(
            model_name='chuyenphong',
            name='khachHang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chuyen_phong', to='myapp.khachhang'),
        ),
        migrations.AlterField(
            model_name='nhanphong',
            name='thuePhong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nhan_phong', to='myapp.thuephong'),
        ),
        migrations.AlterField(
            model_name='thuedichvu',
            name='dichVu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dichvu'),
        ),
        migrations.AlterField(
            model_name='thuedichvu',
            name='nhanVien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.nhanvien'),
        ),
        migrations.AlterField(
            model_name='thuedichvu',
            name='thuePhong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thue_dich_vu', to='myapp.thuephong'),
        ),
        migrations.AlterField(
            model_name='thuephong',
            name='khachHang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thue_phong', to='myapp.khachhang'),
        ),
        migrations.AlterField(
            model_name='thuephong',
            name='nhanVien',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.nhanvien'),
        ),
        migrations.AlterField(
            model_name='thuephong',
            name='phong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.phong'),
        ),
        migrations.AlterField(
            model_name='traphong',
            name='nhanVien',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.nhanvien'),
        ),
        migrations.AlterField(
            model_name='traphong',
            name='thuePhong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tra_phong', to='myapp.thuephong'),
        ),
    ]
