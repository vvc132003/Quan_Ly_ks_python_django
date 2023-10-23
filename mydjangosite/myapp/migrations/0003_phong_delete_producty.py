# Generated by Django 4.2.6 on 2023-10-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_producty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phong',
            fields=[
                ('maPhong', models.AutoField(primary_key=True, serialize=False)),
                ('soPhong', models.CharField(max_length=255)),
                ('loaiPhong', models.CharField(max_length=255)),
                ('tinhTrangPhong', models.CharField(max_length=255)),
                ('giaTien', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Producty',
        ),
    ]