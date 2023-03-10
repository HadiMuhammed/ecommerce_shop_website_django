# Generated by Django 3.2.16 on 2023-01-18 14:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
