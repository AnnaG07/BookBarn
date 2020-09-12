from django.db import models
from logregapp.models import User
from django.utils.text import slugify
from django.conf import settings

class Book(models.Model):
    image = models.ImageField(upload_to='images/', default="")
    url = models.URLField(default="")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    listing_type = models.CharField(max_length=100)
    seller = models.ForeignKey(User, related_name="seller_books", on_delete=models.CASCADE)
    faves = models.ManyToManyField(User, related_name="faved_books", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/profile/', blank=True)
    address = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now=True)

    def set_photo(self):
        _photo = self.photo
        if not _photo:
            self.photo="images/profile/default_profile_pic.png"

    def __str__(self):
        return f'Profile for user {self.user.first_name}'