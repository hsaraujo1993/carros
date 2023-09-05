from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from carros.models import Carro, Marca
from carros.forms import CarroModelForm, MarcaModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

    
class CarrosLisView(ListView):
    model = Carro
    template_name = "carros.html"
    context_object_name = "carros"

    def get_queryset(self):
        carros = super().get_queryset().order_by("modelo")
        search = self.request.GET.get("search")
        if search:
            carros = carros.filter(modelo__icontains=search)
        return carros


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarroNovoView(CreateView):
    model = Carro
    form_class = CarroModelForm
    template_name = "carro_novo.html"
    success_url = "/carros/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class MarcaNovaView(CreateView):
    model = Marca
    form_class = MarcaModelForm
    template_name = "nova_marca.html"
    success_url = "/carros/"
    

@method_decorator(login_required(login_url="login"), name="dispatch")
class CarroDetalheView(DetailView):
    model = Carro
    template_name = "carro_detalhe.html"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarroUpdateView(UpdateView):
    model = Carro
    form_class = CarroModelForm
    template_name = "carro_update.html"

    def get_success_url(self):
        return reverse_lazy('carro_detalhe', kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarroDeleteView(DeleteView):
    model = Carro
    template_name = "carro_delete.html"
    success_url = "/carros/"

    

    

