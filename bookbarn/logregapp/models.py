from django.db import models
#from django.utils.translation import gettext_lazy as _
#from django.utils.timezone import now as timezone_now
#from imagekit.models import ImageSpecField
#from pilkit.processors import ResizeToFill
#import contextlib, os
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be in valid email format"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['pw_conf']:
            errors['pw_conf'] = "Passwords do not match"
        return errors

    def authenticate(self, email, password):
        user = self.filter(email=email)
        if not user:
            return False
        user = user[0]
        return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=60)
    photo = models.ImageField(upload_to='images/profile/', blank=True)
    address = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def set_photo(self):
        _photo = self.photo
        if not _photo:
            self.photo="../../media/images/profile/default_profile_pic.png"

    def __str__(self):
        return f'Profile for user {self.first_name}'
"""
def upload_to(instance, filename):
    now = timezone_now()
    base, extension = os.path.splitext(filename)
    extension = extension.lower()
    return f'images/profile/(instance.pk)(extension)'
"""
    