# Generated by Django 3.2.9 on 2022-06-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthArea', '0003_alter_usermodel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'admin'), ('DIRECTOR', 'director'), ('SECRATARY', 'secratory'), ('OTHERS', 'others')], default='SECRATARY', max_length=20),
        ),
    ]