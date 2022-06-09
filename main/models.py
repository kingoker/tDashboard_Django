from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Модель для стоимости хлопка
class CottonPrice(models.Model):
    flag = models.ImageField(upload_to='flags/', verbose_name='Флаг')
    title = models.CharField(max_length=50, verbose_name='Название страны')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стоимость хлопка'
        verbose_name_plural = 'Стоимость хлопка'


# Модель профиля которая связана с User
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='', verbose_name='Название компании')
    mark = models.IntegerField(verbose_name='Оценка', default=0)
    log = models.ImageField(upload_to='logos/', verbose_name='Логотип', null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            p = Profile.objects.create(user=instance)
            p.title = instance.username

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


# Модель продукта
class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    order_to = models.ForeignKey('OrderTo', on_delete=models.PROTECT, verbose_name='Ордер на')
    product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT, verbose_name='Тип продукта')
    product_number = models.ForeignKey('ProductNumber', on_delete=models.PROTECT, verbose_name='Номер продукта')
    product_mark = models.ForeignKey('ProductMark', on_delete=models.PROTECT, verbose_name='Марка продукта')
    product_much = models.FloatField(verbose_name='Кол-во (млн. тон)')
    text = models.TextField(verbose_name='Примечания', null=True, blank=True)

    def __str__(self):
        return str(self.product_type)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


# Продажа Покупка
class OrderTo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ордер на', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип ордера'
        verbose_name_plural = 'Типы ордера'


# Виды прдукта
class ProductType(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип продукта', db_index=True)
    className = models.CharField(max_length=50, verbose_name='Класс иконки', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'


# Номер продукта
class ProductNumber(models.Model):
    title = models.CharField(max_length=50, verbose_name='Номер продукта', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Номер продукта'
        verbose_name_plural = 'Номера продуктов'


# Марка продукта
class ProductMark(models.Model):
    title = models.CharField(max_length=50, verbose_name='Марка продукта', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка продукта'
        verbose_name_plural = 'марки продуктов'


# Рейтинг компаний
class Rating(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Название компании')
    mark = models.IntegerField(verbose_name='Оценка', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pk', )
        verbose_name = 'Оценка компаний'
        verbose_name_plural = 'Оценка компании'

