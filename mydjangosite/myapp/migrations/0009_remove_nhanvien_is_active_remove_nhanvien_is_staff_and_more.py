# Generated by Django 4.2.6 on 2023-10-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_nhanvien_matkhau_alter_nhanvien_taikhoan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nhanvien',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='nhanvien',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='matKhau',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='taiKhoan',
            field=models.CharField(max_length=255),
        ),
    ]