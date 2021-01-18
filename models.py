from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class ViewBook(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        abstract = True  # зависит от какого-либо объекта(в нашем случае 'Book'), то есть не показывается без подкласса

    title = models.CharField('Название', max_length=200)
    author = models.CharField('Автор', max_length=70)
    image = models.ImageField('Изображение')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Cart(models.Model):  # создаем класс корзина
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct', blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)


class CartProduct(models.Model):  # создаем класс который находится в корзине и в корзине этот класс можно арендовать
    Customer = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name='корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "Продукт: {}".format(self.product.title)


class Customer(models.Model):  # создаём модель пользователя
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Book(ViewBook):  # используя наследование берём фичи у ViewBook
    pages = models.CharField(max_length=4, verbose_name='количество страниц')

    def __str__(self):
        return self.title
