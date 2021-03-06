# Generated by Django 4.0.4 on 2022-06-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_cottonprice_options_remove_profile_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название компании')),
                ('mark', models.IntegerField(default=0, verbose_name='Оценка')),
            ],
            options={
                'verbose_name': 'Оценка компаний',
                'verbose_name_plural': 'Оценка компании',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='log',
            field=models.ImageField(blank=True, null=True, upload_to='logos/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Название компании'),
        ),
    ]
