from rest_framework import serializers

from .models import Application, Configuration


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Model Serializer that validate and returns serialized objects for Application.
    """
    
    class Meta:
        model = Application
        fields = ('id', 'name', 'department',)


class ConfigurationSerializer(serializers.ModelSerializer):
    """
    Model Serializer used to visualize items from Configuration model.
    """
    
    class Meta:
        model = Configuration
        fields = ('id', 'created_at', 'updated_at', 'type_choice', 'roles_set',)


class ConfigurationCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Model Serializer used to create or update items from Configuration model.
    """
    
    class Meta:
        model = Configuration
        fields = ('type_choice', 'roles_set', 'application',)
