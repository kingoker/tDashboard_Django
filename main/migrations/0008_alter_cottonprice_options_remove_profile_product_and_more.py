# Generated by Django 4.0.4 on 2022-06-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cottonprice',
            options={'verbose_name': 'Стоимость хлопка', 'verbose_name_plural': 'Стоимость хлопка'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='product',
        ),
        migrations.AlterField(
            model_name='profile',
            name='log',
            field=models.ImageField(blank=True, null=True, upload_to='flags/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(default='user.username', max_length=100, verbose_name='Название компании'),
        ),
    ]
