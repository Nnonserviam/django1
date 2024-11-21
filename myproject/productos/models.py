from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"

class Producto(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='images/', default='images/luffy.png', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
            slug_unico = self.slug
            contador = 1
            if Producto.objects.filter(slug=slug_unico).exists():
                slug_unico = f"{self.slug}-{contador}"
                contador += 1
            self.slug = slug_unico
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
