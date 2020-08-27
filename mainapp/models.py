from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(max_length=400, unique=True, verbose_name='url')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=400, verbose_name='url', unique=True)
    image = models.ImageField(blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Покупатель')
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая Цена')

    def __str__(self):
        return f"Cart Product: {self.product.title}"


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True)
    total_products = models.PositiveIntegerField(default=0)
