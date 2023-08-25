from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from Garagem2.views import (
    MarcaViewSet,
    CategoriaViewSet,
    CorViewSet,
    AcessorioViewSet,
    ModeloViewSet,
    VeiculoViewSet,
)

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
]
