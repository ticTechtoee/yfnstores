from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Products(models.Model):
    title = models.CharField(max_length=100)
    description =  CKEditor5Field()
    image1 = models.ImageField(upload_to='post_images/', default='post_images/default.jpg',blank=True, null=True)
    image2 = models.ImageField(upload_to='post_images/', default='post_images/default.jpg',blank=True, null=True)
    image3 = models.ImageField(upload_to='post_images/', default='post_images/default.jpg',blank=True, null=True)
    cardLink = models.URLField(max_length=500)
    def __str__(self):
        return self.title
