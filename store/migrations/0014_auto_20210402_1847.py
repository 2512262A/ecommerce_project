# Generated by Django 2.2.17 on 2021-04-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210330_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
