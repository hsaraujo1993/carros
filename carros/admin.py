from django.contrib import admin
from carros.models import Carro, Marca


# Register your models here.


class CarroAdmin(admin.ModelAdmin):
    list_display = ("id", "modelo", "marca", "ano", "valor")
    search_fields = ("id", "modelo", "marca", "ano", "valor")


admin.site.register(Carro, CarroAdmin)


class MarcaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


admin.site.register(Marca, MarcaAdmin)
