from django.db import models
from PIL import Image
class House(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    viloyat = models.CharField(max_length=100)
    tuman = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    qurilgan = models.IntegerField()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.img.path)
    

        output_size = (180, 130)
        img.thumbnail(output_size)
        img.save(self.img.path)
    