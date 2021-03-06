# Generated by Django 4.0.4 on 2022-05-21 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=80)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DailySales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('totalprice', models.IntegerField(default=0)),
                ('datesold', models.DateField(auto_now_add=True)),
                ('paymentmethod', models.CharField(choices=[('CASH', 'cash'), ('TRANSFER', 'transfer')], default='CASH', max_length=40)),
                ('havepaid', models.BooleanField(default=False)),
                ('datepaid', models.DateField(auto_now=True)),
                ('itemsold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soldItem', to='DailySales.products')),
            ],
            options={
                'verbose_name_plural': 'Daily Sales',
            },
        ),
    ]
