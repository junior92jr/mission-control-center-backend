from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .common import MultiSerializerViewSet
from .models import (
    Application, 
    Configuration
)
from .serializers import (
    ApplicationSerializer,
    ConfigurationSerializer,
    ConfigurationCreateUpdateSerializer
)


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    Model Viewset that handles CRUD for Aplication Model.
    """

    serializer_class = ApplicationSerializer
    permission_classes = (AllowAny,)
    queryset = Application.objects.all()


class ConfigurationViewSet(MultiSerializerViewSet):
    """
    Model Viewset that handles CRUD for Configuration Model.
    """

    serializers = {
        'default': ConfigurationSerializer,
        'list': ConfigurationSerializer,
        'detail':  ConfigurationSerializer,
        'create': ConfigurationCreateUpdateSerializer,
        'update': ConfigurationCreateUpdateSerializer,
    }

    permission_classes = (AllowAny,)
    queryset = Configuration.objects.all()
