# Generated by Django 2.2.5 on 2019-09-27 12:57

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0004_stockopen'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockClose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close_date', models.DateField(verbose_name='Stock Close Date')),
                ('close_qty_p', models.IntegerField(verbose_name='Stock Close P')),
                ('close_qty_q', models.IntegerField(verbose_name='Stock Close Q')),
                ('close_qty_n', models.IntegerField(verbose_name='Stock Close N')),
                ('close_qty_d', models.IntegerField(verbose_name='Stock Close D')),
                ('close_qty_l', models.IntegerField(verbose_name='Stock Close L')),
                ('close_qty_xg', models.IntegerField(verbose_name='Stock Close XG')),
                ('close_qty_y', models.IntegerField(verbose_name='Stock Close Y')),
                ('close_sale_p', models.IntegerField(verbose_name='Stock Close P')),
                ('close_sale_q', models.IntegerField(verbose_name='Stock Close Q')),
                ('close_sale_n', models.IntegerField(verbose_name='Stock Close N')),
                ('close_sale_d', models.IntegerField(verbose_name='Stock Close D')),
                ('close_sale_l', models.IntegerField(verbose_name='Stock Close L')),
                ('close_sale_xg', models.IntegerField(verbose_name='Stock Close XG')),
                ('close_sale_y', models.IntegerField(verbose_name='Stock Close Y')),
                ('total_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Category', verbose_name='Stock Category')),
                ('close_shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Shop', verbose_name='Stock Close Shop')),
            ],
            options={
                'verbose_name': 'StockClose',
                'verbose_name_plural': 'StockCloses',
                'ordering': ['close_date'],
            },
        ),
    ]
