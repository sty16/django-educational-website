# Generated by Django 2.2.1 on 2019-10-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191025_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileverify',
            name='mobile',
            field=models.CharField(help_text='电话号码', max_length=11, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(help_text='电话号码', max_length=11, verbose_name='电话'),
        ),
    ]
