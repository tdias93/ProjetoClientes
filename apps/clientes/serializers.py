from rest_framework import serializers
from apps.clientes.models import Cliente
from apps.clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos'})
    
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua número nesse campo'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O CPF deve ter 9 dígitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O Celular deve ter no minimo 11 dígitos'})

        return data
