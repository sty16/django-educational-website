# Generated by Django 2.2.1 on 2019-10-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='create_time',
            new_name='upload_time',
        ),
        migrations.RemoveField(
            model_name='file',
            name='title',
        ),
        migrations.AddField(
            model_name='file',
            name='checked',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
