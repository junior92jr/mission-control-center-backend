from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Model Serializer that validate and returns serialized objects for Application.
    """
    
    class Meta:
        model = Application
        fields = ('name', 'department',)
