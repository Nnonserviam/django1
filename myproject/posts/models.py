from django.db import models

# Create your models here.

class Post(models.Model):
    idPost = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    slug = models.SlugField()
    date =models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='luffy.png', blank=True)

    def __str__(self):
        return self.nombre