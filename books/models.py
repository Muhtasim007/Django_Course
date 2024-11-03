from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(default="2000-01-01")
    
    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=2000,default="")

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(default="2000-01-01")
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default= 0.00)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    def __str__(self):
        return self.title