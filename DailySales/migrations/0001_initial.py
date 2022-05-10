# Generated by Django 3.2.5 on 2022-04-18 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=80)),
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
                ('datesold', models.DateTimeField(auto_now_add=True)),
                ('paymentmethod', models.CharField(choices=[('CASH', 'cash'), ('TRANSFER', 'transfer')], default='CASH', max_length=40)),
                ('havepaid', models.BooleanField(default=False)),
                ('datepaid', models.DateTimeField(auto_now_add=True)),
                ('itemsold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soldItem', to='DailySales.itemsold')),
            ],
            options={
                'verbose_name_plural': 'Daily Sales',
            },
        ),
    ]
