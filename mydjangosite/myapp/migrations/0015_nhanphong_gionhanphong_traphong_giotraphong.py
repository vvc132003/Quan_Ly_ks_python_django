# Generated by Django 4.2.6 on 2023-11-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_thuephong_gionhanphong_thuephong_giotraphong'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanphong',
            name='gioNhanPhong',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='traphong',
            name='gioTraPhong',
            field=models.TimeField(default='00:00'),
        ),
    ]
