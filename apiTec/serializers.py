from rest_framework import serializers
from .models import User, Cliente

# Se llama esta funcion make_password para encriptar contraseña

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'id','name','email','numero','password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'name','email','username','password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.password = make_password(password) # estamos encriptando contraseña antes de guardar password
        instance.save()
        return instance
    
class clienteLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
