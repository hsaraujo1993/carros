from django import forms
from carros.models import Carro, Marca


class CarroModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = "__all__"

    def clean_valor(self):
        valor = self.cleaned_data.get("valor")
        if valor < 10000:
            self.add_error("valor", "Valor minimo R$10.000,00")
        return valor


class MarcaModelForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        if Marca.objects.filter(nome=nome).exists():
            self.add_error("nome", "Marca já existe cadastrada!")
        return nome
