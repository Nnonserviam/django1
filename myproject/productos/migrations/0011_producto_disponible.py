# Generated by Django 4.2.13 on 2024-11-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]