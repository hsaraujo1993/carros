"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from carros.views import CarroNovoView, MarcaNovaView, CarrosLisView, CarroDetalheView, CarroUpdateView, CarroDeleteView
from contas.views import registro_view, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("carros/", CarrosLisView.as_view(), name="carros_lista"),
    path('carro_novo/', CarroNovoView.as_view(), name='carro_novo'),
    path("nova_marca/", MarcaNovaView.as_view(), name="nova_marca"),
    path("carro/<int:pk>/", CarroDetalheView.as_view(), name="carro_detalhe"),
    path("carro/<int:pk>/update/", CarroUpdateView.as_view(), name="carro_update"),
    path("carro/<int:pk>/delete/", CarroDeleteView.as_view(), name="carro_delete"),

    

    path("registro/", registro_view, name="registro"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
