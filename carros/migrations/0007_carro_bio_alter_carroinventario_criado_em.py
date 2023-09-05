# Generated by Django 4.2.2 on 2023-08-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0006_carroinventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carroinventario',
            name='criado_em',
            field=models.DateField(auto_now_add=True),
        ),
    ]
