# Generated by Django 4.1.1 on 2023-08-20 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_rename_active_coupon_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
