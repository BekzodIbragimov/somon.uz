from django.db import models


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
    
    

>>>>>>> 1a67676f1c714e28035cf2145e493073804a6609
