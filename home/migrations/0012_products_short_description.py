# Generated by Django 4.1.5 on 2023-01-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='short_description',
            field=models.CharField(default='Please Click the Title for Detailed Description.', max_length=100),
        ),
    ]
