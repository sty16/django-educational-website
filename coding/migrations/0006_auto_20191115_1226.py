# Generated by Django 2.2.6 on 2019-11-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0005_code_result_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='result_check',
            field=models.BooleanField(blank=True, default=False, verbose_name='人工审核结果'),
        ),
    ]
