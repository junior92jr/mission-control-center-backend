from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend



from .common import MultiSerializerViewSet
from .models import (
    Application, 
    Configuration
)
from .serializers import (
    VersionInputSerializer,
    ApplicationSerializer,
    ConfigurationSerializer,
    ConfigurationCreateUpdateSerializer,
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'application',
    )

    permission_classes = (AllowAny,)
    queryset = Configuration.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Overwrite the perform create method from viewsets.
        """
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = ConfigurationSerializer(serializer.instance)

        return Response(
            response.data, status=status.HTTP_201_CREATED, headers=headers)


    @action(methods=['get'], url_path=r'(?P<pk>\w+)/versions', detail=False)
    def versions(self, request, pk=None):
        """
        Perform get versions logic from Configurations.
        """

        input_serializer = VersionInputSerializer(data={'pk': pk})
        input_serializer.is_valid(raise_exception=True)

        configuration = get_object_or_404(Configuration, pk=pk)

        view_general_history = self.map_serialized_item_to_list(
            configuration.__to_dict__(), configuration.history_log)

        return Response(view_general_history)