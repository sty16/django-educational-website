# Generated by Django 2.2.1 on 2019-11-14 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20191031_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False, verbose_name='管理员'),
        ),
    ]
