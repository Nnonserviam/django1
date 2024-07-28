# Generated by Django 4.2.13 on 2024-07-10 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_categorias_alter_pedido_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(related_name='pedidos', through='posts.PedidoProducto', to='posts.post'),
        ),
    ]
