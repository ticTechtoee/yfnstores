# Generated by Django 3.2.16 on 2023-01-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_products_cardimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
