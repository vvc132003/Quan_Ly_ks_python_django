# Generated by Django 4.2.6 on 2023-10-22 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_chuyenphong_dichvu_khachhang_nhanvien_thuedichvu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chuyenphong',
            name='khachHang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chuyen_phong_khach_hang', to='myapp.khachhang'),
        ),
        migrations.AlterField(
            model_name='chuyenphong',
            name='phongCu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chuyen_phong_phong_cu', to='myapp.phong'),
        ),
        migrations.AlterField(
            model_name='chuyenphong',
            name='phongMoi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chuyen_phong_phong_moi', to='myapp.phong'),
        ),
        migrations.AlterField(
            model_name='dichvu',
            name='danhSachThueDichVu',
            field=models.ManyToManyField(related_name='dich_vu_thue_dich_vu', to='myapp.thuedichvu'),
        ),
        migrations.AlterField(
            model_name='khachhang',
            name='danhSachThuePhong',
            field=models.ManyToManyField(related_name='khach_hang_thue_phong', to='myapp.thuephong'),
        ),
        migrations.AlterField(
            model_name='nhanphong',
            name='thuePhong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nhan_phong_thue_phong', to='myapp.thuephong'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='danhSachChuyenPhong',
            field=models.ManyToManyField(related_name='nhan_vien_chuyen_phong', to='myapp.chuyenphong'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='danhSachThueDichVu',
            field=models.ManyToManyField(related_name='nhan_vien_thue_dich_vu', to='myapp.thuedichvu'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='danhSachThuePhong',
            field=models.ManyToManyField(related_name='nhan_vien_thue_phong', to='myapp.thuephong'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='danhSachTraPhong',
            field=models.ManyToManyField(related_name='nhan_vien_tra_phong', to='myapp.traphong'),
        ),
        migrations.AlterField(
            model_name='phong',
            name='danhSachChuyenPhong',
            field=models.ManyToManyField(related_name='phong_chuyen_phong', to='myapp.chuyenphong'),
        ),
        migrations.AlterField(
            model_name='phong',
            name='danhSachThuePhong',
            field=models.ManyToManyField(related_name='phong_thue_phong', to='myapp.thuephong'),
        ),
        migrations.AlterField(
            model_name='thuedichvu',
            name='dichVu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thue_dich_vu_dich_vu', to='myapp.dichvu'),
        ),
        migrations.AlterField(
            model_name='thuedichvu',
            name='nhanVien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thue_dich_vu_nhan_vien', to='myapp.nhanvien'),
        ),
        migrations.AlterField(
            model_name='thuedichvu',
            name='thuePhong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thue_dich_vu_thue_phong', to='myapp.thuephong'),
        ),
        migrations.AlterField(
            model_name='thuephong',
            name='danhSachThueDichVu',
            field=models.ManyToManyField(related_name='thue_phong_thue_dich_vu', to='myapp.thuedichvu'),
        ),
        migrations.AlterField(
            model_name='thuephong',
            name='khachHang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thue_phong_khach_hang', to='myapp.khachhang'),
        ),
        migrations.AlterField(
            model_name='thuephong',
            name='nhanVien',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thue_phong_nhan_vien', to='myapp.nhanvien'),
        ),
        migrations.AlterField(
            model_name='thuephong',
            name='phong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thue_phong_phong', to='myapp.phong'),
        ),
        migrations.AlterField(
            model_name='traphong',
            name='nhanVien',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tra_phong_nhan_vien', to='myapp.nhanvien'),
        ),
        migrations.AlterField(
            model_name='traphong',
            name='thuePhong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tra_phong_thue_phong', to='myapp.thuephong'),
        ),
    ]
