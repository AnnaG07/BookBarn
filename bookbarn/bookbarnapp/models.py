from django.db import models
from logregapp.models import User
from django.utils.text import slugify

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
    requests = models.ManyToManyField(User, related_name="requested_books", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Requests(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, related_name="requested_book", on_delete=models.CASCADE)
    requestor = models.ForeignKey(User, related_name="book_requestor", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    request = models.ForeignKey(Requests, related_name="comment_request", on_delete=models.CASCADE)
    poster = models.ForeignKey(User, related_name="poster_comment", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)