from django.db import models

# Create your models here.


class Slide(models.Model):
    
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=256)
    image = models.ImageField(upload_to='uploads')
    
    
    def __str__(self):
        return self.name



    
 
class Brand(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name  
    
class Category(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)
    options = models.TextField(max_length=512)
    price = models.IntegerField()
    image = models.ImageField(upload_to="uploads")
    
    
    # many to one
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand , on_delete=models.PROTECT)      
    
    
    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=264)
    phone = models.CharField(max_length=264)
    message = models.TextField(max_length=512)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس ها"