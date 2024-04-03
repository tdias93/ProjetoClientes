from rest_framework import serializers
from apps.clientes.models import Cliente
from apps.clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF invalido.'})
    
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua número nesse campo'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O CPF deve ter 9 dígitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O Celular deve seguir o modelo 11 99999-9999'})

        return data
