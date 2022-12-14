from email.policy import default
from django.db import models
from django.urls import reverse
from game_ecommerce_site.settings import AUTH_USER_MODEL

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("shop:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default="images/default.jpg")
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    # TODO: change so that there can be numerous platforms for a single product
    platforms = models.ManyToManyField(Platform, blank=True, related_name="product")
    release_date = models.DateField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("shop:product_item", args=[self.slug])
    
    def __str__(self):
        return self.title
