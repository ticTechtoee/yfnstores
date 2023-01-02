from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100)
    description =  models.TextField()
    image1 = models.ImageField(upload_to='post_images/',blank=True, null=True)
    image2 = models.ImageField(upload_to='post_images/',blank=True, null=True)
    image3 = models.ImageField(upload_to='post_images/',blank=True, null=True)
    cardImage = models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.title
