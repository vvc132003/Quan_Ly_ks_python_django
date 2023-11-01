# Generated by Django 4.2.6 on 2023-11-01 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_nhanvien_is_active_remove_nhanvien_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dichvu',
            name='image',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='dichvu',
            name='trangThai',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='khachhang',
            name='trangThai',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nhanvien',
            name='trangThai',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='taiKhoan',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
