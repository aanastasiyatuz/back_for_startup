from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


MyUser = get_user_model()

class ProfileProvider(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='provider')
    email = models.CharField(max_length=50,unique=True)
    avatar = models.ImageField(upload_to='providers', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(primary_key=True, unique=True, blank=True)

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

class ProfileClient(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='client')
    email = models.CharField(max_length=50,unique=True)
    avatar = models.ImageField(upload_to='clients', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(primary_key=True, unique=True, blank=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)