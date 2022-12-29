from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100)
    description =  models.TextField()

    def __str__(self):
        return self.title

class Images(models.Model):
    image = models.ImageField()
    product = models.ForeignKey("Products", on_delete=models.PROTECT)