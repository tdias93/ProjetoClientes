from rest_framework import viewsets
from apps.clientes.serializers import ClienteSerializer
from apps.clientes.models import Cliente

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
