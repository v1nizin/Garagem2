from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from uploader.router import router as uploader_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

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
    path("api/", include(router.urls)),
    path("api/usuario", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)