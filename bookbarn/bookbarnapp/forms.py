from django import forms
from .models import Book #, Profile
from urllib import request
from django.core.files.base import ContentFile
from django.core.files.images import get_image_dimensions
from django.utils.text import slugify
from django.urls import reverse

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('url', 'title', 'desc', 'price', 'listing_type')

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1) [1].lower()
        print(url)
        return url
        
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        print(image, 'this is the image variable')
        print(image.image, 'this is my expected image path')
        if commit:
            image.save()
            print(image_url)
        return image
"""
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('photo', 'address')

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        try:
            w, h = get_image_dimensions(photo)
            max_width = max_height = 150
            if w > max_width or h > max_height:
                raise forms.ValidationError(u'Please use an image that is %s x %s pixels or smaller.' % (max_width, max_height))
            main, sub = photo.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, GIF OR PNG image')
            if len(photo) > (20 * 1024):
                raise forms.ValidationError(u'Picture file size may not exceed 20k.')
        except AttributeError:
            pass
        return photo

    def save(self, commit=True):
        user = super(MyChangeForm, self).save(commit=False)
        if user.photo:
            user.set_photo()
        if commit:
            user.save()
        return user
"""