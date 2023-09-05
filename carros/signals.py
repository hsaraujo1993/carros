from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from carros.models import Carro, CarroInventario


def carro_update_estoque():
    contagem_carros = Carro.objects.all().count()
    carros_valor = Carro.objects.aggregate(valor_total = Sum('valor'))['valor_total']
    CarroInventario.objects.create(
        contagem_carros= contagem_carros,
        carros_valor= carros_valor)


@receiver(post_save, sender=Carro)
def carro_post_save(sender, instance, **kwargs):
    carro_update_estoque()


@receiver(post_delete, sender=Carro)
def carro_post_delete(sender, instance, **kwargs):
    carro_update_estoque()


@receiver(pre_save, sender=Carro)
def carro_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = ''


