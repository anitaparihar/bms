# Generated by Django 2.2.5 on 2019-09-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0006_auto_20190927_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmsuser',
            name='user_role',
            field=models.CharField(choices=[('A', 'ADMIN'), ('S', 'SUBADMIN'), ('U', 'USER')], default='U', max_length=1, verbose_name='User Role'),
        ),
    ]