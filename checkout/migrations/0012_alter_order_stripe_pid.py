# Generated by Django 4.1.1 on 2023-09-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_alter_order_stripe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
