# Generated by Django 4.2.2 on 2023-06-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0004_carro_imagem_carro_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='placa',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
