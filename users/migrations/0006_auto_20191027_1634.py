# Generated by Django 2.2.1 on 2019-10-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191025_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='user_image/default.png', upload_to='user_image/'),
        ),
    ]
