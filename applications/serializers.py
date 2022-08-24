from ensurepip import version
from rest_framework import serializers

from .models import Application, Configuration


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Model Serializer that validate and returns serialized objects for Application.
    """
    
    class Meta:
        model = Application
        fields = ('id', 'name','department', 'description',)


class ConfigurationSerializer(serializers.ModelSerializer):
    """
    Model Serializer used to visualize items from Configuration model.
    """
    
    class Meta:
        model = Configuration
        fields = ('id', 'created_at', 'updated_at', 'type_choice', 'roles_set', 'application',)


class ConfigurationCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Model Serializer used to create or update items from Configuration model.
    """
    
    class Meta:
        model = Configuration
        fields = ('type_choice', 'roles_set', 'application',)

    def update(self, instance, validated_data):
        
        if not instance.history_log:
            instance.history_log.append({
                'version': 1,
                'updated_at': instance.updated_at.strftime('%m.%d.%Y, %H:%M:%S'), 
                'roles_set': instance.roles_set
            })
        else:
            current_version = instance.history_log[-1].get('version')
            instance.history_log.append({
                'version': current_version + 1,
                'updated_at': instance.updated_at.strftime('%m.%d.%Y, %H:%M:%S'), 
                'roles_set': instance.roles_set
            })

        instance = super(
            ConfigurationCreateUpdateSerializer, self).update(
                instance, validated_data)
        
        return instance
