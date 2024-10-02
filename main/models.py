from django.db import models
from django.utils.text import slugify

from accounts.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to="product_images/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return self.product.title
    

class Services(models.Model):
    image = models.ImageField(upload_to="services_images/", null=True, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to="team_images/", null=True, blank=True)
    fullname = models.CharField(max_length=150)
    job = models.CharField(max_length=150)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.fullname
    

class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)


class UserContact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self) -> str:
        return self.firstname


class NewsLetter(models.Model):
    email = models.EmailField(max_length=250)

    def __str__(self) -> str:
        return self.email
    