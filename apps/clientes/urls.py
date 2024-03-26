from django.urls import path, include
from rest_framework import routers
from apps.clientes.views import ClientesViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]