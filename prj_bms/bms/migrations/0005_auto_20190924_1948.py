# Generated by Django 2.2.5 on 2019-09-24 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0004_invoice_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='category_id',
            field=models.IntegerField(verbose_name='Category Id'),
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_shift_date', models.DateField(verbose_name='Stock Shift Date')),
                ('stock_shift_from', models.IntegerField(verbose_name='Stock Shift From Shop')),
                ('stock_shift_p', models.IntegerField(verbose_name='Stock Shift P')),
                ('stock_shift_q', models.IntegerField(verbose_name='Stock Shift Q')),
                ('stock_shift_n', models.IntegerField(verbose_name='Stock Shift N')),
                ('stock_shift_d', models.IntegerField(verbose_name='Stock Shift D')),
                ('stock_shift_l', models.IntegerField(verbose_name='Stock Shift L')),
                ('stock_shift_xg', models.IntegerField(verbose_name='Stock Shift XG')),
                ('stock_shift_y', models.IntegerField(verbose_name='Stock Shift Y')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Brand')),
                ('stock_shift_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Shop', verbose_name='Stock Shift To Shop')),
            ],
            options={
                'verbose_name': 'Shift',
                'verbose_name_plural': 'Shifts',
                'ordering': ['stock_shift_date'],
            },
        ),
    ]